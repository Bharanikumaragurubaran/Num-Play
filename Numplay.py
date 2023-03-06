import random


def gaming(str1=0, str2=0, count=0):
    if str1 != str2:
        if count == 5:
            print(str2) #give divisors in range of 10 to 50
            #print(div_list)
            if len(list1) != 0:
                div = random.choice(list1)  ## if the num have divisors in the range of 10 to 50, this fn will provide the divisor
            elif len(list1) == 0 and len(list5) != 0:
                div = random.choice(list5)
            else:
                div = random.choice(div_list)  ## else this block will provide a random divisor

        elif count == 4:
            print(str2) #give divisors in range of 51 to 99
            if len(list2) != 0:
                div = random.choice(list2)  #give divisors in range of 51 to 99
            elif len(list2) == 0 and len(list1) != 0:
                div = random.choice(list1)  #give divisors in range of 10 to 50
            elif len(list2) == 0 and len(list1) == 0 and len(list5) != 0:
                div = random.choice(list5)  #give divisors in range of 1 to 9
            else:
                div = random.choice(div_list) # random divisor
            #divisors.append(div)
            #print(f"XXXX is divisible by {divisors}")

        elif count == 3:
            print(str2) #give divisors in range of 100 to 500
            n = str(str1)
            print(f"XXXX - Starts with {n[0]} i.e., {n[0]}XXX")  # shows 1st value of the num
            if len(list3) != 0:
                div = random.choice(list3)  #give divisors in range of 100 to 500
            elif len(list3) == 0 and len(list2) != 0:
                div = random.choice(list2)  #give divisors in range of 51 to 99
            elif len(list3) == 0 and len(list2) == 0 and len(list1) != 0:
                div = random.choice(list1)  #give divisors in range of 10 to 50
            elif len(list3) == 0 and len(list2) == 0 and len(list1) == 0 and len(list5) != 0:
                div = random.choice(list5)  #give divisors in range of 1 to 9
            else:
                div = random.choice(div_list)   # random divisor

        elif count == 2:
            print(str2) #give divisors in range of 501 to 999 and 3rd digit
            n = str(str1)
            if len(list4) != 0:
                div = random.choice(list4) #give divisors in range 501 to 999
            elif len(list4) == 0 and len(list3) != 0:
                div = random.choice(list3) #give divisors in range of 100 to 500
            elif len(list3) == 0 and len(list4) == 0 and len(list2) != 0:
                div = random.choice(list2) #give divisors in range of 51 to 99
            elif len(list3) == 0 and len(list4) == 0 and len(list2) == 0 and len(list1) != 0:
                div = random.choice(list1) #give divisors in range of 10 to 50
            elif len(list3) == 0 and len(list4) == 0 and len(list2) == 0 and len(list1) == 0 and len(list5) != 0:
                div = random.choice(list5) #give divisors in range of 1 to 9
            else:
                div = random.choice(div_list) # random divisor
            print(f"XXXX - ist and 3rd digit are {n[0]}, {n[2]} i.e., {n[0]}X{n[2]}X")  ## shows 1st aand 3rd value of the num
        else:
            div = 1
        return False, count, div

    else:
        return True, count, 0


play = True
while play:

    invalid_num = False
    while not invalid_num:
        data = random.randint(1000, 9999)
        div_list = []
        for i in range(1, (data // 2) + 1):
            if data % i == 0:
                div_list.append(i)

        if len(div_list) <= 8:     ## Number should have atleast 8 divisors to make the guessing game interesting..
            invalid_num = True

        else:
            print("Find XXXX")
            chances = 6
            game_done = False
            #result = []
            divisors = []
            while not game_done:
                win = False
                chances -= 1

                if chances == 0:
                    print("You lost :(")
                    print("The num is:", data)
                    again = input("Do you want to play another game (y/n)?:")
                    game_done = True
                    invalid_num = True
                    if again.lower() == 'y':
                        print("restarting...")
                    else:
                        print("thanks for playing..")
                        play = False
                        break

                else:
                    div_list.pop()  ## removing the last divisor because last divisoer of a number will be the number itself.

                    list1 = []  ## list1 will have divisor values in the range of 10 to 50
                    list2 = []  ## list2 will have divisor values in the range of 51 to 99
                    list3 = []  ## list3 will have divisor values in the range of 100 to 500
                    list4 = []  ## list4 will have divisor values in the range of 501 to 999
                    list5 = []  ## list5 will have divisor values in the range of 1 to 10

                    for i in div_list:
                        if i in range(10, 51):
                            list1.append(i)
                        elif i in range(51, 100):
                            list2.append(i)
                        elif i in range(100, 501):
                            list3.append(i)
                        elif i in range(501, 1000):
                            list4.append(i)
                        else:
                            list5.append(i)

                    print(f"Total chances available: {chances}")
                    try:
                        num = int(input("Enter your number: "))


                        a = str(data)
                        b = str(num)
                        if len(b) != 4:
                            print("Please enter 4 digit number")
                            chances += 1
                        else:
                            win, c, x = gaming(data, num, chances)
                            if win == False and c != 1:
                                divisors.append(x)  ## x is one of the divisor from div_list
                                div_list.remove(x)
                                print("number is divisible by: ", divisors)  ## hint for user


                        if win == True:
                            game_done = True
                            if c == 5:
                                print("You guessed it right!!!")
                                print("No. of chances took:", 6-c)
                            elif c == 4:
                                print("You guessed it right!!!")
                                print("No. of chances took:", 6-c)
                            elif c == 3:
                                print("You guessed it right!!!")
                                print("No. of chances took:", 6-c)
                            elif c == 2:
                                print("You guessed it right!!!")
                                print("No. of chances took:", 6-c)
                            else:
                                print("You guessed it right!!!")
                                print("No. of chances took:", 6-c)

                            again = input("Do you want to play another game (y/n)?:")
                            if again.lower() == 'y':
                                print("restarting...")
                            else:
                                print("thanks for playing..")
                                invalid_num = True
                                play = False
                    except ValueError:
                        print("Error: Please enter 4 digit number")
                        chances += 1


