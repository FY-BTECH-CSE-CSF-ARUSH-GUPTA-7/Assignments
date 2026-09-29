my_list = [10, 20, 30, 40, 50]

my_list.extend([60, 70])     # add many items at end
print(my_list)
my_list.insert(1, 15)        # insert 15 at index 1
print(my_list)
my_list.pop()                # remove last item
print(my_list)
my_list.append(80)           # add one item at end
print(my_list)
my_list.sort()               # sort in ascending order
print(my_list)
print(my_list.pop())
my_tuple = (1, 2, 3, 2, 4, 2)

my_tuple.count(2)            # 3 (how many times 2 appears)
len(my_tuple)                # 6 (number of items)
my_tuple.index(3)            # 2 (position of first 3)
max(my_tuple)                # 4 (largest item)

my_dict = {"name": "Kishan", "age": 18, "city": "Pune"}

my_dict.update({"course": "FY"})   # add or update a key-value pair
my_dict.pop("city")                # remove key "city"
my_dict.get("name")                # 'Kishan' (safe access)
my_dict.items()                    # all (key, value) pairs
