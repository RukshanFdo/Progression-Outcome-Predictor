# 4COSC006C     : Software Development I - Coursework Specification (2020/21)
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution

# Module Leader :   Saman Hettiarachchi
# Student ID    :   1809821
# IIT ID        :   2019784
# Date          :   December 11th 2020

# Part 4 - Vertical Histogram (optional exetension)

#---Use Len function to decorate with stars----
S = "** Progression Outcome Program - Start **"
print("*"*len(S))
print(S)
print("*"*len(S))
print("\n")

#---Create Variables---
Pass     = 0
Defer    = 0
Fail     = 0
Progress = 0
Trailer  = 0
Exclude  = 0
Retriever= 0

#---Create the List---
Range_List = [0,20,40,60,80,100,120]


#---To check the total of the inputs are equal to 120 or not---
        
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

        Total = TotalAndOutcome_Prog()                                     # Calling the Function 2
        if Total:                                                          # If total is correct (True) program is end. If not (False) program is continue the Function 1 and get new values
            break

            
# Function 2           
#---To check the total of the user input values are equal to 120 or not and execute the Progresion Outcome---                

def TotalAndOutcome_Prog():
    global Progress,Trailer,Retriever,Exclude
    
    Total = True
    
    if Pass + Defer + Fail == 120:                       # If the user input values are equal to 120

        if Pass == 120:                                  # Progression Outcome of "Progress"
            print("Progress")
            Progress = Progress + 1
            
        elif Pass == 100 and Defer <= 20 and Fail <= 20: # Progression Outcome of "Progress (Module Trailer)"
            print("Progress (Module Trailer)")
            Trailer = Trailer + 1
            
        elif Fail >= 80 and Fail <= 120:                 # Progression Outcome of "Exclude"  
            print("Exclude")
            Exclude = Exclude + 1

        else:                                            # Progression Outcome of "Do not progress - Module Retriever"
            print("Do not progress - Module Retriever")
            Retriever = Retriever + 1

    elif Pass + Defer + Fail > 120:                      # If the user input values equal to more than 120
        
        print("\t","*"*5,"Total Inccorect:- Total credits is More than 120","*"*5,"\n")
        Total = False
        
    else:                                                # If the user input values equal to less than 120
        print("\t","*"*5,"Total Inccorect:- Total credits is Less than 120","*"*5,"\n")
        Total = False
        
    return Total                                         # Return to Function 1


                        
# Function 3
#---To create the Vertical Histogram---
def Vertical_Histogram():
    print("\n")
    print("-"*75)

    #---Creat a List for Vertical---
    # Create a 2D list. List have main 4 indexces
    Vertical_List=[[],[],[],[]] # Create a list variable for colect data its helps to printing part
    #if Progress =3
       #Trailer  =5
       #Retriever=2
       #Exclude  =1
    # Program create 2d list as [[1,1,1,0,0],[1,1,1,1,1,],[1,1,0,0,0],[1,0,0,0,0]]
    # 0 index for Progress
    # 1 index for Trailer
    # 2 index for Retriever
    # 3 index for Exclude
    
    print("Vertical Histogram\n")
    print("Progress",Progress,"|"," Trailer",Trailer,"|"," Retriever",Retriever,"|"," Exclude",Exclude)

    # Find max count between (Progress,Trailer,Retriever,Exclude)
    Progression_Type = max(Progress,Trailer,Retriever,Exclude) # max count is the sub list's indexses count

    #---Make a loop using max value---
    # Creating first 0 index in Vertical_List
    for a in range(Progression_Type):        
        if Progress > a:                     # Find if progress value less than a or not. This part run when if True
            Progression = 1                  # Assign Progression to 1
        else:                                # This part run when if False
            Progression = 0                  # Assign Progression to 0
    
        Vertical_List[0].append(Progression) # Add 1's and 0's to 0th index

    # Creating first 1 index in Vertical_List   
    for a in range(Progression_Type):        
        if Trailer > a:                      # Find if progress value less than a or not. This part run when if True
            Progression = 1                  # Assign Progression to 1
        else:                                # This part run when if False
            Progression = 0                  # Assign Progression to 0
        Vertical_List[1].append(Progression) # Add 1's and 0's to 0th index

    # Creating first 2 index in Vertical_List
    for a in range(Progression_Type):        
        if Retriever > a:                    # Find if progress value less than a or not. This part run when if True
            Progression = 1                  # Assign Progression to 1
        else:                                # This part run when if False
            Progression = 0                  # Assign Progression to 0
        Vertical_List[2].append(Progression) # Add 1's and 0's to 0th index

    # Creating first 3 index in Vertical_List   
    for a in range(Progression_Type):        
        if Exclude > a:                      # Find if progress value less than a or not. This part run when if True
            Progression = 1                  # Assign Progression to 1
        else:                                # This part run when if False
            Progression = 0                  # Assign Progression to 0
        Vertical_List[3].append(Progression) # Add 1's and 0's to 0th index
    
        
    
    for i in range(len(Vertical_List[0])):   # This loop use for print part
        # Get length of Vertical_List list
        # Create a loop using length
        # Print * multiplying by sub list's values
        
        print(" "*5+"*"*Vertical_List[0][i]+" ",end="\t")  # Print fist sub list's indexes, delete last newline charecter
        print(" "*10+"*"*Vertical_List[1][i]+" ",end="\t") # Print second sub list's indexes, delete last newline charecter
        print(" "*8+"*"*Vertical_List[2][i]+" ",end="\t")  # Print third sub list's indexes, delete last newline charecter
        print(" "*5+"*"*Vertical_List[3][i])               # Print forth sub list's indexes


    print("\n")
    print(Progress+Trailer+Retriever+Exclude,"outcomes in total.") # To get the total number of the students records   
    print("-"*75)


#---Main Programe----
# Making loop to input multiple records
# Create boolean variable as Flag
done = True                                # Initialize so that the while loop will execute
while done:
    Int_RList()                            # Calling Function 1
   
    print("\nWould you like to enter another set of data?")
    while True:
        try:
            yqMessage = input("Enter 'y' for yes or 'q' to quit and view results: " )
            if yqMessage.lower() == "q":   # Set done to False if the 'q' string value found. It not be continue the while loop anymore and  it runs the rest of programe(Histogram) and End
                done = False
                break
            elif yqMessage.lower() != "y": # If user input a letter out of "y" and "q", Display the incorrect message and continue the while loop
                print("\t","*"*5,"User input is incorrect","*"*5,"\n")
            else:                          # If user input "y", break the loop and user can input another record
                print("\n")
                print("-"*75)
                break
        except:                            # If user input char values like space then this program works
            print("\t","*"*5,"User input is incorrect","*"*5,"\n")


# ---Calling the Function 3---
Vertical_Histogram()

#---End of Progression---
S = "** Progression Outcome Program - End **"
print("\n")
print("*"*len(S))
print(S)
print("*"*len(S)) 
    
