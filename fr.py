#! /usr/bin/env python

fr = 0.6269
br = (24+23.5+22+20+19+17+16+15+15+14+15+15+15*4+8*16+5*17.5+15+14+12.5+10*3+5*9+5*10+3*12)/48/1000
print br
for i in range(50):
	fr = (fr+br*fr*0.75/2.06) / \
	(1+br*fr)
	print fr

#0,537634409
