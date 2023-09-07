#N01445323 - Bethany Innes

from random import randint

#credit card class
class CreditCard():
    
    #dictionary for card types
    #card_dict = {1:"Visa", 2:"Master", 3:"Amex", 4:"Discover"}
    credit_limit = 1000
    
    #initializing method for credit card object
    def __init__(self, card_num, name, expiration):
        self.name = name
        self.card_num = card_num
        self.expiration = expiration
        self.balance = randint(0, 1000) 
        self.card_dict = {1:"Visa", 2:"Master", 3:"Amex", 4:"Discover"}
        self.card_type = self.get_cardType()
       
    
    #getter method for name   
    def get_cardOwner(self):
        return self.name
    
    #getter method for card type, based on dictionary
    def get_cardType(self):
        
        #executed if its a valid key at index 5
        if int(self.card_num[5]) > 0 and int(self.card_num[5]) < 5:
            #type = self.card_num[5]
            self.card_type = self.card_dict[int(self.card_num[5])]
        #executed if its an invalid key at index 5
        else:
            self.card_type = "Not Supported Card Type"
        return self.card_type
    
        
    #determines whether they have enough room to make the transaction
    def processOrder(self, transaction_price):
        
        if self.card_type != "Not Supported Card Type":
        #executes if they have enough room
            if (self.credit_limit -self.balance) >= transaction_price:
                self.balance = self.balance + transaction_price
                return True
        #executes if they cannot make the transaction
            else:
                return False
    
    #returns string representation of the object    
    def __str__(self):
        return f"{self.name} is the owner of the credit card with number {self.card_num} which expires on {self.expiration}."
    