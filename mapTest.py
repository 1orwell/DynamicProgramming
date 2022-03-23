twod_list = [[4,5,6,7,8], [6,5,3], [4,5,1,2]]
simple_list = [4,5,6,7,8]
print(twod_list)
new_map = map(lambda x: x.append(10), twod_list)
simple_new_map = map(lambda x: x+1, simple_list)
new_list = list(new_map)
simple_new_list = list(simple_new_map)

for val in new_list:
    print(val)

for val in simple_new_list:
    print(val)

my_list = [1,3,4,5,6]

my_list.insert(0, 10)
print(my_list)

