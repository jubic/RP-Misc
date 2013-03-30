import re
phone_good = "91234567"
phone_bad  = "9a234567"
#
result = re.search("(6|9)[0-9]{7}", phone_good)
print result    # prints something like: <_sre.SRE_Match object at 0x2a8db0>
#
result = re.search("(6|9)[0-9]{7}", phone_bad)
print result    # prints None (not match/found)