questions_list=["How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"]
option_of_list=[["Four", "Nine", "Seven", "Eight"],["Chandigarh", "Bhopal", "Chennai", "Delhi"],["Software Engineering", "Counseling", "Tourism", "Agriculture"]]
solution_list=[3,4,1]
help_list=[[3,4],[1,4],[1,2]]
i=0
lifeline=0
while(i<len(questions_list)):
    print("apka question hai?")
    print()
    print(questions_list[i])
    j=0
    print("apka option hai?")
    while (j<len(option_of_list[i])):
        print(j+1,option_of_list[i][j])
        j=j+1
    solution=(input("Enter the answer/lifeline5050:-"))
    if(solution=="lifeline5050"): 
        if (lifeline== 0):
            print(help_list[i])  
            check=int(input("enter the answer:-"))
            if(check==(solution_list[i])):
                print("Congrats! Aapka answer sahi hai")
                lifeline=lifeline+1
                
            else:
                print("Sadly aapka javab galat hai.")
                break
        else:
            print("You allready use your lifeline")
            user=int(input("enter your correct answer:- "))
            d=solution_list[i]
            if(user==d):
                print("Congrats! Aapka answer sahi hai")
            else:
                print("Sadly aapka javab galat hai.")
                break
    elif(int(solution)==(solution_list[i])):
        print("Congrats! Aapka answer sahi hai")
    else:
        print("Sadly aapka javab galat hai.")
        break
    i=i+1