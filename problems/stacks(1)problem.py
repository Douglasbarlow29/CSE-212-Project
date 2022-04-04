'''
For this first function you must create a stack from the list
given that will only have factors of 20 in it. This means that
it will only add numbers that divide perfectly into 20 to the
stack from the list given.
'''

def factors_of_20(numbers):
    stack = []



'''
For the last_digit function you must return True or False based on the back of the stack being equal to 8. If you pop a value from the back and it is equal to 8 then return True, if not return False.
'''
def last_digit(numbers):
    stack = []

    



list_1 = [9, 5, 4, 2, 5, 7, 3, 1, 8, 5] 
list_2 = [8, 7, 2, 5, 5]
list_3 = [2, 5, 8, 4, 1, 9, 4, 5, 3, 3, 2, 4]

print(factors_of_20(list_1)) #Output: [5, 4, 2, 5, 1, 5]
print(last_digit(list_1)) #Output: False
print(last_digit(list_2)) #Output: True
print(last_digit(list_3)) #Output: False