The following example illustrates the usage of the standard data streams:
>>> import sys
>>> print "Going via stdout"
Going via stdout
>>> sys.stdout.write("Another way to do it!\n")
Another way to do it!
>>> x = input("read value via stdin: ")
read value via stdin: 42
>>> print x
42
>>> print "type in value: ", ; sys.stdin.readline()[:-1]
type in value: 42

'42'
>>> 