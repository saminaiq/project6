# project 6 :Build_compose_and-Decorate_A_complete-Traditonal_oop_project_Series
# instructur:Samina

# Class variable and Class Methods
#Assigment :
# CReate a class bank with  a class variable bank_name .Add a class method change_bank_name(cls, name)that changing the bank nasme. Show that it affects all instancees.




class Bank:
    bank_name = "DefaultBank"
    
    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        
    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Objects
account1 = Bank("Ali")
account2 = Bank("Hamza")

# Display before changing bank name
account1.display()
account2.display()

# Changing bank name
Bank.change_bank_name("Meezan Bank")

# Display after changing bank name
account1.display()
account2.display()
