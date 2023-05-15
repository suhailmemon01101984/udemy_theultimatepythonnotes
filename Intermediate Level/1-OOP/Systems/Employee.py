#Example 2: Employee


'''
This example demonstrates how to create an 
Employee class that stores information about an employee.

'''

class Employee:
    """
    A class representing an employee.
    """
    
    def __init__(self, name, id_number, title):
        """
        Initializes a new employee object.
        """
        self.name = name
        self.id_number = id_number
        self.title = title
    
    def get_name(self):
        """
        Returns the name of the employee.
        """
        return self.name
    
    def get_id_number(self):
        """
        Returns the ID number of the employee.
        """
        return self.id_number
    
    def get_title(self):
        """
        Returns the title of the employee.
        """
        return self.title
    
    def __str__(self):
        """
        Returns a string representation of the employee.
        """
        return f"{self.name} ({self.id_number}): {self.title}"


'''
we define an Employee class that has three methods:
 __init__, get_name, and get_title. The __init__ method is a constructor 
 that initializes a new Employee object with a name, an ID number, 
 and a title. The get_name and get_title methods return the name and 
 title of the employee, respectively. 
 The get_id_number method returns the ID number of the employee. 
 The __str__ method returns a string representation of the employee, 
 which is used when the object is printed.

'''

# Create a new employee
employee = Employee("John Smith", "1234", "Manager")

# Print the employee details
print(employee)


'''
we create a new Employee object with a name of "John Smith", 
an ID number of "1234", and a title of "Manager". 
We print the employee details using the __str__ method, 
which returns a string representation of the employee.
'''
