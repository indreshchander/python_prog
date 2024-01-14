"""
Class variables are shared between different objects of the class.

If this variable is changed between object
"""

class MyClass:
    # Class variable
    class_variable = 0

    def __init__(self, instance_variable):
        # Instance variable
        self.instance_variable = instance_variable

# Creating instances of MyClass
obj1 = MyClass(10)
obj2 = MyClass(20)

#Changing class variable
MyClass.class_variable = 999

# Accessing class variable through obj
print("Class Variable:", obj1.class_variable)  # Output: Class Variable: 999
print("Class Variable:", obj2.class_variable)  # Output: Class Variable: 999

#Accessing class variable using class name
print("Class Variable accessing through class variable:", MyClass.class_variable)

# Accessing instance variables
print("Instance Variable for obj1:", obj1.instance_variable)  # Output: Instance Variable for obj1: 10
print("Instance Variable for obj2:", obj2.instance_variable)  # Output: Instance Variable for obj2: 20

