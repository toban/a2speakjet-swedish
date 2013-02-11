# -*- coding: iso-8859-1 -*-
'''
Consonants
There are six plosives:

	Symbol		Word		Transcription
	p		pil		pi:l
	b		bil		bi:l
	t		tal		tA:l
	d		dal		dA:l
	k		kal		kA:l
	g		gås		go:s
	
There are six fricatives:

	f		fil		fi:l
	v		vår		vo:r
	s		sil		si:l
	S		sjuk		S}:k	(front and back allophones#)
	h		hal		hA:l
	C		tjock		COk	(not syllable-final)
	
	

There are six sonorant consonants (nasals, liquids and semivowels):

	m		mil		mi:l
	n		nål		no:l
	N		ring		rIN	(not syllable-initial)
	r		ris		ri:s
	l		lös		l2:s
	j		jag		jA:g

Vowels
There are nine long and nine short vowels.

Long vowels (followed by short consonant):

	i:		vit		vi:t
	e:		vet		ve:t
	E:		säl		sE:l
	y:		syl		sy:l
	}:		hus		h}:s
	2:		föl		f2:l
	u:		sol		su:l
	o:		hål		ho:l
	A:		hal		hA:l
	

Short vowels (followed by long consonant):

	I		vitt		vIt
	e		vett		vet
	E		rätt		rEt
	Y		bytt		bYt
	u0		buss		bu0s
	2		föll		f2l
	U		bott		bUt
	O		håll		hOl
	a		hall		hal
'''
map = {

# prosodi
'"' : 14, # stress
'""' : 14, # jättestress?

# SAMPA generell
'9' : 221, #
'9:' : (8,221),
'{' : 131,
'{:' : (8,131), #lång e

# Plosiver
'p' : 198,
'b' : 170,
't' : 191,
'd' : 174,
'k' : 194,
'g' : 180,

# Frikativer
'f' : 186,
'v' : 185,
's' : 187,
'S' : 182, # sj Fulhax church feature
'h' : 183,
'C' : 182, # sj Fulhax church feature

# nasals
'm' : 140,
'n' : 141,
'N' : 143,
'r' : 148,
'l' : 145,
'j' : 165,

# vokaler langa
'i:' : 129,
'e:' : 130,
'E:' : 130, # sael
'y:' : 128,
'}:' : 139, # hus
'2:' : 139, # foel
'u:' : 137, # sol
'o:' : 137, # hAl
'A:' : 154, # hal 

# vokaler korta
'I' : 129,
'e' : 131,
'E' : 131, # raett
'Y' : 158,
'u0' : 134,
'2' : 131, # foell
'U' : 135,
'O' : 137, #hAll
'a' : 136,

'rt' : (148,191),
'rs' : (148,187)
}
'''

There are also two pre-r allophones (long and short) of /E/ and /2/ (see below).

The following important allophonic variants occur in Swedish which require separate symbolic representation:

	{:		här		h{:r	pre-r allophone of E:
	9:		för		f9:r		"	2:
	{		herr		h{r		"	E
	9		förr		f9r		"	2

	@		pojken		pOjk@n	schwa vowel allophone

	rt		hjort		jUrt	retroflex consonant, not initial*
	rd		bord		bu:rd		"
	rn		barn		bA:rn		"
	rs		fors		fOrs		"
	rl		karl		kA:rl		"

* in cases where the dental consonants do not change into retroflexes, they are transcribed using the separator sign (ASCII 45): r-t, r-d.

Swedish has two contrasting tonemes, but only in stressed syllables. Tone 1 is indicated by the ordinary stress mark, Tone 2 by a doubled stress mark, e.g.

stress and toneme 1	anden		"and@n		(the duck) 	
stress and toneme 2	anden		""and@n		(the spirit) 	

'''

