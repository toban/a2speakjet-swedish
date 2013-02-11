# -*- coding: iso-8859-1 -*-

def format_lexikon(input,output):
	
	fin = open(input, 'r')
	fout = open(output, 'w')
	word_count = 0
	
	for line in fin:
		
		if(line[:5] != 'LEMMA'):
			
			if(line[0] != '\n'):
				word_count += 1
				line_split =  line.split('\t')
				fout.write(line_split[0] + " = " + line_split[2])
	
	print "read",word_count,"words."

	

format_lexikon("sv_lex", "sv_lex_formatted")



