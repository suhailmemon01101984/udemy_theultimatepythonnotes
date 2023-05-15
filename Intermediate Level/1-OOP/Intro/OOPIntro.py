#What is OOP ? 

'''
OOP stands for Object-Oriented Programming. 
It's a programming paradigm that emphasizes the use of objects to represent 
and manipulate data. An object is an instance of a class, 
and a class is a blueprint or template for creating objects.
'''

#How to create OOP?

'''
Creating OOP involves defining a class and then creating objects of that class. 
Here are the steps to create OOP:

Define the Class: The first step in creating OOP is to define a class. 
A class is a blueprint or template for creating objects. 
It defines the properties and methods that the objects of that class will have.

Create Objects: The second step is to create objects of that class. 
An object is an instance of a class. 
You can create multiple objects of the same class, 
and each object will have its own properties and methods.

Access Properties and Methods: Once you have created objects of a class, 
you can access their properties and methods using the dot notation.
'''


#Small Example:

# Define a Class
class Dog:
    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Instance Method
    def speak(self, sound):
        return f"{self.name} barks {sound}"

# Create Objects
dog1 = Dog("Buddy", 2)
dog2 = Dog("Molly", 3)

# Access Properties and Methods
print(f"{dog1.name} is a {dog1.species}")
print(dog2.description())
print(dog1.speak("Woof!"))


#Explanation

'''
First, we define a class called Dog. The class has a class attribute species that is shared by all objects of the class.

The class also has an initializer method __init__ that takes two arguments name and age. 
The method initializes two instance attributes name and age with the values passed as arguments.

The class has two instance methods description and speak. 
The description method returns a string that describes the dog's name and age, 
and the speak method takes a sound as an argument and returns a string that includes the dog's name and the sound it makes.

Next, we create two objects of the Dog class: dog1 and dog2.

Finally, we access the properties and methods of the objects using the dot notation. 
We print the name and species of dog1, the description of dog2, and the sound that dog1 makes.
'''