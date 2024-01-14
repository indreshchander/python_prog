In variables class variable and static variables are same. 

Class methods and Static methods are different.


In Python, methods in a class can be categorized into three main types:

1. Instance Methods:

These are the most common type of methods.
They operate on an instance of the class and have access to instance attributes.
The first parameter is typically named self and represents the instance on which the method is called.


Example:

class MyClass:
    def instance_method(self):
        print("This is an instance method")

obj = MyClass()
obj.instance_method()


2. Class Methods:

These methods are bound to the class rather than the instance.
They are defined using the @classmethod decorator.
The first parameter is typically named cls and represents the class itself.
Class methods can be called on the class rather than an instance.

Example:

class MyClass:
    class_variable = 0

    @classmethod
    def class_method(cls):
        print(f"This is a class method. Class variable: {cls.class_variable}")

MyClass.class_method()


3. Static Methods:

These methods are not bound to the instance or the class.
They are defined using the @staticmethod decorator.
They don't have access to self or cls and don't modify class or instance state.
They are more like regular functions but are defined within the class for organization.

Example:

class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.static_method()


Understanding and using these types of methods allows you to structure your code effectively and choose the appropriate method type based on the intended behavior and the data it needs to operate on.
