while True:
    print("WELCOME TO ODD-EVE CHOOSE CRAZY OR NORMAL")
    print("1. Normal")
    print("2. Crazy")
    print("3. exit")
    ch = int(input("choose 1,2 or 3: "))
    if ch == 1:


        print("""Game of normal odd-eve
        1. Choose odd or eve.
        2. If the toss is in your favour, then  bat or bowl. If the toss is not in your
           favour then you have to do what the computer asks you to.
        3. If it's your batting (say), choose a number from 1 to 10, if it matches the
           the number with computer (who is bowling) then you are out. If it doesn't then 
           the runs will keep adding till all 30 balls are over or you lose all 5 wickets.
        4. If you get all out or the balls are finished, the computer will try and chase down
           your score. If it does, then the computer wins else you win.
        5. If it's your bowling, the roles of the computer and yourself will get reversed in
           steps 3 and 4.""")

        print("\n---------- Start Game ----------")

        import random

        # Toss

        print("\n----------------------------TOSS-------------------------------------")
        toss = (input("Choose odd or eve: ")).lower()

        r_toss = random.randint(1, 2)
        r2_c_ch = random.randint(1, 2)

        u_ch = 0
        c_ch = 0

        if r_toss == 1 and toss == "odd":
            print("\nYou won the toss")
            u_ch = (input("Choose bat or ball: ")).lower()

        elif r_toss == 2 and toss == "eve":
            print("\nYou won the toss")
            u_ch = (input("Choose bat or ball: ")).lower()

        else:
            print("\n Computer won the toss")

            if r2_c_ch == 1:
                c_ch = "bat"
                print("Computer choose to", c_ch)

            elif r2_c_ch == 2:
                c_ch = "ball"
                print("Computer choose to", c_ch)

        # First Innings

        print("\n---------- First Innings----------")

        runs_1 = 0
        wickets_1 = 0
        balls_1 = 0

        while wickets_1 != 5 and balls_1 != 30:

            u_choice = int(input("\nChoose a number from 1 to 10: "))
            c_choice = random.randint(1, 10)

            if u_choice < 1 or u_choice > 10:
                print("\nPlease choose a value from 1 to 10.")

            else:
                print("Your choice: ", u_choice, "\nComputer's choice: ", c_choice)

                if u_choice == c_choice:
                    wickets_1 += 1

                else:
                    if u_ch == "bat" or c_ch == "ball":
                        Bat_first = "You"
                        Ball_first = "Computer"
                        runs_1 += u_choice

                    elif u_ch == "ball" or c_ch == "bat":
                        Bat_first = "Computer"
                        Ball_first = "You"
                        runs_1 += c_choice

                print("\nScore =", runs_1, "/", wickets_1)

                balls_1 += 1

                print("Balls remaining: ", 30 - balls_1)

        print("\n---------- End of Innings ----------")

        print("\nFinal Score:")
        print("Runs =", runs_1)
        print("wickets =", wickets_1)

        print("\n", Ball_first, "needs", runs_1 + 1, "runs to win.")

        # Second Innings

        print("\n---------- Second Innings Begins ----------")

        runs_2 = 0
        wickets_2 = 0
        balls_2 = 0

        while wickets_2 != 5 and balls_2 != 30 and runs_2 <= runs_1:

            u_choice = int(input("\nChoose any number from 1 to 10: "))
            c_choice = random.randint(1, 10)

            if u_choice < 1 or u_choice > 10:
                print("\nPlease choose a value from 1 to 10.")

            else:
                print("Your choice: ", u_choice, "\nComputer's choice: ", c_choice)

                if u_choice == c_choice:
                    wickets_2 += 1

                else:
                    if Bat_first == "Computer":
                        runs_2 += u_choice
                        Bat_second = "You"

                    elif Bat_first == "You":
                        runs_2 += c_choice
                        Bat_second = "Computer"

                print("\nScore =", runs_2, "/", wickets_2)

                balls_2 += 1



                if runs_2 <= runs_1 and balls_2 <= 29 and wickets_2 != 5:
                    print("To win:", runs_1 - runs_2 + 1, "runs needed from", 30 - balls_2, "balls.")

        print("\n---------- End of Innings ----------")

        print("\nFinal Score:")
        print("Runs =", runs_2)
        print("wickets =", wickets_2)

        # Result of Match

        print("\nResult")

        if runs_1 > runs_2:

            if Bat_first == "You":
                print("\n You won the Match by", runs_1 - runs_2, "runs.")

            else:
                print("\n The Computer won the Match by", runs_1 - runs_2, "runs.")

        elif runs_2 > runs_1:

            if Bat_second == "You":
                print("\n You won the Match by", 5 - wickets_2, "wickets.")

            else:
                print("\nThe Computer won the Match by", 5 - wickets_2, "wickets.")

        else:
            print("NO RESULT.")


    if ch == 2:

        print("""Game of crazy odd-eve
        1. Choose odd or eve.
        2. If the toss is in your favour, then  bat or bowl. If the toss is not in your
           favour then you have to do what the computer asks you to.
        3. If it's your batting (say), choose a number from 1 to 10, if it matches the
           the number or if it is different with computer (who is bowling) then the runs will be your choice**2. If it is 
           +1 or -1 than the computer's choice then you are out.
        4. If you get all out or the balls are finished, the computer will try and chase down
           your score. If it does, then the computer wins else you win.
        5. If it's your bowling, the roles of the computer and yourself will get reversed in
           steps 3 and 4. """)

        print("\n---------- Start Game ----------")

        import random

        # Toss

        print("\n----------------------------------Toss---------------------------------")
        toss = (input("Choose odd or eve: ")).lower()

        r_toss = random.randint(1, 2)
        r2_c_ch = random.randint(1, 2)

        u_ch = 0
        c_ch = 0

        if r_toss == 1 and toss == "odd":
            print("\nYou won the toss")
            u_ch = (input("Choose bat or ball: ")).lower()

        elif r_toss == 2 and toss == "eve":
            print("\nYou won the toss")
            u_ch = (input("Choose bat or ball: ")).lower()

        else:
            print("\n Computer won the toss")

            if r2_c_ch == 1:
                c_ch = "bat"
                print("Computer choose to", c_ch)

            elif r2_c_ch == 2:
                c_ch = "ball"
                print("Computer choose to", c_ch)

        # First Innings

        print("\n---------- First Innings Begins ----------")

        runs_1 = 0
        wickets_1 = 0
        balls_1 = 0

        while wickets_1 != 5 and balls_1 != 30:

            u_choice = int(input("\nChoose any number from 1 to 10: "))
            c_choice = random.randint(1, 10)

            if u_choice < 1 or u_choice > 10:
                print("\nPlease choose a value from 1 to 10.")

            else:
                print("Your choice: ", u_choice, "\nComputer's choice: ", c_choice)

                if u_choice == c_choice + 1 or u_choice == c_choice - 1:
                    wickets_1 += 1

                else:
                    if u_ch == "bat" or c_ch == "ball":
                        Bat_first = "You"
                        Ball_first = "Computer"
                        runs_1 += u_choice ** 2

                    elif u_ch == "ball" or c_ch == "bat":
                        Bat_first = "Computer"
                        Ball_first = "You"
                        runs_1 += c_choice ** 2

                print("\nScore =", runs_1, "/", wickets_1)

                balls_1 += 1



                print("Balls remaining: ", 30 - balls_1)

        print("\n---------- End of Innings ----------")


        print("Runs =", runs_1)
        print("wickets =", wickets_1)

        print("\n", Ball_first, "needs", runs_1 + 1, "runs to win.")

        # Second Innings

        print("\n---------- Second Innings Begins ----------")

        runs_2 = 0
        wickets_2 = 0
        balls_2 = 0

        while wickets_2 != 5 and balls_2 != 30 and runs_2 <= runs_1:

            u_choice = int(input("\nChoose any number from 1 to 10: "))
            c_choice = random.randint(1, 10)

            if u_choice < 1 or u_choice > 10:
                print("\nPlease choose a value from 1 to 10.")

            else:
                print("Your choice: ", u_choice, "\nComputer's choice: ", c_choice)

                if u_choice == c_choice + 1 or u_choice == c_choice - 1:
                    wickets_2 += 1

                else:
                    if Bat_first == "Computer":
                        runs_2 += u_choice ** 2
                        Bat_second = "You"

                    elif Bat_first == "You":
                        runs_2 += c_choice ** 2
                        Bat_second = "Computer"

                print("\nScore =", runs_2, "/", wickets_2)

                balls_2 += 1



                if runs_2 <= runs_1 and balls_2 <= 29 and wickets_2 != 5:
                    print("To win:", runs_1 - runs_2 + 1, "runs needed from", 30 - balls_2, "balls.")

        print("\n---------- End of Innings ----------")


        print("Runs =", runs_2)
        print("wickets =", wickets_2)

        # Result of Match

        print("\n--------------------------------------------- RESULT -------------------------------------------------")

        if runs_1 > runs_2:

            if Bat_first == "You":
                print("\n You won the Match by", runs_1 - runs_2, "runs.")

            else:
                print("\n The Computer won the Match by", runs_1 - runs_2, "runs.")

        elif runs_2 > runs_1:

            if Bat_second == "You":
                print("\n You won the Match by", 5 - wickets_2, "wickets.")

            else:
                print("\n The Computer won the Match by", 5 - wickets_2, "wickets.")

        else:
            print("NO RESULT")


    if ch == 3:
        exit()
