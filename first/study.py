# Part 2: Study Habits
# 1. Please complete the following:
#   Your First name and Last Name: Saif Shaikh
#   Your Student ID: 261202410


# 2. Write your program here:

#inputs from the user
A = int(input('How many hours out of 10 do you spend on attending class? '))
C = float(input("How many hours do you practice coding and review concepts each week? (out of 10): "))
D = float(input('How many deep hours per week on average do you spend studying without distractions: '))
G = float(input('How many hours of sleep do you have per night on average? (out of 24): '))
E = float(input('How many hours do you spend on exercise and/or hobbies and/or time socializing with friends or family per week ? (out of 10): '))
H = input("Do you ask for help when stuck? (yes/no): ")

#the variable for weightage for each input to calculate the score
STUDY_WEIGHT = 0.55
ATTENDANCE_WEIGHT = 0.3
PRACTICE_WEIGHT = 0.7
WELLNESS_WEIGHT = 0.25
HELP_WEIGHT = 0.2

#conditions to find the focus factor value
if G>=6 and D>=3:
    F = 1
elif G<6:
    F = 0.8
elif G>=6 and D<3:
    F = 0.8

#conditions to determine the value of H (1 if asks for help and 0 if doesnt)
if H == "yes":
    H = 1
else:
    H = 0

 
#formula of calculating the probability factor 
P = STUDY_WEIGHT*F*((A/10 *ATTENDANCE_WEIGHT)+(C/10 * PRACTICE_WEIGHT)) + WELLNESS_WEIGHT* E/10 + HELP_WEIGHT*H

#this function rounds P to two decimal places
P = round(P,2)

#prints the score upto two decimal points
print("Your success score is: ", P)

#if the value of P is greater than equal to 0.7 it gives good feed back
if P>=0.7:
    print("You're on track to do well in your class!")
#if the value of P is lower than 0.7 then it gives feedback according to individual inputs determining which is lower
else:
    print("Your success score is low. Below are suggestions to improve score:")
    if F<1:
        print("\t* Consider improving your sleep and focus habits:")
        if G<6:
            print("\t\t+ try sleeping for more than 6 hours")
        if D<3:
            print("\t\t+ make sure to get at least 3 hours of deep focus without any distractions.")
    if A<3:
        print("\t* Consider attending more classes.")
    if C <= 4:
        print("\t* Consider practicing coding more.")
    if H ==0:
        print("\t* Consider asking for help when stuck.")