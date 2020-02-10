# Class 5 Classwork for functions.
Here is classwork assignment for class 5. Here is list of topics for this class.
### Submit of this url:

https://forms.gle/ns4WCen3MS9KnE8n7


#### Topics
##### 1. Functions
* Introduction to functions
* Passing Information to functions
* Passing information to function using keyword arguments
* Assigning default value to parameter
* Mixing positional and keyword arguments
* Dealing with unknown no of arguments
* Passing information back from function
* Using functions as variables
* Local vs Global variables
* Function within functions
##### 2. While Loop
* Introduction
* While loop with string comparison
* Using break keyword
* Infinite loop
---
### Assignments:
Here is your assignment tasks.
#### 1. Calculate area of circle.
You have given radius of circle. You need to write a function `calcArea` to calculate its area. Where `pi=3.14`. You have to access following test cases.
> Set `pi` as default argument
```python
r = 8.7
r = 9.2
r = 16.03
```
#### 2. Write function to check if a value exists in a list
You have to create a function `checkVal` that accepts a list and finds a number in that list. You will not use built-in function.
**hint:**
> Use loop (while/for)
> Use comparision operator

You have this data given
```python
data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]

# Value to find
"python"
"html"
"c"
```
#### 3. Write a function to shift list item to right n times
You have given a data list. You have to write a function `shiftItems` which accepts 2 parameters `ListName` and `n`(No of times to shift)
```python
data = ["python", "r", "java", "pascal", "c", "javascript", "assembley", "html", "c++"]
```
If we want to shift its values 3 times to right, so output will be like
```
data = ["assembley", "html", "c++", "python", "r", "java", "pascal", "c", "javascript"]
```
If we shift it 1 time out will be
```python
data = ["c++", "python", "r", "java", "pascal", "c", "javascript", "assembley", "html"]
```
Your task is to write a function for this to shift items.
#### 4. Use while loop to get data
You have to write a while loop to get input from user for `radius of circle`.
If user enters `quit`, break the loop, otherwise call `calcArea` function to get area of cricle from radius and print `area of circle`.
#### 5. Function with `**kwargs`:
Write function `showDetails` that takes five positional arguments and receives as dictionary with `**kwargs` and print in formatted way.
Input data is as follows.
```python
name = "Ali", class = "AI", marks = {"math" : 50, "physics" : 80, "biology" : 90, "computer" : 67}, date = "1 Feb 2020", nextClass = True
```
Now write a function
```python
def showDetails(**kwargs):
    # Your code here
```
Output should be as follows
```
Hello Ali
Here is your result for class of AI.
Your score card is as follows.
ClassMarks:
    math : 50
    physics : 80
    biology : 90
    computer : 67
Total marks are: 287
Percentage is as follows: 71.75%
Maximum marks are in "Biology"
Minimum marks are in "Math"
You are promoted to next class.
```
Note
> Use functions and methods to solve total marks and percentage.
