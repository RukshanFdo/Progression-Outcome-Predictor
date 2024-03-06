# 4COSC006C     : Software Development I - Coursework Specification (2020/21)
# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution

# Module Leader :   Saman Hettiarachchi
# Student ID    :   1809821
# IIT ID        :   2019784
# Date          :   December 11th 2020

# Part 5 - Alternative Staff Version (optional exetension)

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


# Function 1           
#---To execute the Progresion Outcome---

def TotalAndOutcome_Prog():
    global Progress,Trailer,Exclude,Retriever
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
        
    


# Function 2
#---To create the Horizontal Histogram---
def Horizontal_Histogram():
    print("\n")
    print("-"*50)
    print("Horizontal Histogram\n")
    print("Progress ",Progress,":", "*"*Progress)                    # Total output of "Progress"
    print("Trailer  ",Trailer,":", "*"*Trailer)                      # Total output of "Trailer"
    print("Retriever",Retriever,":", "*"*Retriever)                  # Total output of "Retriver"
    print("Exclude  ",Exclude,":", "*"*Exclude,"\n")                 # Total output of "Exclude"
    print((Progress+Trailer+Exclude+Retriever),"outcomes in total.") # To get the total number of the students records
    print("-"*50)




#---Main Programe----
# Create the all Progression outcomes List

Outcomes_List = [[120,0,0],[100,20,0],[100,0,20],[80,20,20],[60,40,20],[40,40,40],[20,40,60],[20,20,80],[20,0,100],[0,0,120]]

for i in range (0,10):                # Use for loop to call Liist Data (Progression outcomes)
    Pass  = Outcomes_List[i][0]       # 0 index for Pass value 
    Defer = Outcomes_List[i][1]       # 1 index for Defer value
    Fail  = Outcomes_List[i][2]       # 2 index for Fail value

    # Calling the Function 1
    TotalAndOutcome_Prog()

# Calling the Function 2    
Horizontal_Histogram()

    
#---End of Progression---
S = "** Progression Outcome Program - End **"
print("\n")
print("*"*len(S))
print(S)
print("*"*len(S))              
                


            
                
                





