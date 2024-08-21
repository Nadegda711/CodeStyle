my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_ = 0
while index_ < len(my_list):
    element = my_list[index_]
    if element < 0:
        break
    elif element > 0:
        print(element)
    index_ += 1