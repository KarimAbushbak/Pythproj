import random
import datetime

class Client():

    def __init__(self, full_name,age,id_no,phone_number):
        self. id = random.randint(1, 100)
        self.full_name=full_name
        self.age=age
        self.id_no=id_no
        self.phone_number=phone_number
    def display(self):
       return {"Id":self.id
           ,"Full name":self.full_name,
         "Age":self.age,
         "Id_No":self.id_no,
         "Phone Nubmer":self.phone_number }

class librarian(Client):
    def __init__(self, id, full_name, age, id_no, phone_number,salary=0.0):
        super().__init__(id, full_name, age, id_no, phone_number)
        self.salary=salary
       



class book:


  def __init__(self,title , description, author):
      self.id=random.randint(0,100)
      self.title=title
      self.description=description
      self.author=author
      self.activity= "Active"


  def display(self):
      return {
          "Book id":self.id
          ,"Book title":self.title,
          "Author":self.author,
          "Description":self.description
          ,"Book status":self.activity

      }
class borrweing_order:


    def __init__(self,clinet_id,book_id,time):
        self.clinet_id=clinet_id
        self.book_id=book_id
        self.time=time
        self.start_date= datetime.date.today()
        self.end_date=datetime.date.today()+datetime.timedelta(self.time)
        if(datetime.date.today()<=self.end_date):
            self.status="Active"
        else:self.status="Expired"


    def display(self):
     return {
        "Clinet id ": self.clinet_id,
        "Book id ": self.book_id,
        "Start date": self.start_date,
        "End date": datetime.date.today() + datetime.timedelta(self.time)
        , "Staus": self.status
    }



clients=[]
books=[]
borrwed_orders=[]
librarians=[]
total_avalible_books=0
total_borrowed_orders=0

n=int(input('''
Please Enter the number of the transaction you would like to make:

1-Sign up as a new client 

2-Sign up a new book

3-Borrow a book

4-Sign up as a librarian 

5-Exit

Please enter the number of you transaction : 
'''))

if n==1 :
    e=int(input("Please Enter the number of clinets you would like to sign :"))
    for i in range(0,e):
        clients.append(Client(input("Enter full name :"), int(input("Enter your age:")), int(input("Enter your id: ")),
                              int(input("Enter your phone number: "))))


    for s in clients:
        print((s.display()))

elif n==2 :
    e=int(input("Please enter the number of books you would like to sign : "))
    for i in range(0,e):
        books.append(book(input("Please Enter book title : "), input("Please enter book description : "),
                          input("Please Enter book author: ")))

    for s in books:
        print((s.display()))
elif n==3 :
    e=int(input("Please enter the number of books you would like to borrow : "))
    for i in range(0, e):
        borrwed_orders.append(borrweing_order(input("Enter the clinet id : "), input("Enter the book id : "), int(input(
            "Enter the amount of days you would like to borrow this book : "))))
    for s in borrwed_orders:
        print(s.display())
elif n==4 :
    e=int(input(("Please enter the number of librarin you would like to sign :")))
    for i in range(0,e):
        librarians.append(librarian(input("Please enter your id :"),input("Please enter your full name :"),input("Please enter your age :"),input("Please enter your id no :"),input("Please enter your phone number "),input("Please enter your salary :")))
