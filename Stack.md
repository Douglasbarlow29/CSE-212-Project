# **Stacks**
Stacks are a data structure where the items within are organized exactly the way it sounds: They are stacked. This means that the last value added to the stack will be on the top meaning it is the first to be drawn from the stack.

## Push and Pop Operations

Within the data structure of stacks, there are push and pop operations. It is easier understand these operations when you visualize a stack of some sort. You could visualize a stack of bricks, a stack of pancakes, etc. If we look at a stack of pancakes we see that the last one to be put on the stack (meaning it is on top) is the first to be eaten. This is often called "Last In, First Out". Everytime we add something to the stack, this is called a **push** operation. There is a visual below to give you an idea of what this looks like.

![Alternate Text To Display](push.png)

Once something is pushed to the stack, the stack increases. At some point we are able to take a value off of the stack or perform a **pop** operation as visualized below:

![Alternate Text To Display](pop.png)

Now, in python we categorize the top of a stack in a visual as the back of the stack. Meaning that the first value or item added to the stack (the one on the bottom) is considered to be the front, while the latested item to be added is considered the back of the stack.

## Undo option
One of the most commonnly used stacks that is used on the computer utilizes something called the "Undo" option. This basically means that we can type something out and it will be put on the screen and added to a stack. When undo is hit, it will take the last thing that was added and delete it from the stack. For example if you were to type, "I went to the store today." then the stack would look something like this: "I" "went" "to" "the" "store" "today". If we were to hit the undo button, then today would be taken away from the stack and therefore your computer screen too.

![Alternate Text To Display](undo.png)

The stack is very useful because it maintains a history of where things are stored. There is an exact order to each item in the stack. When we hit "undo" what we are really doing is popping an item from the back of a stack that we created. When we type a word we are just pushing an item to that stack.

## How to use Stacks in Python

We already know many of the functions in python that can be used to create and take apart stacks. For instance, we can create a list and use the append function to push something to the back of the list. We can use the pop function in order to delete the last item to be pushed to the list/stack.

### Useful functions:

* Push: **list.append(item)**
* Pop: item = **list.pop()**
* Size of Stack: **len(list)**
* Determining if the Stack is Empty: **if len(list) == 0:**

## Example Code

Below is an example of pushing values into a stack:

```Python
def create_stack(numbers):

    stack = [] #create a list
    for x in numbers: #iterate through the string

        n = int(x) #convert to integers


        if n >= 5: #check to see if integer is greater than 
                   #or equal to five
            stack.append(n) #push integer to list

        else:
            None

    print(stack) #display list/stack


one = "95836754827"

two = "47578398578341212"

three = "111122222333365432"

create_stack(one) #output should be [9, 5, 8, 6, 7, 5, 8, 7]

```
If you were to use "two" or "three" you would get:
* create_stack(two) = [7, 5, 7, 8, 9, 8, 5, 7, 8]
* create_stack(three) = [6, 5]

## Problem

Here is a problem to solve:

```Python
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

```
Below is a solution to check your answer with:

[Text To Display](stacks(1)_solution.py)