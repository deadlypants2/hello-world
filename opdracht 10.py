my_list = [12, 24, 312, 1, 67, 89, 244, 45]
my_list.sort(reverse=True)
print(my_list)
print(my_list[0:4])
del my_list[3:5]
print(my_list)


New_list = []

for getallijst in range (0, 100, 4):
    New_list.append(getallijst)

print(New_list)