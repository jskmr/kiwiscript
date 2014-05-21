

chartoke = {
	"0123456789": 1,
	"_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": 2,
	"+-*/%=!<>": 3
}

tokens = {
	"+": 1
	
	
}

def read(file):
	with open(file, "r") as source:
		source = source.read().split("\n")
		return source

def lex(s): #Convert expression to string of tokens (lex it)
	s = str(s)
	type = 0
	tokchars = ""
	
	for c in s:
		for key, value in chartoke.iteritems():
			if c in key:
				if type != value:
					pass
				else:
					tokchars += c
			else:
				raise Exception("Invalid character!")
