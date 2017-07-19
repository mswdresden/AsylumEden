# -*- coding: utf-8 -*-
# msw: every controller should start with this utf-8 line
"""
    Testing Controllers  # msw: a meaningful name (and description)
"""

# web2py accesses functions according to the URL given (the desired page you type in in your browser)
# so application/controller/function (in this case http://127.0.0.1:8000/AsylumEden/mytester/index ) calls the index
# fuction. as index is always the 'default', you can leave it also away (i.e. .../AsylumEden/mytester/ )

# this later, when we use a module/resource
#module = request.controller
#resourcename = request.function

# S3 framework functions
def index():
    # web2py accesses functions according to the URL given (the desired page you type in in your browser)
    # so application/controller/function (in this case http://127.0.0.1:8000/AsylumEden/mytester/index ) calls the index
    # fuction. as index is always the 'default', you can leave it also away (i.e. .../AsylumEden/mytester/ )

    print "Hallo Martin" # print something to stdout (in the shell you run 'python web2py -a pass')
    return dict()        # return an empty dict

# ------------
# access this function via http://127.0.0.1:8000/AsylumEden/mytester/tester1
def tester1():
    print "Hello, you are function 'tester1' located in the controller mytester"
    dict1 = {"key1" : "Hello", "key2" : "World"}
    dict2 = dict(key3="... go", key4="crazy")
    return locals()

# -----------------------------------------------------------------------------
def tester2():

    print "\n creating a dict and looping over it"
    d = dict(k1='value_1', k2="value_2")
    for key in d:
        print "the value is %s" % d[key]

    print "\n looping with counting"
    for i, key in enumerate(d):
        print i, key, d[key]

    print "\n the use of 'break' in a loop"
    for i in [1,2,3,4,5,6]:
        if i > 3:
            break
        else:
            print i

    print "\n the use of 'continue' in a loop"
    for i in [1,2,3,4,5,6]:
        if i%2==0:
            continue
        else:
            print i

    print "\n the use of if ... elif ... else"
    for i in range(3,11,2): # range(from,to,increment)
        print i
        if i == 5:
            print "i is 5!"
        elif i == 7:
            print "i is 7!"
        else:
            print "i is not 5 or 7"

    print "\n Python can throw - pardon, raise - Exceptions:"
    # a list of all exceptions (web2py): http://www.web2py.com/books/default/chapter/29/02/the-python-language
    num = 1
    den = [0,1]
    for den in den:
        print "denominator is %d" % den
        try:
            value = num/den
        except Exception, e:
            print "uups: %s " % e
        else:
            print "no problem here, value is %(value)f" % dict(value=value)
        finally:
            print "done"

    print "\n 'print'ing things ..."
    print "con ..." + "catenate"
    print "integer value: %i" % 1.23
    print "float value: %f" % 1.23
    print "string value: %s" % 1.23

    print "\n "

    #print "\n "

    # return some dict
    return d

# using functions
def function_test():
    # this function just defines a sub-scope for our testing.
    print "\n using functions"
    print "\n some words on 'scope'"
    def f1(x):
        y = 1 # this y is local to the function
        print "inside f1 y is %d" % y
        return x*y

    def f2(x):
        #y = 1 # y is defined in an outer scope (note: in python this does not have to be prior to function definition
        # (as in C++) - the 'y=2' is written below this fuction definition)
        print "inside f2 y is %d" % y
        return x*y

    x=10
    y=2

    print "f1(%d) = %d" % (x, f1(x))
    print "f2(%d) = %d" % (x, f2(x))

    ###
    print "\n defining 'closures'"
    def f(x):
        def g(y): # a function is defined in f ...
            return x*y
        return g # ... and a function is returned
    doubler = f(2)
    tripler = f(3)

    print "doubling 2 = %d" % doubler(2)
    print "tripling 2 = %d" % tripler(2)


    ###
    print "\n functions can have default values and return multiple values"
    # however, as in C++: once you have a default value, all parameters after that must also have default
    def func(a,b=2,c=30):
        return a,b,c

    a,b,c = func(1,3)
    print a, b, c

    # the order only matters, if you do not specify the parameters explicitly
    a, b, c = func(c=999, a=-8, b=3)
    print a, b, c

    return dict()

print "\n variable_test"
def variable_test():
    def foo():
        print "'a' within a function defined above and called after definition(s):  %d" % a
    #foo() # does not work!
    a = 10
    a = 20
    a = 30
    foo()
    print "a below definition(s) %d" % a

print "\n Functions can take runtime-variable number of arguments"
def runtime_argtest():
    def foo(*a, **b): # '*': list of single things; '**' dict-like things
        return a, b

    a , b = foo(1, "hallo", True, 555  ,   c="Truck", d=5) # entry like ',"hugo" : "boss",' does NOT work
    print "'a' (single things):" , a
    print "'b' (dict like things):", b

    return dict()

###
print "\n functions with many arguments can get them via list or tuple"
def listtuple_test():
    def foo(a,b):
        return a+b

    li = [1,2]
    tu = (3,4)

    print "list test : adding", li, "results in " , foo(*li)
    print "tuple test: adding", tu, "results in " , foo(*tu)


print "\n map and lambda:"
def mapNlambda_test():

    # lambda ist a short way to define functions
    def func_foo(b):
        return b+1

    lambda_foo = lambda x : x+1

    print "func_foo(1)  :", func_foo(1)
    print "lambda_foo(1):", lambda_foo(1)

    # lambda can be convenient, e.g. when a function is quickly needed:
    arr = [1,2,3,4,5,6,7]
    arr1 = map(func_foo, arr)
    arr2 = map(lambda x : x+1, arr)

    print "arr1", arr1
    print "arr2", arr2

    return dict()

# =============================================================================
