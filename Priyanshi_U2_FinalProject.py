import random

play_again = "Yes" #assigning the required condition/value for the code to start again

#opening statements
print("Welcome to the sustainable city builder!" )
print("You are tasked to pick specific options from the questions presented to you.")
print("Have fun and make the right decisions (or not...)!")

print(" ")

name_city = input("Wait! Before we begin, what will you name your city?: ")
print(name_city, "is a great name! Lets begin...")

#Lists of the questions and the positive/negative statements
questions = ["What kind of energy will your city use? (petrol, hydroelectricity, gas, solar power):",
             "What kind of transportation will be used? (cars, trains, busses, subway): ",
             "What materials will be used to build your city? (wood, glass, steel, concrete): "
             "What type of food joints will be available? (fast-food, Convenience store, grocery store): "
             ""] #add more later

positive_statements = ["Your city is thriving in sustainability! Good job in choosing the right choices."
                      "Citizens are happy. Environment is sustainable and clean. You did an amazing job!"
                       "The city has passed the sustainability requirements! Your city will live on for much longer."
                       ]
negative_statements = [""]
neutral_statements = [""]
answers = [] #empty list where the answers inputted by the user will be stored



