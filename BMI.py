from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_category(self):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        category = self.get_category()
        print(f"Name: {self.name}, Age: {self.age}, BMI:{bmi.}, Category: {category}")
              
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_category(self):
        bmi = self.calculate_bmi()
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal weight"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"
        
class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3
    
    def get_category(self):
        bmi = self.calculate_bmi()
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"
        
class BMIApp:
    def __init__
        

    
               
             
