import random

play_again = "yes" #determining the required condition/value for the code to start again

#Lists of the questions and the positive/neutral/negative statements
questions = ["What kind of energy will your city use? (petrol, hydroelectricity, gas, solar power): ",
             "What kind of transportation will be used? (cars, trains, busses, subway): ",
             "What materials will be used to build your city? (wood, glass, steel, concrete): ",
             "What type of food joints will be available? (fast food, convenience store, grocery store): ",
             "How many green spaces are you going to implement in your city? (1, 3, 6, 9): "
             ]

positive_statements = ["Your city is thriving in sustainability! Good job in choosing the right choices.",
                      "Citizens are happy. Environment is sustainable and clean. You did an amazing job!",
                       "Your investments in renewable energy and green spaces have paid off; air quality has improved, and wildlife is returning!",
                       "Citizens are proud to call this city home. Thanks to your decisions, future generations will enjoy a cleaner, safer world."
                       ]
negative_statements = ["Your city did terribly! The air is filled with smoke and your citizens are in grave conditions...",
                       "You tried...but it didnt work. Your city plan will not be established!",
                       "The plants are dying, everything is! What have you done? Choose the right choices next time.",
                       "You've been fired! You did a terrible job, and you've killed many of your citizens"
                       ]
neutral_statements = ["Your city is doing well, however many improvements could be made.",
                      "Your citizens do not love the city, but they do not hate it either. Choose wisely next time",
                      "Your city is...going..? Its not great but it could be worse. A for effort.",
                      "Citizens are getting by. Not thrilled, not angry. Just kind of... existing."
                      ]

#starting the while loop; will restart the code then the value of "play_again" is "yes"
while play_again.lower() == "yes":
    answers = [] #empty list to append the user's inputs into
    score = 0 #setting initial score to 0

    # opening statements
    print("Welcome to the sustainable city builder!")
    print("You are tasked to pick specific options from the questions presented to you.")
    print("Have fun and make the right decisions (or not...)!")

    print(" ") #space

    name_city = input("Wait! Before we begin, what will you name your city?: ")
    print((name_city[0].upper() + name_city [1:].lower()), "is a great name! Lets begin...")

    # Selecting certain questions from the list named 'questions'; storing it temporarily in variable 'q'
    for q in questions:
        answer = input(q).lower()
        answers.append(answer) #adding the user's input into the empty list to check its corresponding scores/values

        #checking the input/score values of question no. 1
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

                # another for loop to give the user one more chance to only choose the given options
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
                        score -= 5 #if answer is still wrong, 5 points are deducted
                        print(" ")

        # checking the input/score values of question no. 2
        elif q == questions[1]:
            if answer == "cars":
                score -= 10
            elif answer == "trains":
                score -= 5
            elif answer == "busses":
                score += 10
            elif answer == "subway":
                score += 20
            else:
                print(" ")
                print("Invalid response, one more try until points are deducted.")

                # another for loop to give the user one more chance to only choose the given options
                for attempt in range(1):
                    answer = input(q).lower()

                if q == questions[1]:
                    if answer == "cars":
                        score -= 10
                    elif answer == "trains":
                        score -= 5
                    elif answer == "busses":
                        score += 10
                    elif answer == "subway":
                        score += 20
                    else:
                        print("Answer still invalid. Deducting 5 points...")
                        score -= 5 #if answer is still wrong, 5 points are deducted
                        print(" ")

        # checking the input/score values of question no. 3
        elif q == questions[2]:
            if answer == "wood":
                score += 5
            elif answer == "glass":
                score -= 2
            elif answer == "steel":
                score += 25
            elif answer == "concrete":
                score -= 20
            else:
                print(" ")
                print("Invalid response, one more try until points are deducted.")

                # another for loop to give the user one more chance to only choose the given options
                for attempt in range(1):
                    answer = input(q).lower()

                if q == questions[2]:
                    if answer == "wood":
                        score += 5
                    elif answer == "glass":
                        score -= 2
                    elif answer == "steel":
                        score += 25
                    elif answer == "concrete":
                        score -= 20
                    else:
                        print("Answer still invalid. Deducting 5 points...")
                        score -= 5  # if answer is still wrong, 5 points are deducted
                        print(" ")

        # checking the input/score values of question no. 4
        elif q == questions[3]:
            if answer == "fast food":
                score -= 5
            elif answer == "convenience store":
                score += 5
            elif answer == "grocery store":
                score += 15
            else:
                print(" ")
                print("Invalid response, one more try until points are deducted.")

                # another for loop to give the user one more chance to only choose the given options
                for attempt in range(1):
                    answer = input(q).lower()

                if q == questions[3]:
                    if answer == "fast food":
                        score -= 5
                    elif answer == "convenience store":
                        score += 5
                    elif answer == "grocery store":
                        score += 15
                    else:
                        print("Answer still invalid. Deducting 5 points...")
                        score -= 5 #if answer is still wrong, 5 points are deducted
                        print(" ")

        # checking the input/score values of question no. 5
        elif q == questions[4]:
            if answer == "1":
                score -= 15
            elif answer == "3":
                score -= 5
            elif answer == "6":
                score += 5
            elif answer == "9":
                score += 15
            else:
                print(" ")
                print("Invalid response, one more try until points are deducted.")

                # another for loop to give the user one more chance to only choose the given options
                for attempt in range(1):
                    answer = input(q).lower()

                if q == questions[4]:
                    if answer == "1":
                        score -= 15
                    elif answer == "3":
                        score -= 5
                    elif answer == "6":
                        score += 5
                    elif answer == "9":
                        score += 15
                    else:
                        print("Answer still invalid. Deducting 5 points...")
                        score -= 5 #if answer is still wrong, 5 points are deducted

            print(" ")

            print("You're all set!")
            print("Its time to travel to the future and see the state of your city! [stand by...]")

            print(" ")

            print("FINAL SCORE: ", score, "/100") #prints the final score of the user

            # randomly choosing specific statements to present to the user depending on their score
            if score < 40:
                print("FAILED.")
                print(random.choice(negative_statements))
            elif 40 <= score <= 60: #in between a specific range
                print("DECENT.")
                print(random.choice(neutral_statements))
            elif score > 60:
                print("EXCELLENT.")
                print(random.choice(positive_statements))

            #ask the user if they want to play again; if yes the condition at the start is true and code repeats
            play_again = input("Do you want to play again? (yes/no): ").lower()

            print(" ")

            # while loop checks if the user's answer is correct to the choices given
            # if not it will continue to ask the user again until the they respond using the correct options
            while play_again != "yes" and play_again != "no":
                print("Invalid response. Try again.")
                play_again = input("Do you want to play again? (yes/no): ").lower()

                print(" ")

            # if the user says no, the code will stop and ending statement will be printed
            if play_again == "no":
                print("Hope you had fun! See you next time.")

