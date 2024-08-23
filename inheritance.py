# class person:
#     def __init__(self,fname,lname):
#        self.firstname=fname
#        self.lastname=lname

#     def printname(self):
#         print(self.firstname,self.lastname)
# class student(person):
#         def __init__(self, fname, lname):
#              person.__init__(self, fname, lname)  # Directly call the parent class's __init__ method
# x=student("mike","olsen")
# x.printname()            


# class animal:
#     def __init__(self,breed,colour):
#         self.type=breed
#         self.colours=colour

#     def printbreed(self):
#         print(self.type,self.colours)   
        

# class dogs(animal):
#         def __init__(self,breed,colours):
#             animal.__init__(self,breed,colours)

     
# x=dogs("doberman","black")    
# x=printbreed()
# # x= animal_colour()

        
# class Animal:
#     def __init__(self, breed, colour):
#         self.type = breed
#         self.colours = colour

#     def printbreed(self):
#         print(self.type, self.colours)

# class Dogs(Animal):
#     def __init__(self, breed, colours):
#         Animal.__init__(self, breed, colours)  # Initialize the parent class

# # Create an instance of Dogs
# x = Dogs("doberman", "black")
# x.printbreed()  # This will correctly print: doberman black
