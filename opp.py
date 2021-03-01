class HumanBeings():
    # Initialization of class
    def __init__(self, name, color, height, weight, age):
        self.name = name
        self.color = color
        self.height = height
        self.weight = weight
        self.age = age
        self.bmi = 0
        

    # Creating Methods - these are functions that are related

    def get_result(self):
        return f'{self.name} is of {self.color} - color,{self.height} - height, {self.age} - age'

    def calculate_bmi(self):
        height_meters = self.height/100
        #bmi = self.weight/(height_meters*height_meters)
        #return bmi
        self.bmi = self.weight/(height_meters*height_meters)
        return self.bmi

    # Give the user advice based on the bmi output
    def bmi_advice(self):
        #print(self.bmi)
        if self.bmi<18.5:
            return f'Your BMI of {self.bmi} shows you are in the underweight range'
        elif self.bmi>=18.5 and self.bmi<=24.9:
            return f'Your BMI of {self.bmi} shows you are in the healthy weight range'
        elif self.bmi>=25.0 and self.bmi<=29.9:
            return f'Your BMI of {self.bmi} shows you are in the overweight range'
        elif self.bmi>=30.0 and self.bmi<=39.9:
            return f'Your BMI of {self.bmi} shows you are in the obese range'
        else: 
            return f'Your BMI of {self.bmi} is invalid'
# Instantiation
person1 = HumanBeings(name="Tech", color="Black", height=170, weight=70, age=28)

result1 = person1.get_result()
result1bmi = person1.calculate_bmi()
result1bmi_advice = person1.bmi_advice()
print(result1)
print(result1bmi)
print(result1bmi_advice)

# Inheritance
# Start with Parent Class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        return f'{self.name} is {self.age} years old'

# Create the Child Class
class Employees(Person):
    def __init__(self, name, age, department):
         Person.__init__(self, name, age)
         self.department = department

    def in_department(self):
        return f'{self.name} is in {self.department} department'    

employee1 = Employees('Ken', 45, 'Manufacturing')
print(employee1.output())
print(employee1.in_department())

p1 = Person('Ken', 48,)
print(p1.output())

