f = open("/tmp/cwrite", "w")
f.write("one\n")
f.close()

f = open("/tmp/cwrite", "w+")
f.write("two\n")
f.close()

f = open("/tmp/cread", "w")
f.write("one\n")
f.close()

f = open("/tmp/cread", "r+")
f.write("two\n")
f.close()

import os
os.unlink("/tmp/cappend")

f = open("/tmp/cappend", "a")
f.write("one\n")
f.close()

f = open("/tmp/cappend", "a")
f.write("two\n")
f.close()

f = open("/tmp/cappend", "a+")
f.write("three\n")
f.close()

print "WRITE TEST"
print open("/tmp/cwrite").read()
print

print "READ TEST"
print open("/tmp/cread").read()
print

print "APPEND TEST"
print open("/tmp/cappend").read()
print
