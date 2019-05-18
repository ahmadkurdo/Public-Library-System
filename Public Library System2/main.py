from classes import *
import sys
import time


costumer_script = False
librarian_script = False
wrong_command = False
choose_user = input("Please choose 1 if you are a costumer or 2 if you are the librarian ")


if choose_user not in '12':
    wrong_command = True

while wrong_command:
    print("please choose 1 or 2 \n")
    choose_user = input("Please choose 1 if you are a costumer or 2 if you are the librarian ")

    if choose_user == '1' or choose_user == '2':
        wrong_command = False


if choose_user == '2':
    librarian_script = True

elif choose_user == '1':
    costumer_script = True





def screen_librarian():
    print("\n")
    print("*"*120)
    print ("\t \t \t \t \t  WELCOME TO ROTTERDAM LIBRARY \t \t \t \n")
    print("\n")
    print("\t \t \t \t \t  press 1 to show all books \n")
    print("\t \t \t \t \t  press 2 to add a book \n")
    print("\t \t \t \t \t  press 3 to search for a book\n")
    print("\t \t \t \t \t  press 4 loan a book \n")
    print("\t \t \t \t \t  press 5 to add a costumer \n")
    print("\t \t \t \t \t  press 6 to show books in loan \n")
    print("\t \t \t \t \t  press 7 to show all costumers \n")
    print("\t \t \t \t \t  press 8 to save and quit\n")
    print("*"*120)
    print("\n") 
    
def screen_costumer():
    print("\n")
    print("*"*120)
    print ("\t \t \t \t \t  WELCOME TO ROTTERDAM LIBRARY \t \t \t \n")
    print("\n")
    print("\t \t \t \t \t  press 1 to show all books \n")
    print("\t \t \t \t \t  press 2 to search for a book\n")
    print("\t \t \t \t \t  press 3 to quit \n")
    print("*"*120)
    print("\n")

    


while librarian_script :
    time.sleep(0.5)
    screen_librarian()
    command = input("\t \t \t \t \t  PLEASE CHOOSE A COMMAND   \n")


    if command not in "12345678":
        time.sleep(0.5)
        print("\n")
        print("PLEASE CHOOSE A VALID COMMAND")

    if command == '1':
        Catalog().showAvialbleBooks()

    elif command == '2':

        while True:
            try:

                author = input("please enter the author's name \n")
                country = input("please enter the country's name \n")
                imagelink = input("please enter the imagelink \n")
                language = input("please enter the language \n")
                link = input("please enter the link \n")
                pages = input("please enter the pages \n")
                title = input("please enter the title \n")
                year = input("please enter the year \n")
                isbn = input("enter the isbn \n")
                lib.addBook(author, country, imagelink, language, link, int(pages), title, int(year),int(isbn))        
            except ValueError:
                time.sleep(0.5)
                print(" please make sure you use numbers for pages, year and isbn")
                print("\n")
                time.sleep(0.5)
            else:
                break
    
    
    elif command == '3':

        print("Press 1 to search by isbn \n")
        print("Press 2 ro search by name \n")
        print("Press 3 to search by both \n")
        command_2 = input("Please choose a command  ")

        if command_2 == '1':

            while True:
                try:    
                    isbn = input("please enter the isbn  \n")
                    lib.searchBook(number = int(isbn))

                except ValueError:
                    time.sleep(0.5)
                    print("Please choose a valid input")
                    print("\n")
                    time.sleep(0.5)
                else:
                    break

        elif command_2 == '2':

            while True:
                try:


                    name = input("Please enter the name  \n")
                    lib.searchBook(title = str(name))
                except ValueError:
                    time.sleep(0.5)
                    print("Please choose a valid input")
                    print("\n")
                    time.sleep(0.5)

                else:
                    break
        elif command_2 == '3':

            while True:
                try:

                    name = input("Please enter the name  \n")
                    isbn = input("Please enter the isbn  \n")
                    lib.searchBook(title = str(name), number = int(isbn) )
                except ValueError:
                    time.sleep(0.5)
                    print("Please choose a valid input, make sure you choose a number for the isbn")
                    time.sleep(0.5)
                else:
                    break
    
    
    elif command == '4':
        while True:
            try:

                idcos = input("Please enter the costumer id")
                isbn = input("Please enter the books isbn")
                lib.loanBook(id = str(idcos), number = int(isbn))
            except ValueError:
                print("Please choose a valid number")
            else:
                break
    
    
    
    
    
    
    elif command == '5':
        row = []
        Number = input("please enter the costumer id \n")
        Gender = input("please enter the costumer gender \n")
        NameSet= input("please enter the costumer nameset \n")
        GivenName = input("please enter the costumer given name \n")
        Surname = input("please enter the costumer surname \n")
        StreetAddress = input("please enter the costumer streetaddress \n")
        ZipCode = input("please enter the costumer zipcode \n")
        City = input("please enter the costumer city \n")
        EmailAddress = input("enter the costumer emailaddress \n")
        Username = input("enter the costumer username \n")
        TelephoneNumber= input("enter the costumer phonenumber \n")
        row.extend([Number, Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, Username, TelephoneNumber])

        lib.addCostumer(Number, Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, Username, TelephoneNumber)

        with open('FakeNameSet20.csv', 'a') as csvFile:
            
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()

    
    
    elif command == '6':
        loan.showLoanBooks()

    
    elif command == '7':
        cos.listAllCustomers()
    
    
    
    elif command == '8':
        data.clear()
        for x in range (0,len(Catalog().books)):
            data.append(Catalog().books[x].__dict__)
        with open('booksset1.json','w') as f:
            json.dump(data, f, indent=2)
        
        data_2.clear()
        for x in range(0,len(loanAdministration().books)):
            data_2.append(catalog.books[x].__dict__)
        with open('loanitems.json','w') as f:
            json.dump(data_2, f, indent=2)
        librarian_script = False
        time.sleep(0.5)
        print("CHALAAAAZZZZZZZZZ!!!!")
        time.sleep(1)

while costumer_script:
    screen_costumer()
    command = input("\t \t \t \t \t  PLEASE CHOOSE A COMMAND   \n")


    if command not in "12":
        print("PLEASE CHOOSE A VALID COMMAND")
    
    if command == '1':
        Catalog().showAvialbleBooks()


    elif command == '2':

        print("press 1 to search by isbn")
        print("press 2 ro search by name")
        print("press 3 to search by both ")
        print("\n")
        command_2 = input("please choose a command  ")

        if command_2 == '1':

            while True:
                try:    
                    isbn = input("please enter the isbn  \n")
                    costumer.searchBook(number = int(isbn))

                except ValueError:
                    time.sleep(0.5)
                    print("please choose a valid input")
                    time.sleep(0.5)
                else:
                    break
        elif command_2 == '2':


            while True:
                try:


                    name = input("please enter the name  \n")
                    lib.searchBook(title = str(name))
                except ValueError:
                    time.sleep(0.5)
                    print("please choose a valid input")
                    time.sleep(0.5)
                else:
                    break
        
        
        
        elif command_2 == '3':

            while True:
                try:


                    name = input("please enter the name  \n")
                    isbn = input("please enter the isbn  \n")
                    lib.searchBook(title = str(name), number = int(isbn) )
                except ValueError:
                    time.sleep(0.5)
                    print("please choose a valid input")
                    time.sleep(0.5)
                else:
                    break
    
    elif command == '3':
        time.sleep(0.5)
        costumer_script = False
    


