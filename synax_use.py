#a = sum(i for i in range(1,3))
#print(a)

nest = [[1,2],4,[4,6,7],8]

def flatted(nested):
	try:
		for sub in nested:
			for element in flatted(sub):
				yield element
	except TypeError:
		yield nested

print(list(flatted(nest)))

g = (i * 2 for i in range(10))


print(type(g))#<class 'generator'>
#g.next()  #generator' object has no attribute 'next'

print(next(g))


