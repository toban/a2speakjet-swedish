from serial import *
from array import *
import sampa_to_speakjet_se
from Tkinter import *
from time import *

SERIAL_DEVICE = '/dev/ttyUSB1'

def sampaToSpeakjet(input,map):

	input_split = input.split()
	code = array('i')
	
	total_count = len(input_split)
	found_count = 0
	
	for part in input_split:
	
		if(map.has_key(part)):
			found_count += 1
			if(type(map[part]) == tuple):
				for i in map[part]:
					code.append(i)
			else:
				code.append(map[part])
		
	status = "NOT CORRECT!"
	if(total_count == found_count):
		status = "CORRECT!"
		
	print "Converting:",input,"total parts:",total_count,"found parts",found_count,status

	
	return code
	

def generateCode(string):
	
	output = array('i', [20,96,21,114,22,88,23,5])
	output_string = ""
	
	for i in string:
		output.append(lex[i])
	
	for i in output:
		output_string += chr(i)
	
		
	
	return output_string
	
def writeToArduino(string,device):
	
	try:
		ser = Serial(device, 9600)
		ser.write(string)
		
	except SerialException:
		print "Device not ready."
		return

def getSampa(input, file):
	
	f = open(file,'r')
	
	for line in f:
		
		word = line.split(' = ')
		
		if(word[0] == input):
			print "Found word"
			return word[1]
	
	return -1

def lookupAndConvert(input,lexikon):

	sampa_string = getSampa(input,lexikon)

	speakjet_code = -1
	
	if(sampa_string != -1):
		
		speakjet_code = sampaToSpeakjet(sampa_string,sampa_to_speakjet_se.map)
	
	return speakjet_code

code = 0

class partContainer:

	def __init__(self,master,value):
	
		self.value = value
		self.frame = Frame(master)
		self.frame.pack(side=LEFT,fill=BOTH,expand=1)
		
		self.label = Label(self.frame, text=value)
		self.label.pack()

class command(partContainer):
	
	def __init__(self,master,value):
		partContainer.__init__(self,master,value)
		return
		
class fonem(partContainer):
	

	
	def __init__(self,master,value, st, sl):
		partContainer.__init__(self,master,value)
		
		self.doStress = IntVar()
		self.doSlow = IntVar()
		self.pitch = IntVar()
		
		self.doStress.set(st)	
		self.doSlow.set(sl)
		self.pitch.set(88)
		
		self.speedVar = IntVar()
		
		self.speedVar.set(114)
		self.speedSlide = Scale(self.frame,variable=self.speedVar,from_=1,to=127,width=5)
		self.speedSlide.pack()
		
		self.pitchSlide = Scale(self.frame,variable=self.pitch,from_=1,to=255,width=5)
		self.pitchSlide.pack()
		
		self.stress = Checkbutton(self.frame,variable = self.doStress,text="st")

		self.stress.pack()
		
		self.slow = Checkbutton(self.frame,variable = self.doSlow,text="sl")
		self.slow.pack()
		
	'''
	TODO:
	
	'''
	def remove(self):
		print "REMOVE"
		self.speedSlide.pack_forget()
		self.stress.pack_forget()
		self.pitchSlide.pack_forget()
		self.slow.pack_forget()
		self.label.pack_forget()
		self.frame.pack_forget()


		
class App:

    def __init__(self, master):

		self.frame = Frame(master)
		self.frame.pack(fill=BOTH,expand=1,padx=10,pady=10)
		
		self.partFrame = Frame(self.frame,relief=RAISED, borderwidth=1)
		self.partFrame.pack(fill=BOTH,expand=1,padx=10,pady=10)
		
		entryFrame = Frame(self.frame, relief=RAISED, borderwidth=1)
		entryFrame.pack(fill=BOTH,expand=1,padx=10,pady=10)
		
		
		self.entryVar = ""
		self.wordEntry = Entry(entryFrame,textvariable=self.entryVar)
		self.wordEntry.pack(fill=BOTH,expand=1,side=LEFT)
		
		self.processBtn = Button(entryFrame,text="LOOKUP", command=self.startLookup)
		self.processBtn.pack(side=RIGHT)
		
		self.bendVar = IntVar()
		self.bendVar.set(5)
		self.bendSlide = Scale(self.frame,variable=self.bendVar,from_=1, to=15,label="voice")
		self.bendSlide.pack(fill=BOTH,expand=1,side=LEFT)
		
		self.volVar = IntVar()
		self.volVar.set(100)
		self.volSlide = Scale(self.frame,variable=self.volVar,from_=0, to=127,label="volume")
		self.volSlide.pack(fill=BOTH,expand=1,side=LEFT)
		
		self.partList = list()
		
		self.pitchEnv1 = Button(self.frame, text="ENV TRI", command=self.makePitchTri)
		self.pitchEnv1.pack(fill=BOTH,expand=1,side=LEFT)
		
		self.pitchEnv2 = Button(self.frame, text="ENV RISE-SLOPE ", command=self.makePitchRise)
		self.pitchEnv2.pack(fill=BOTH,expand=1,side=LEFT)
		
		self.pitchEnv3 = Button(self.frame, text="ENV DESC-SLOPE ", command=self.makePitchDesc)
		self.pitchEnv3.pack(fill=BOTH,expand=1,side=LEFT)
		
		self.sendbutton = Button(self.frame, text="SEND", command=self.send, bg="GREEN")
		self.sendbutton.pack(fill=BOTH,expand=1,side=LEFT)
        


    def send(self):
		arr = array('i')

		arr.append(20) # volume
		arr.append(self.volVar.get())
		arr.append(23) # bend
		arr.append(self.bendVar.get())
		for i in self.partList:

			if(i.doStress.get() == True):
				arr.append(14) # stress
			elif(i.doSlow.get() == True):
				arr.append(8) # slow
			
			
			arr.append(21) # speed
			arr.append(i.speedVar.get())
			arr.append(22) # pitch
			arr.append(i.pitch.get())
			arr.append(i.value)
		
		code_str = ""
		
		for i in arr:
			code_str += chr(i);
		
		print "SENT:",arr
		print SERIAL_DEVICE
		writeToArduino(code_str,SERIAL_DEVICE)
	
    def makePitchTri(self):
		
		int = 88
		stepSize = ((255+88) / (1.0+len(self.partList))) 
		index = 0
		for i in self.partList:
			
			if(index >= len(self.partList)/2):
				int-=stepSize
			else:
				int+=stepSize
				
			i.pitch.set(int)
			
			index+=1
			
    def makePitchRise(self):
		
		int = 88
		stepSize = ((255-88) / (1.0+len(self.partList))) 

		index = 0
		for i in self.partList:

			int+=stepSize
				
			i.pitch.set(int)
			
			index+=1
    def makePitchDesc(self):
    
		int = 255
		stepSize = ((255-88) / (1.0+len(self.partList))) 
		index = 0
		for i in self.partList:

			int-=stepSize
				
			i.pitch.set(int)
			
			index+=1
		
    def startLookup(self):
    
		tmp = lookupAndConvert(self.wordEntry.get().encode('utf-8'),"sv_lex_formatted_utf8")
		print self.wordEntry.get()
		if(tmp!=-1):
			it = iter(tmp)
			for i in self.partList:
				i.remove()
			self.partList = list()
			try:
				while(1):
					doStress = False
					doSlow = False
					
					i = it.next()
					if(i==8):
						doSlow = True
						i = it.next()
					if(i==14):
						doStress = True
						i = it.next()
					
					self.partList.append(fonem(self.partFrame,i,doStress,doSlow))
			except StopIteration:
				pass

		
root = Tk()
root.title("SpeakJet 2 Sampa")

app = App(root)

root.mainloop()





