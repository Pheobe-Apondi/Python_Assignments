class Account:
    def __init__(self,name,min_balance):
        self.name = name
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_limit = 0.5 * self.balance
        self.current_loan = 0
        self.account_frozen = False
        self.loan = 0
        self.min_balance = min_balance

        

    def deposit(self,amount):
        if self.account_Frozen:
            return("You cannot deposit funds into this account. It is currently frozen. Would you like to unfreeze the account?")
        if(amount>0):
            self.deposits.append(amount)
            self.balance = self.get_balance()
            return (f"You have deposited:{amount}, your new balance is {self.get_balance()}")
        else:
            return (f"We only accepts deposits above O shillings,please try to deposit again.")
        



    def withdraw(self,amount):
          if self.account_frozen:
            return("You cannot withdraw funds from this account. It is currently frozen. Would you like to unfreeze the account?")
          elif amount <= 0:
               return("The lowest amount you can withdraw is KES 1")
          elif amount >self.get_balance():
              return (f"You do not qualify for an overdraft. Please input a number within your balance range. Your current balance is{self.get_balance()}")
          elif self.get_balance() - amount <self.min_balance:
            return ("There is a minimum balance restriction in your account. You do not have enough funds in your account to make this withdrawal")
          else:
             self.withdrawals.append(amount)
             return (f"Withdrawal was successful. {amount} was withdrawn. New account balance is {self.get_balance()}")
    


    
    def show_balance(self):
        return self.balance
    

    
    def transfer(self,amount,account):
          if self.account_frozen:
            return("Your account is currently frozen. Would you like to unfreeze the account?")

          elif amount <= 0:
               return("The lowest amount you can transfer is KES 1")
          elif self.get_balance() - amount <self.min_balance:
            return ("There is a minimum balance restriction in your account. You do not have enough funds in your account to make this transfer")

          elif amount > 0 and amount < self.balance:
            self.balance -=amount
            return (f"Transfer was successful: {amount} was transferred to account {account}")
          else:
            transfered_money = self.balance - amount
            self.withdrawals.append(transfered_money)
            return (f"The transfer was successful. {amount} was transfered to {account}.")
          


    def get_balance(self):
        self.balance = sum([num for num in self.deposits]) - sum([num for num in self.withdrawals]) - self.loan
        return self.balance



    def get_loan(self,amount):
        if self.account_frozen:
            return("Your account is currently frozen. Would you like to unfreeze the account?")
        elif amount <= 0:
               return("The loan must be apositive number")
        if amount <= self.loan_limit:
            self.current_loan +=amount
            return (f"Loan appplication successfully: {amount} will be deposited in your account")
        else:
            return("Lan application unsuccessful: Please try a lower amount")
        


        

    def repay_loan(self,amount):
        if amount > 0 and amount == self.current_loan:
            self.current_loan -= amount
            return(f"Your loan payment was successful, you have cleared your loan. You can apply for a new loan. ")
        elif amount > 0 and amount <self.current_loan:
            self.current_loan -=amount
            return (f"Your loan payment was successful,your new loan balance is {self.current_loan}")
        else:
            return (f"We only accepts amounts above O shillings,please try again.")   




        
    def account_details(self):         
       
        return (f"Hello {self.name}.Here is your current balance {self.get_balance()} We are happy to have you here and welcome any feedback.")
    

    def change_account_owner(self,owner):
        self.name = owner
        return (f"Account owner changed to {self.name}")
    



    def  account_statement(self):
         total_deposits = 0
         total_withdrawals = 0
         print(f"Hello {self.name}.Here is your account statement.")
         for deposit in self.deposits:
             total_deposits  += deposit
             print(f"Deposits: {total_deposits}")
         for withdrawal in self.withdrawals:
             total_withdrawals +=withdrawal
             print (f"Withdrawals: {total_withdrawals}")
         print(f"Outstanding Loan:{self.loan}")
         print(f"Current balance:{self.get_balance()}")
 



    def apply_interest(self):
        if self.account_frozen:
            return "Your account is currently frozen"
        else:
            interest = self.get_balance() * 0.05
            self.deposits.append(interest)
            return f"Interest of {interest} applied to your funds. New balance is {self.get_balance()}"
     
        
    def freeze_account(self):
         self.account_frozen = True
         return f"{self.name},your account has been frozen."
    
    
    def unfreeze_account(self):
        self.account_frozen = False
        return f"{self.name},your account has been unfrozen."
             

    def set_min_balance(self,amount):
        self.min_balance = amount
        return f"Minimum balance has been set to {self.min_balance}"
    

    def close_account(self):
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        withdraw = self.get_balance ()
        self.balance -= withdraw
        return  f"{self.name}. Your account has been closed. {withdraw} shillings has been withdrawn from your account. All balances and transactions have been reset."





