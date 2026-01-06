#Make a Number guessing game where there will be a hidden number and the user has to find the number between 1 and 1000
#If the input answer is greater than the actual answer print "Your Guess is Too high" else "Your Guess is Too Low"
#No.of Guesses =10
#If the no.of guesses is over then print"You have ran out of Available Guesses"
#If the user wins print no.of guesses he took to win
#Use a built-in function random
import random
key=random.randint(1,1000)
guess=10
print("                   WELCOME TO MAGICAL NUMBER GUESSING GAME             ")
print("                  FIND THE MAGICAL NUMBER BETWEEN 1 TO 1000            ")
print("                       LET    THE    GAME    BEGIN!!!!                 ")
print("No.of Available Guesses You have:",guess)
count=1
while(guess!=0):
    user=int(input("Enter your Number:"))
    if(user!=key):
        if(user!=key and user-key>=-10 and user-key<0 and guess!=1):
            print("Add a Number from 1 to 10")
        elif(user!=key and user-key<-10 and user-key>=-50 and guess!=1):
            print("Add a Number from 11 to 50")
        elif(user!=key and user-key<-50 and user-key>=-100 and guess!=1):
            print("Add a number from 51 to 100")
        elif(user!=key and user-key<-100 and guess!=1):
            print("Your Guess is Too Low")
        if(user!=key and user-key<=10 and user-key>0 and guess!=1):
            print("Substract a Number from 1 to 10 ")
        elif(user!=key and user-key<=50 and user-key>10 and guess!=1):
            print("Substract a Number from 11 to 50")
        elif(user!=key and user-key<=100 and user-key>50 and guess!=1):
            print("Substract a Number from 51 to 100 ")
        elif(user!=key and user-key>100 and guess!=1):
            print("Your Guess is Too high")
        guess=guess-1
        count=count+1
        print("No.of Guesses Left:",guess)
        if(guess==0):
            print("The Magical Number was:",key)
            print("You have ran out of Available Guesses")
            print("Pls Try Again!")
        continue
    else:
        print("Hurray!! and Congratulations You have Successfully Found the Magical Number:",user)
        print("No.of Guesses You Took is:",count)
        break
