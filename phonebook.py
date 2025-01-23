#import module
import sys

def initial_phonebook():
    rows,cols =int(input("please enter initial number of cantacts")),5
    phone_book =[]
    print(phone_book)
    
    for i in range(rows):
        print("\nEnter contact %d details in the following order(ONLY): %(I+1)")
        print("NOTE: * indicates mandatory fields ")
        print("**********************************************************")
        temp =[]
        for i in range(cols):
            if i == 0:
                temp.append(str(input("Enter name*: ")))
                if temp[i] =='' or temp[i]=='':
                    sys.exit("Name is mandatory field. process exit due to blank fields")
                    
            if i == 1:
                temp.append(str(input("Enter number*: ")))
                
            if i == 2:
                temp.append(str(input("Enter e-mail address*: ")))
                if temp[i] =='' or temp[i]==' ':
                    temp[i] = None  
            
            if i == 3:
                temp.append(str(input("Enter date of birth*: ")))
                if temp[i] =='' or temp[i]==' ':
                    temp[i] = None          
                
            if i == 4:
                temp.append(str(input("Enter category(family/friends/work/others)*: ")))
                if temp[i] =='' or temp[i]==' ':
                    temp[i] = None      
                
    phone_book.append(temp)
    print(phone_book)
    return phone_book

def menu():
    print("**********************************************************************************************************")
    print("\t\t\tSmartphone directory", flush=False)
    print("************************************************************************************************************")
    print("\You can now perform the following operations on this phonebook\n")
    print("1. Add new Contact")
    print("2. remove existing contact")
    print("3. Delete all contact")
    print("4. serch for a contact")
    print("5.Display all contacts")
    print("6.Exit phonebook")
    Choice = int(input("Please enter your choice"))
    return Choice

def add_contact(pb):
    dip =[]
    for i in range(len(pb(pb[0]))):
        if i == 0:
            dip.append(str(input("Enter your name: ")))
        if i == 1:
            dip.append(str(input("Enter your number")))   
        if i == 2:
            dip.append(str(input("Enter your Email")))
        if i == 3:
            dip.append(str(input("Enter your date of birth")))
        if i == 4:
            dip.append(str(input("Enter category(family/friends/work/others): ")))
            pb.append(dip)
            return pb

def remove_existing(pb):
    query = str(input("Please enter name of contact you wish  remove from phonebook"))
    temp =0
    for i in range(len(pb)):
         if query ==pb[i][[0]]:
             temp+=1
             print(pb.pop(1)) 
    if temp ==0:
        print("Sorry, you have entered invalid query. \nPlease recheck and try it again")
        return pb
initial_phonebook()
menu()
add_contact()
remove_existing()                                  

