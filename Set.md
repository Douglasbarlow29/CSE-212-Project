# **Set**

A set is basically a list of values in no particular order. A set is similar to a stack in the set that it is a list of values, but different because in a stack there is a certain order to each value (the last in is the first out) but in a set there is not. A set is also not able to be duplicated when a stack is. This makes a set more efficient because it is able to use something called **Hashing** in order to achieve O(1) time.

## Hashing

Hashing is a way of assigning each piece of data an integer value in order for it to be easily accessible and unable to duplicate. An example of this would be if you were to have a list of numbers 0-9 and you wanted to achieve O(1) time when adding, removing, and checking on this list. What you would do is assign each number a specific index and then you could call on that number at any moment with the code: index(n) = n. Below is a visual representation of what this would look like.

![Alternate Text to Display](hashing_1.png)

Something interesting about the list above is that it is not guaranteed to be completely filled up. There can be gaps in it. This is called a sparse list. This sparse list is also known as a set. Before we talked about how sets could not be duplicated. If you look at the visual above you will see that there is only one place for each specific value. This means that no duplicates can be made because there would be no where to put them.

### Bigger Sets

An issue that can be faced with larger groups of numbers is that in order to achieve the preferred O(1) performance you would need to make a list as big as the numbers go. For numbers 0 - 1,000,000 you would need a list the size of one million. If you only wanted to store a few values out of that many numbers than it would be an immense amount of overkill to make a sparse list that big. Something that could be done is using the code: index(n) = n % 10 which would see if the number is divisible by ten and leave it's remainder. Below is an example:

![Alternate Text to Display](hashing_2.jpg)

When given the numbers (1, 2, 3, 4, 5, 26, and 17) you don't need a list the size of 26 to put them in a list with an integer value to represent them. All you need to do is use the code: index(n) = n % 10 (or in this case hashFunction(k) = k % 10). This puts each value in a specific location so as to achieve O(1) performance while minimizing the size of the list.

### Hashing Function

A very useful tool in hashing is called the **Hashing Function**. It is used to convert non-integers to integers so that you can use things like the % modulo in order to achieve your ideal sets.

## Open Addressing

Open Addressing is one way we can deal with issues in a sparse list. When we use the index(n) = n function and find that there is already a value in that specific location then the idea behind open addressing is to move it to another available spot, prefereably one to the right. The problem with this method is that if you have too many occupied spots, you may end up moving the original value very far away. Then when another value comes along to take it's spot, the original value will be there. This can basically cause a chain reacition of more and more values being put in locations that don't actually coincide with their original value.

## Chaining

The other option for dealing with issues in sparse lists is called Chaining. Chaining is when instead of finding a new location for your value like open addressing, you simply add that value to the same location, creating a list of values in one space.

## Making Sure We Achieve O(1) Perfmormance

The problem with using these methods of solving issues in Sets is that it can take us away from O(1) performance and start heading towards 0(n) performance. This completely defeats the purpose of sets. So, if chaining and open addressing start becoming more and more often to the point of approaching 0(n) performance, then we need to increase the size of our sparse list in order to compensate.

## Example

Below is a quick example of adding numbers to a set.

```Python 
def list_of_numbers(numbers):
    
    sparse_list = set() #create set

    for n in numbers: #iterate through numbers

        sparse_list.add(n) #use add() function to put them in specific locations
    
    return sparse_list
    

num = [0, 1, 7, 3, 9, 6]
print(list_of_numbers(num))

```
This is a simple example of how to add numbers to a set

## Problem

```Python
'''
In this section you will need to solve a problem involving sets. Take the two lists of numbers given and combine them into a set without repeating any numbers
'''
def sparse_list(num_1, num_2):




num_1 = [1, 3, 2, 6, 2, 9, 5, 6, 8, 3, 6, 0, 8]
num_2 = [3, 6, 10, 15, 20, 12, 15, 4, 6, 8]

print(sparse_list(num_1, num_2)) #The output should be {0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 20}
```
Below is a solution to check your answer with

[Text To Display](sets(1)solution.py)