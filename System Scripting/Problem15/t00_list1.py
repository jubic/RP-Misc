"""
h2. Create Lists of Various Types

Create *three* lists, each list with 3 items in it. The first list has _integer_ only items, and the second has _string_ only items. 

And the third list must have *3 lists* in it (each of these _internal_ lists can contain any number of items of any types).
"""

list_of_int = [1, 2, 3]
list_of_string = ['1', '2', '3']
list_of_lists = []
list_of_lists.append(list_of_int)
list_of_lists.append(list_of_string)
list_of_lists.append(list_of_string)
