import sys

filename = sys.argv[1]
sourceCode = open(filename,'r').read()
lines = sourceCode.split( "\n" )

#M = 0
Ans = 0

for line in lines:

	tokens = line.split( " " )
	firstToken = tokens[0]

	for token in tokens:
		if token == "Ans":
			token = str( Ans )

	if firstToken == "pr":
		print( Ans )
	else:
		value = " ".join( tokens )
		Ans = eval( value )