def stack(numbers):
    
    stack = [] #create stack

    for x in numbers: #iterate through numbers
        if 20 % x == 0: #check to see if the number is a factor of 20
            stack.append(x) #push number to stack
        else:
            None
            
    return stack #display stack

def last_digit(numbers):
    stack = [] #create stack

    for x in numbers: #iterate through numbers
        stack.append(x) #push all numbers to stack in order

        if stack.pop() == 8: #check to see if number on top is 8
            return True
        else:
            return False



list_1 = [9, 5, 4, 2, 5, 7, 3, 1, 8, 5] 
list_2 = [8, 7, 2, 5, 5]
list_3 = [2, 5, 8, 4, 1, 9, 4, 5, 3, 3, 2, 4]

print(stack(list_1))
print(last_digit(list_1))
print(last_digit(list_2))
print(last_digit(list_3))

