# our_list = [1, 2, 3, 4, 5, 6, 7]

# print(our_list)

# new_list = ['A', 'B', 'C', 1,2,3,4, True, False]
# print(new_list)

# new_list3 = new_list[-3]
# print(new_list3)


# between_list = new_list[3 : 6:]
# print(between_list)

# end_list = new_list[6::]
# print(end_list)

our_list = [1, 2, [3,4,5], [6,7]]
begin_list = our_list[1]
print(begin_list)

middle_list = our_list[2]
print(middle_list)

end_list = our_list[3]
print(end_list)

nest1 = our_list[2][0]
print(nest1)

nest2 = our_list[3][1]
print(nest2)

print(our_list)
our_list.append("new item")
print(our_list)
our_list.pop(1)
our_list.pop(2)
print(our_list)