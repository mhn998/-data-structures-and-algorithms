# Data Structures and Algorithms

See [setup instructions](https://codefellows.github.io/setup-guide/code-301/3-code-challenges), in the Code 301 Setup Guide.

## Repository Quick Tour and Usage

### 301 Code Challenges

Description | Link
---------|--------
Code-Challenge01 |[forEach](./code-challenges/challenges-01.test.js)
Code-Challenge02 |[Call by Reference,Value](./code-challenges/challenges-02.test.js)
Code-Challenge03 |[Sort](./code-challenges/challenges-03.test.js)
Code-Challenge04 |[Regex1](./code-challenges/challenges-04.test.js)
Code-Challenge05 |[Splice , Slice , Join , Split](./code-challenges/challenges-05.test.js)
Code-Challenge06 |[Object.keys,values,entries ](./code-challenges/challenges-06.test.js)
Code-Challenge07 |[Map](./code-challenges/challenges-07.test.js)
Code-Challenge08 |[Filter](./code-challenges/challenges-08.test.js)
Code-Challenge09 |[Reduce](./code-challenges/challenges-09.test.js)
Code-Challenge10 |[Chaining Methods](./code-challenges/challenges-10.test.js)
Code-Challenge11 |[Regex2](./code-challenges/challenges-11.test.js)
Code-Challenge12 |[Two-Dimensional Arrays](./code-challenges/challenges-12.test.js)
Code-Challenge13 |[Includes , every , substring , charAt](./code-challenges/challenges-13.test.js)




### 401 Data Structures, Code Challenges

- Please follow the instructions specific to your 401 language, which can be found in the directory below, matching your course.


Description | Link
---------|--------
Code-Challenge01 |[Reverse-Array](./python/code_challenges/array_reverse/array_reverse.py)
Code-Challenge01 |[Shift-Array](./python/code_challenges/array_shift/array_shift.py)









---------------------------
# Reverse an Array

## Challenge Summary
a function that reverse an array without using built-in method such as reverse()

## Approach & Efficiency
I took advantage of len() multiple times, for , while , append , insert.

## Solution
![ReverseArray1](./python/assets/array-reverse1.jpg)
![ReverseArray2](./python/assets/array-reverse2.jpg)



-----------------------

# Array Shift

## Challenge Summary
Manipulate the array by specifically adding values to its middle

## Challenge Description
a function that takes an array of numbers and a value as an arguments , add that value to the middle of the array

## Approach & Efficiency
two approaches ,one depending on the length of the array if it's even or odd(longer solution) . second one that takes advantage of the ceiling of the half and slice the array into two parts between the value which sets in the middle.

## Solution
![Array-shift picture1](./python/assets/array_shift1.jpg)
![Array-shift picture2](python/assets/array_shift2.jpg)


# Binary Search

## Challenge Summary
find the index of a value in a sorted array without using built in methods

## Challenge Description
a function that takes an array of numbers and a value as an arguments , find the index of that value in the array by calculating mid , figure out if the value equals, higher , less than the mid and go towards it , each time the mid is calculated the array is halved , and if the mid doesn't equal half if array add or subtract 1, keep iterating all they way  till finds it and returns it, else then the mid becomes 0 and return -1.

## Approach & Efficiency
described above.
Efficiency : Checked with any other types than numbers , take all types of numbers , tested for each case (Happy path , expected failure , edge cases)

## Solution
![ReverseArray2](python/assets/array-binary-search.png)


# Linked list

# Challenge Summary
Define a linked list class with two methods insert and includes.

## Whiteboard Process
N/A

## Approach & Efficiency
if else statement for the insert where if contains while loop , regarding includes it's an if statement inside a while loop.



# Linked list insertion

# Challenge Summary
add new methods that insert nodes in different places in the linkedlist , append which is opposite of insert , insert after and insert before.

## Whiteboard Process
N/A

## Approach & Efficiency
insert before and insert have nearly the same concept of algorithm ,  which is loop over the linkedlist to search for that certain node then change the .next value for both the new node and the current node for inserting before or after , for inserting at the end it will loop over the end of the linkedlist then insert the node and change the .next for the current node.


# Linked list find a value from the end

# Challenge Summary
a function that finds a value from a linked list which start the index counting from the last node to the first

## Whiteboard Process
N/A

## Approach & Efficiency
convertig to normal list through looping over the linkedlist by assigning its values to a variable.



# Linked list zip

## Challenge Summary
Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

## Challenge Description
we should Chain two linkedlist by taking 1 value from each and link them together without creating new linkedlist

## Approach & Efficiency
looping till both ll hit none and appending item (described in details in white-board)
space -> O(1)
time -> O(2n)

## Solution
![Zip two linkedlists](python/assets/ll_zip.png)

# Stack and Queues

## Challenge Summary
Create stack and queue with all its essential methods

## Approach & Efficiency
create a Node class that creates the node , then create a class for Stack with a top of None when instantiating , adds push , pop , isEmpty , peek and other methods to it , and the same for queue.

## Whiteboard process
N/A



# Stack with queues

## Challenge Summary
Create a queue that consists of two stacks

## Approach & Efficiency
Create a PseudoQueue class.this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects.

enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.
dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Whiteboard process
N/A

# Animal Shelter
Create a class called AnimalShelter which contains only dogs and cats. The shelter operates using a first-in, first-out approach. And Data can be recognized if a Dog or Cat

## Challenge Description
Implement the following methods:
- enqueue(animal): adds animal to the shelter.
- animal can be either a dog or a cat object.
- dequeue(pref): returns either a dog or a cat.
- If pref is not "dog" or "cat" then return null.

## Approach & Efficiency
enqueue(animal) is just a normal enqueue that appends to the Queue , dequeue(pref) it will check for front if not none it will loop on current.next until it finds it

## Solution
- Problem domain : Create a class called AnimalShelter which contains only dogs and cats. The shelter operates using a first-in, first-out approach. And Data can be recognized if a Dog or Cat

- Algorithim for dequeue
1. check kind if none , if yes return the front
2. if not none assign the front to a variable
3. check front if it's equal to the value
4. if not , check the next
5. if not , assign current to next and check next
6. when equals save to a variable
7. assign the next for the current to the next after it
8. return variable

- pseudo code : n/a

- Big O
time: O(n)
space : O(1)

# Multi-bracket Validation

## Challenge Description
a function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Approach & Efficiency
create your normal stack, then use your function to loop over the string and predict closing or opening and make decision based on it.

## Solution
![Multi bracket validation whiteboard](python/assets/multi-bracket.png)

# Trees

## Challenge Description
- Create a BinaryTree class, define a method for each: preOrder , inOrder , postOrder
- Create a BinarySearchTree class, define a method named add that adds a new node with value to tree. Define a method named contains that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once.

# Approach & Efficiency
- uses recursion in BinaryTree with big O(2^n)
- uses recursion in BinarySearchTree with big O(2^n)

#  Whiteboard process
n/a

# API
- preOrder,inOrder and postOrder:
1. create an empty array
2. It loops over the tree by going to the root
3. append if preorder goes to the left node if existed and use recursion
4. append if inorder then go to right if existed and uses recursion
5. append if postorder

- Add and contains
Add :
1. assigns root if it does not exist, else assigns current as root
2. check if it is equal and do comparison with the current and add to it if doesn't exist, else will navigate to the left or right

Contains: Same as Add

# Find Maximum Value in Binary Tree

## Challenge Description
Find the Maximum Value in a Binary Tree without using built ins methods.

## Approach & Efficiency
define a max attribute that is equal to the root ,  then iterate over the tree while comparing

Big O of time --> O(2^n) Big O of space --> O(1)

## API
1. define a max attribute that is equal to the root
2. use preOrder methods to iterate over tree Nodes values
3. compare with the value saved in max then replace it if it is bigger
4. after the recursion ends we will have the maximum value in the tree
5. return it
