def sparse_list(num_1, num_2):

    list_1 = set()
    num_3 = num_1 + num_2
    for n in num_3:

       
        list_1.add(n)



    return list_1

num_1 = [1, 3, 2, 6, 2, 9, 5, 6, 8, 3, 6, 0, 8]
num_2 = [3, 6, 10, 15, 20, 12, 15, 4, 6, 8]

print(sparse_list(num_1, num_2))