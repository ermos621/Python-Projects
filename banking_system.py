# Banking system using oop

# parents class: user
class User() :
    # holds details about an user 
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    # has a function to show user details     
    def show_user_details(self):
        print ("Personal details ")
        print (" ")
        print ("Name " , self.name)
        print ("Age " , self.age)
        print ("Gender " , self.gender)

# child class : bank
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        # stores details about the account balance
        self.balance = 0 

# allows for deposits withdraw , view_balance 
# stores details about the amount

    def deposit(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : £" , self.balance)


    def withdraw (self , amount):
        self.amount = amount
        if self.amount > self.balance:
            print (" Insufficient funds | balance available : £ " , self.balance)
        else :
            self.balance = self.balance - self.amount
            print("Acount balance has been updated : £ " , self.balance )

    def view_balance (self):
        self.show_user_details()
        print("Acount balance: £ " , self.balance )