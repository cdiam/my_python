class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)


class Child(Parent):
    def __init__(self,last_name, eye_color, number_of_toys):
        print("Child Contrustror Called")
        Parent.__init__(self, last_name, eye_color) 
        self.number_of_toys = number_of_toys


    def show_info(self):
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)
        print("Number of toys - " + str(self.number_of_toys))

billy_cirys = Parent("Curys","blue")
#print(billy_cirys.last_name)

#billy_cirys.show_info()

miley_cirys = Child("Curys","Blue",5)

miley_cirys.show_info()

#print(miley_cirys.last_name)

#print(miley_cirys.number_of_toys)