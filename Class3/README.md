## Class for Week 3 of Python
Here is code notebook for class 3. You can practice it.
## Assignment
Your first assignment is to write code for list operations

### 1. Indexing
Write code for retriving values from list by indexing and `print` a statement message for given lists
```
# Example 1
employee_data = ['Ali', 125000, 'Google', 5]
output: 'Ali is working in Google for 5 years and his salary is 125000'

# Example 2
studentData = ['Ahmed', 'Bilal', 'Government College University', 'Computer Science', 'BS', 50000,
				'28 Januray 2020', '05 February 2020']
output:
'Hello Ahmed Bilal,
Your application is accepted for admission in "BS Computer Science" in Government College University.
You have to submit fee 50000 before 28 January 2020.
Your classes will start from 05 February 2020.
Thanks'
```
**hint**: Use `list indexing` and `string format` methods


### 2. Slicing
```
You have a list of cities given as follows. Use positive and negative slicing methods to print out following outputs:
cities = ["Faisalabad", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sahiwal", "Rawalpindi", "Sialkot"]

Outputs:
(For positive slicing)
1. ["Faisalabad", "Lahore", "Islamabad", "Peshawar"]
2. ["Islamabad", "Peshawar", "Quetta", "Sahiwal"]
3. ["Sahiwal", "Rawalpindi", "Sialkot"]

(For negative slicing)
1. ['Quetta', 'Sahiwal', 'Rawalpindi']
2. ['Peshawar', 'Quetta', 'Sahiwal', 'Rawalpindi', 'Sialkot']
```

### 3. Update Lists
You have a list of student information. You need to update it for following statements
```
studentData = ["Ali Raza", 22, 91.24, "Computer Science", 5, "University of Agriculture"]
```
Add values to this list using `append`
```
1. '20 February 2019'
2. 8
```
Use `insert` method to insert at specific index
```
1. 25000 at index 4
2. 'M. Iqbal' at index 1
```

Update list using list update method:
```
1. Change Name from 'Ali Raza' to 'Zohaib Ali'
2. Change No of subjects from 5 to 7
```
Remove values from list using `remove` method
```
1. 'Computer Science'
2. 91.24
```
Remove using `pop` method
```
1. Last value from list
2. value at 3rd index
```

### 4. Multidimensional list tasks
You have given data of an employee
```python
employeeData = [["Ali", 35000, "Software Engineer"],
				["Talha", 55000, "Product Manager"],
				["Nasir", 79000, "Computer Engineer"],
				["Khalid", 44000, "DBA"]]
```
#### For Loop
**Tasks**
```
1. Print name of employees with salaray greater than 50000.
2. Calculate total salary of all employees.
```
#### List update tasks
```
1. Change salary of nasir from 79000 to 90000 and designation to "Product Manager"
2. Change salary of Khalid to 50000
```
### 5. Login User
You have given some users data. You have to write a script to check if username and password are correct. If `username` and `password` are correct. Then you have to check if email is verified or not. If it is verified then print `Login Succeed` else print `Email not verified`. If username or password are incorrect you have to print `Incorrect Login details`
```python
# Data 1
username = "faizan1214"
password = "qwerty"
emailVerified = False

# Data 2
username = "faizan1214"
password = "qwerty"
emailVerified = True
```
