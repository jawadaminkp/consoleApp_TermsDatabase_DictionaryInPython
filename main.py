

termsAndDef={}


print("Terms Database | Console App")
print("_______________________________")
print("Enter 1 to display all the terms stored")
print("Press 2 to look up for a definition")
print("Enter 3 to add a new term to database")
print("Enter 4 to exit the application")




newTerm=""   
newDef=""
    
   
choice=int(input("Enter your choice:"))

while choice <4:
 
    if choice == 1:
        print("following are all the terms")
        print("_______________________________")
        
        i=1
        for state in termsAndDef:
            print(i,":",state)
            i+=1
            
    elif choice ==2:
        term=str(input("Type a term from TERMS DISPLAY"))
        
        for k in termsAndDef.keys:
            if term == k:
                print(termsAndDef[term])
            else:
                print("Sorry Term is not in the database")
                
                break
        
    elif choice ==3:
        
        newTerm=str(input("Enter Term:"))
        newDef=str(input("Enter your Defintion:"))
        
        termsAndDef[newTerm]=newDef
        
        print("Term added successfully")
        
    
    choice=int(input("Enter your choice:"))
    
print("Program Terminated")
print("Happy Coding")

print("Console App developed by: @javadaminkp")

