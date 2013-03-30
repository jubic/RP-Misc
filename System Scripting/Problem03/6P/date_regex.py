import re

# This is more complete and robust regex to check against YYYY/MM/DD - HH:MM:SS format.
# Using re.VERBOSE allows you to put the regex in multiple lines - the spacing in between
# and the comments are ignored.

# Checking on whether Jan has 30 or 31 days is better left to additional code logic before
# the regex gets convoluted and hard to read.

# This is also used in "solution_pro.py" code also.

a = re.compile(r"""20\d{2}/         # year
                   (0\d|1[0-2])/    # month
                   ([0-2]\d|3[01])  # date
                   \s+
                   ([01]\d|2[0-3]): # hour
                   ([0-5]\d):       # minute
                   ([0-5]\d)        # second
               """, re.VERBOSE)

good = ["2010/01/01 01:13:59","2010/12/31 23:59:59","2099/09/30 00:59:59"]
bad  = ["2010/21/01 24:11:11","2010/13/31 23:60:50","2099/00/32 23:59:60"]

def test(l):
    for s in l:
        print s,
        if a.search(s):
            print "GOOD"
        else:
            print "BAD"

test(good)
print "--"
test(bad)
# vim:expandtab:tabstop=4:softtabstop=4:shiftwidth=4
