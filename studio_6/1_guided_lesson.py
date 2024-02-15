# For this portion, we will work together. 
# Please follow along with the teacher. Please do not to work ahead.


# Let's say we want to have some student records in our program
student_1_id = 18584831
student_1_first_name = "Daniel"
student_1_last_name = "White"
student_1_major = "Computer Science"
student_1_expected_graduation_year = "2026"

student_2_id = 18582185
student_2_first_name = "Jennie"
student_2_last_name = "Kim"
student_2_major = "Chemistry"
student_2_expected_graduation_year = "2025"

# TODO: Create a new student student_3 following the same format

student_3_id = 18584321
student_3_first_name = "Smelly"
student_3_last_name = "Sandra"
student_3_major = "Smellology"
student_3_expected_graduation_year = "2027"



# Discussion: What are some problems with this approach?

# Very long variable names, typos?, too many variables for each student





# OOP Property - Encapsulation: Let's contain all of this data into a single Student class


# Basic structure of a class
class Student:
    # TODO: Let's build this class!
    def __init__(self, id, first_name, last_name, major, grad_year):
        self.__id = id
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.grad_year = grad_year

    @property
    def id(self):
        return self.__id
    
    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def get_last_four(self):
        string_id = str(self.id)
        return string_id[-4:]
    
    def print_degree_title(self):
        return "Bachelor of " + self.major

# TODO: Let's recreate our 3 students as objects of our new class!


student_1 = Student(18584831, "Daniel", "White", "Computer Science", "2026")
student_2 = Student(18582185, "Jennie", "Kim", "Chemistry", "2025")
student_3 = Student(18584321, "Smelly", "Sandra", "Smellology", "2027")


# OOP Property Abstraction: The idea of making certain data private
# This prevents other functions/parts of the code from accessing or modifying a value.
    
# TODO: Make the id private.
# Test your code and ensure you cannot access student_1.__id (you should see an error)
    



# This is good because it prevents users from modifying the id by accident.
# However, what if they need to see the id?
    
# TODO: Add an @property getter for id
# Test to make sure you can get the id with student_1.id
    
print(student_3.id)
print(student_3.get_full_name())

# What if we want a way to just get the last four of the id instead of the whole thing? We can build a custom class method to do this.
    
# Create a method in the class called get_last_four
# This should return the last four numbers of the id.
    
print(student_3.get_last_four())

# OOP Property - Inheritence:
# A class can inherit from another class.
# The inheriting class is known as a child class
# The class inherited from is known as the parent class
    
# TODO: Create a child class called GradStudent which inherits from the Student class, with the additional property of "specialization"

class GradStudent(Student):
    def __init__(self, id, first_name, last_name, major, grad_year, specialization):
        super().__init__(id, first_name, last_name, major, grad_year)
        self.specialization = specialization

    def print_degree_title(self):
        return "Master of " + self.major + " with a specialization in " + self.specialization

# create a new student_4 which uses GradStudent instead.
# this person's major is Computer Science and their Specialization is Artifical Intelligence
    
student_4 = GradStudent(12345678, "Klunk", "Rock", "Computer Science", "2027", "Artificial Intelligence")

# OOP Property - Polymorphism
# refers to methods/functions/operators with the same name that can be executed on many objects or classes.
    
# for example, maybe we want a method called print_degree_title, which will print "Bachelor of {major}".
# TODO: add the print_degree_title method to the Student class
    
print(student_3.print_degree_title())

# What happens if we run student_4.print_degree_title?
# Yes, it will print "Bachelor of Computer Science".
    
# This is not what we want though, because it should print Master of Computer Science for our graduate school student. 
    
# We can override our parent method in the child class by creating a function with the exact same name: print_degree_title
    
# TODO: Add the print_degree_title to the Graduate class, have it print "Master of {major} with a specialization in {specialization}."
    
print(student_4.print_degree_title())

# Test your code and make sure print_degree_title prints the master's student as intended.
    
# This is the end of the OOP lesson. Look at part_2.py for the follow up to this lesson. 
    


