import json
import csv
import random
import time
f = open("booksset1.json",'r+', encoding ='utf-8')
f_3 = open('FakeNameSet20.csv', 'r+')
f_2 = open('loanitems.json','r+')

data = json.load(f)
data_2 = json.load(f_2)
data_3 = csv.reader(f_3)






length = len(data)

def create_isbn():
        isbn = ''
        for y in range(0,6):
            isbn += str(random.randint(0,10))
        return int(isbn)

def add_isbn():
    for book in data:
        book.update({'isbn': create_isbn()})
    with open('booksset1.json', 'w') as f:
        json.dump(data,f, indent= 2)
try:
    if data[0]['isbn'] != type(int) or type(str):
        add_isbn()
except KeyError:
    add_isbn()


 
class Person:
    def __init__(self, number, gender, name_set, given_name, surname, street_address, zip_code, city, email_address, username, telephone_number):
        self.number = number
        self.gender = gender
        self.name_set = name_set
        self.given_name = given_name
        self.surname = surname
        self.street_address = street_address
        self.zip_code = zip_code
        self.city = city
        self.email_address = email_address
        self.username = username
        self.telephone_number = telephone_number
    
    def showDetials(self):
        print('{} {} (ID: {})'.format(self.given_name, self.surname, self.number))
        print('Username: {}'.format(self.username))
        print('Gender: {}'.format(self.gender))
        print('Name set: {}'.format(self.name_set))
        print('Address: {}, {}'.format(self.street_address, self.zip_code))
        print('City: {}'.format(self.city))
        print('E-mail address: {}'.format(self.email_address))
        print('Telephone number: {}  \n'.format(self.telephone_number))

    def showNumber(self):
        return self.number
    
    def showGender(self):
        return self.gender
    
    def showNameSet(self):
        return self.name_set
    
    def showGivenName(self):
        return self.given_name
    
    def showSurname(self):
        return self.surname
    
    def showStreetAddress(self):
        return self.street_address
    
    def showZipCode(self):
        return self.zip_code
    
    def showCity(self):
        return self.city
    
    def showEmailAddress(self):
        return self.email_address
    
    def showUsername(self):
        return self.username
    
    def showTelephoneNumber(self):
        return self.telephone_number










class Librarian(Person):
    
    def __init__(self, number, gender, name_set, given_name, surname, street_address, zip_code, city, email_address, username, telephone_number):
         super().__init__(number, gender, name_set, given_name, surname, street_address, zip_code, city, email_address, username, telephone_number)
    
    def checkempty(self,lines):
        if lines == []:
            return False
        else:
            return True

   
    def addCostumer(self,Number, Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, Username, TelephoneNumber):

        costumerList().costumers.append(Costumer(Number, Gender, NameSet, GivenName, Surname, StreetAddress, ZipCode, City, EmailAddress, Username, TelephoneNumber))
    

    
    def addBook(self, author, country, imagelink, language, link, pages, title, year,isbn):

        Catalog().books.append(Book(author, country, imagelink, language, link, int(pages), title, int(year),int(isbn)))


        
        
   
            
    
    def loanBook(self,id, number = None,):
        costumer_1 = None
        numbooks = 0
        numcost = 0
        for costumer in costumerList().costumers:
            numcost += 1   
            if costumer.number == id:
                costumer_1 = costumer
                break

        if numcost + 1 > len(costumerList().costumers):
            time.sleep(0.5)
            print("costumer does not exist")

                
        for book in Catalog().books:
                numbooks += 1
                if book.showIsbn() == number:
                    
                    loanAdministration().AddBook(book)
                    print("book {} lent to {} with id {}".format(book.showTitle(),costumer_1.given_name,costumer_1.showNumber()))
                    break
                    
            
        if numbooks + 1 > len(Catalog().books):
            time.sleep(0.5)
            print("book does not exist")

        
                   
                
        
       

                   
    
 

    def searchBook(self, number = None, title = None):

        x = 0

        for book in Catalog().books:
            x += 1
            if book.showIsbn() == number or book.showTitle() == title or book.showIsbn() == str(number):
                book.showAll()

                
                break

        if x >  len(Catalog().books):
            print('book does not exist')
                
       
       




class Costumer(Person):
    def __init__(self, number, gender, name_set, given_name, surname, street_address, zip_code, city, email_address, username, telephone_number, ):
        
        super().__init__(number, gender, name_set, given_name, surname, street_address, zip_code, city, email_address, username, telephone_number)
    
    def searchBook(self, number = None, title = None):

        x = 0

        for book in Catalog().books:
            x += 1
            if book.showIsbn() == number or book.showTitle() == title or book.showIsbn() == str(number):
                book.showAll()

                
                break

        if x >= len(Catalog().books):
            time.sleep(0.5)
            print('book does not exist')
                
    
    
   
    












class costumerList:
    def __init__(self, costumers=[]):
        self.costumers = costumers
    
    def loadInCustomers(self):
        with open('FakeNameSet20.csv', 'r') as customerNames:
            reader = csv.reader(customerNames)
            counter = 0
            
            for row in reader:
                if counter == 0:
                    counter += 1
                    continue
                try:

                    self.costumers.append(Costumer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))
                except IndexError:
                    pass
    def listAllCustomers(self):
        for costumer in self.costumers:
            costumer.showDetials()



class Book:
    def __init__(self, author, country, imagelink, language, link, pages, title, year,isbn):
        self.author       = author
        self.country      = country
        self.imagelink   = imagelink
        self.language     = language
        self.link         = link
        self.pages        = pages
        self.title        = title
        self.year         = year
        self.isbn           = isbn
    
    def showAll(self):
        print(('Title: {}'.format(self.title,)))
        print('Author: {}'.format(self.author))
        print('Language: {}'.format(self.language))
        print('Year: {}'.format(str(self.year)))
        print('Country: {}'.format(self.country))
        print('Pages: {}'.format(str(self.pages)))
        print('Link: {}'.format(self.link))
        print('Image link: {}'.format(self.imagelink))
        print('isbn: {} \n'.format(self.isbn))
    
    def showAuthor(self):
        return self.author
    
    def showLanguage(self):
        return self.language
    
    def showYear(self):
        return self.year
    
    def showCountry(self):
        return self.country
    
    def showPages(self):
        return self.pages
    
    def showTitle(self):
        return self.title
    
    def showLink(self):
        return self.link
    
    def showImageLink(self):
        return self.imagelink

    def showIsbn(self):
        return self.isbn



 
class loanAdministration:
    def __init__(self, books=[]):
        self.books = books

    def AddBook(self,book):
        self.books.append(book)
    
    def loadBooks(self):
        if len(data_2) == 0:
            print("There are no loan books yet")
        else:
            try:
                for book in data_2:
                    book_item = Book(book['author'], book['country'], book['imagelink'], book['language'], book['link'], book['pages'], book['title'], book['year'], book['isbn'])
                    self.books.append(book_item)
            except AttributeError:
                pass


    
    def showLoanBooks(self):
        if len(self.books) == 0:
            print("\n")
            print("No books are lent ")
        else:
            for book in self.books:
                book.showAll()





class Catalog:
    def __init__(self, books=[]):
        self.books = books
    
    def loadBooks(self):
        try:

            for book in data:
                book_item = Book(book['author'], book['country'], book['imageLink'], book['language'], book['link'], book['pages'], book['title'], book['year'], book['isbn'])
                self.books.append(book_item)
        except AttributeError:
            pass

    
    def showAvialbleBooks(self):
        for book in self.books:
            book.showAll()





catalog = Catalog()
catalog.loadBooks()
cos = costumerList()
cos.loadInCustomers()
loan = loanAdministration()
loan.loadBooks()
lib = Librarian("ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad")
costumer = Costumer("ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad","ahmad")
