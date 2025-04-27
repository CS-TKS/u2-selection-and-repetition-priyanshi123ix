import random

play_again = "yes" #assigning the required condition/value for the code to start again

#Lists of the questions and the positive/negative statements
questions = ["What kind of energy will your city use? (petrol, hydroelectricity, gas, solar power):",
             "What kind of transportation will be used? (cars, trains, busses, subway): ",
             "What materials will be used to build your city? (wood, glass, steel, concrete): ",
             "What type of food joints will be available? (fast-food, Convenience store, grocery store): "
             ""] #add more later

positive_statements = ["Your city is thriving in sustainability! Good job in choosing the right choices."
                      "Citizens are happy. Environment is sustainable and clean. You did an amazing job!"
                       "The city has passed the sustainability requirements! Your city will live on for much longer."
                       ]
negative_statements = ["Your city did terribly! The air is filled with smoke and your citizens are in grave conditions...",
                       "You tried...but it didnt work. Your city plan will not be established!",
                       "The plans are dying, everything is! What have you done? Choose the right choices next time.",
                       "You've been fired! You did a terrible job, and you've killed many of your citizens"
                       ]
neutral_statements = ["Your city is doing well, however many improvements could be made.",
                      "Your citizens do not love the city, but they do not hate it either. Choose wisely next time",
                      "Your city is...going..? Its not great but it could be worse. A for effort."
                      ]

while play_again.lower() == "yes":
    answers = []
    score = 0
    # opening statements
    print("Welcome to the sustainable city builder!")
    print("You are tasked to pick specific options from the questions presented to you.")
    print("Have fun and make the right decisions (or not...)!")

    print(" ")

    name_city = input("Wait! Before we begin, what will you name your city?: ")
    print(name_city, "is a great name! Lets begin...")

    for q in questions:
        answer = input(q).lower()
        answers.append(answer)

        if q == questions[0]:
            if answer == "petrol":
                score -= 5
            elif answer == "hydroelectricity":
                score += 10
            elif answer == "solar power":
                score += 15
            elif answer == "gas":
                score -= 10
            else:
                print(" ")
                print("Invalid response, one more try until points are deducted.")

                for attempt in range(1):
                    answer = input(q).lower()

                if q == questions[0]:
                    if answer == "petrol":
                        score -= 5
                    elif answer == "hydroelectricity":
                        score += 10
                    elif answer == "solar power":
                        score += 15
                    elif answer == "gas":
                        score -= 10
                    else:
                        print("Answer still invalid. Deducting 5 points...")
                        score -= 5


        print(score)

        #elif q == questions[2]



