# 4COSC006C     : Software Development I - Coursework Specification (2020/21)
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution

# Module Leader :   Saman Hettiarachchi
# Student ID    :   1809821
# IIT ID        :   2019784
# Date          :   December 11th 2020

# Part 2 - Student Version (Validation)

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

#---Create the List---
Range_List = [0,20,40,60,80,100,120]

# Functoin 1
#---To check user input values are Integers and in the given Range---
def Int_RList():
    global Pass,Defer,Fail

    while True:                                                            # If Total is incorrect to check new input values obey the following conditions 
        while True:
            try:
                Pass = int(input("Please Enter Your Credits At Pass : "))  # Checking the Pass input value is an Integer
                if Pass not in Range_List:                                 # Checking the Pass input value is not in the given Range
                    print("\t","*"*5,"Out of Range","*"*5,"\n")            
                else:
                    break                                                  # If the Pass input value is in the given Range break and go to the next record
            except:
                print("\t","*"*5,"Integer Required","*"*5,"\n")            # Pass input value is not an Integer 

        while True:
            try:
                Defer = int(input("Please Enter Your Credits At Defer: ")) # Checking the Defer input value is an Integer
                if Defer not in Range_List:                                # Checking the Defer input value is not in the given Range
                    print("\t","*"*5,"Out of Range","*"*5,"\n")            
                else:
                    break                                                  # If the Defer input value is in the given Range break and go to the next record
            except:
                print("\t","*"*5,"Integer Required","*"*5,"\n")            # Defer input value is not an Integer      
        while True:
            try:
                Fail = int(input("Please Enter Your Credits At Fail : "))  # Checking the Fail input value is an Integer
                if Fail not in Range_List:                                 # Checking the Fail input value is not in the given Range
                    print("\t","*"*5,"Out of Range","*"*5,"\n")
                else:
                    break                                                  # If the Fail input value is in the given Range break and go to the next record
            except:
                print("\t","*"*5,"Integer Required","*"*5,"\n")            # Fail input value is not an Integer

        Total = TotalAndOutcome_Prog()                                    # Calling the Function 2
        if Total:                                                         # If total is correct (True) program is end. If not (False) program is continue the Function 1 and get new values
            break

# Function 2           
#---To check the total of the user input values are equal to 120 or not and execute the Progresion Outcome---                
def TotalAndOutcome_Prog():

    Total = True
    
    if Pass + Defer + Fail == 120:                       # If the user input values are equal to 120

        if Pass == 120:                                  # Progression Outcome of "Progress"
            print("Progress")

        elif Pass == 100 and Defer <= 20 and Fail <= 20: # Progression Outcome of "Progress (Module Trailer)"
            print("Progress (Module Trailer)")

        elif Fail >= 80 and Fail <= 120:                 # Progression Outcome of "Exclude"  
            print("Exclude")

        else:                                            # Progression Outcome of "Do not progress - Module Retriever"
            print("Do not progress - Module Retriever")

    elif Pass + Defer + Fail > 120:                      # If the user input values equal to more than 120
        
        print("\t","*"*5,"Total Inccorect:- Total credits is More than 120","*"*5,"\n")
        Total = False
        
    else:                                                # If the user input values equal to less than 120
        print("\t","*"*5,"Total Inccorect:- Total credits is Less than 120","*"*5,"\n")
        Total = False
        
    return Total                                         # Return to Function 1

#---Calling the Functions 1
Int_RList()


#---End of Progression---
S = "** Progression Outcome Program - End **"
print("\n")
print("*"*len(S))
print(S)
print("*"*len(S))
 
