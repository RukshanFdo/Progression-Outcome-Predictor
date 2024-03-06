# 4COSC006C     : Software Development I - Coursework Specification (2020/21)
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution

# Module Leader :   Saman Hettiarachchi
# Student ID    :   1809821
# IIT ID        :   2019784
# Date          :   December 11th 2020

# Part 1 - Student Version


#---Use Len function to decorate with stars----
S = "** Progression Outcome Program - Start **"
print("*"*len(S))
print(S)
print("*"*len(S))
print("\n")

#---Create Variables---
Pass  = 0
Defer = 0
Fail  = 0

# Function 1           
#---Execute the Progresion Outcome---                
# Using Conditions to figure outcome
def TotalAndOutcome_Prog():
    if Pass == 120:                                  # Progression Outcome of "Progress"
        print("Progress")
    
    elif Pass == 100 and Defer <= 20 and Fail <= 20: # Progression Outcome of "Progress (Module Trailer)"
        print("Progress (Module Trailer)")
    
    elif Fail >= 80 and Fail <= 120:                 # Progression Outcome of "Exclude"  
        print("Exclude")
    
    else:                                            # Progression Outcome of "Do not progress - Module Retriever"
        print("Do not progress - Module Retriever")

#---Main Program
# Input Integer Values for Variables
Pass  = int(input("Please Enter Your Credits At Pass : "))
Defer = int(input("Please Enter Your Credits At Defer: "))
Fail  = int(input("Please Enter Your Credits At Fail : "))

#---Calling the Functions 1---
TotalAndOutcome_Prog()

#---End of Progression---
S = "** Progression Outcome Program - End **"
print("\n")
print("*"*len(S))
print(S)
print("*"*len(S))
 

    

