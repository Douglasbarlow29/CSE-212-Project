def list_of_numbers(numbers):
    
    sparse_list = set()

    for n in numbers:

        sparse_list.add(n)
    
    return sparse_list
    

num = [0, 1, 7, 3, 9, 6]
print(list_of_numbers(num))