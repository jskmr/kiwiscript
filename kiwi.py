

chartoke = {
	"0123456789": 1,
	"_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ": 2,
	"+-*/%=!<>": 3
}

tokens = {
	"+": 1,
	"-": 2,
	"*": 3,
	"/": 4,
	"%": 5,
	"**": 6,
	"//": 7,
	"=": 8,
	"+=": 9,
	"-=": 10,
	"*=": 11,
	"/=": 12,
	"%=": 13,
	"**=": 14,
	"//=": 15,
}

def read(file):
	with open(file, "r") as source:
		source = source.read().split("\n")
		return source

def lex(s): #Convert expression to string of tokens (lex it)
	s = str(s)
	t = 0
	v = None
	tokchars = ""
	r = []
	
	for c in s:
		for key, value in chartoke.iteritems():
			if c in key:
				if t != value:
					v = tokens.get(tokchars)
					if v:
						r.append(v)
					else:
						print "Unknown token: '" + tokchars + "'"
					t = value
				else:
					tokchars += c
			else:
				pass
	
	return r
