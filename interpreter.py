Ans = 0
#M = 0

while True:
	line = input( ">> " )

	if line == "exit":
		break

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