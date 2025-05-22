

from callLimit import my_decorator, callLimit

@my_decorator
def test():
	pass

# test()


from callLimit import callLimit

@callLimit(3)
def f():
	print ("f()")


@callLimit(1)
def g():
	print ("g()")


for i in range(3):
	f()
	g()