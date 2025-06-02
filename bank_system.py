from datetime import datetime

class Transaction:
    def __init__(self,narration,amount,transaction_type):
        self.date_time =datetime.now()
        self.narration = narration
        self.amount = amount
        self.transaction_type= transaction_type
        

    
    def __str__(self):
        return f"Date: {self.date_time}\n Transaction type: {self.transaction_type}\nNarration: {self.narration}\nAmount: {self.amount}"


class Account:
    def __init__(self,owner,account_number):
        self._owner = owner
        self._account_number = account_number
        self._transactions = []
        self._is_closed = False
        self.is_Frozen = False
        self._loan_balance = 0.0
        self._minimum_balance = 0.0

    def __check_account_status(self):
        if self._is_closed:
            return ("Account is closed")
        if  self.is_Frozen :
            return("Account is frozen")
        
    def _validate_amount(self,amount):
        if amount <=0:
            return("Amount must be greater than zero")
        

    def _validate_withdrawal(self,amount):
        self._validate_amount(amount)
        if self.get_balance() - amount <self._minimum_balance:
            return f"Withdrawal cannot be made: Minimum balance requirement not met. Your accout balance is {self.get_balance()}, your minimum balance is {self._minimum_balance}"



    def get_balance(self):

        balance = 0
        for transaction in self._transactions:
                if transaction.transaction_type in ['Deposits made','Transfer In','Loan']:
                  balance += transaction.amount
                elif transaction.transaction_type in ['Withdrawals','Transfer Out','Loan repayment']:
                    balance-=transaction.amount
        
        return  balance
    
       
    def deposit (self,amount):
        self.__check_account_status()
        self._validate_amount(amount)
        self._transactions.append(Transaction("Deposits made",amount,"deposit"))
        return f"Deposit successful. New account balance: {self.get_balance()}"
    



    def withdraw(self,amount):
        self.__check_account_status()
        self._validate_withdrawal(amount)
        self._transactions.append(Transaction("Withdrawal", amount,"withdrawal"))
        return f"Withdrawal successful. New account balance:{self.get_balance()}"
    

    
    def transfer_funds(self,amount,account):
        self.__check_account_status()
        self._validate_withdrawal(amount)
        if not isinstance(account,Account):
            return "Account does not exist"
        if self.get_balance() < amount:
            return "You do not have enough funds in your account to make this transfer"
        self._transactions.append(Transaction("Transfer In",amount,f"transfer made to {account.owner}"))
        account._transactions.append(Transaction("Transfer Out",amount,f"transfer from {self._owner}"))
        return f"Transferred {amount} to {account._owner}.Your new balance {self.get_balance()}"
    

    
    def request_loan(self,amount):
        self.__check_account_status()
        self._validate_amount(amount)
        loan_limit = 0.02 * self.get_balance()
        if amount > loan_limit:
            return f"Loan denied: You can only borrow upto {loan_limit}"
        else:
            self._loan_balance+= amount

            self._transactions.append(Transaction("Loan",amount,"Loan"))
            return (f"Loan appplication successfull. Current loan balance is {self._loan_balance}")



  

    def repay_loan(self,amount):
         self.__check_account_status()
         self._validate_amount(amount)
         if amount >self._loan_balance:
             return "Amount entered exceeds your loan balance"
         else:
              self._loan_balance -= amount
              self._transactions.append(Transaction("Loan repayment",amount,"loan repayment"))
         return f"Loan repayment of {amount} was successful. Remaining loan is {self._loan_balance - amount}"



    def view_account_details(self):
        return f"Account Owner: {self._owner}\nAccount Number:{self._account_number}\nBalance:{self.get_balance()}"
    

  
   
    
    def change_account_owner(self,new_owner):
        self.__check_account_status()
        self._owner = new_owner
        return f"Account owner updated to {self._owner}"
    

    def account_statement(self):
        self.__check_account_status()
        for transaction in self._transactions:
            print(transaction)



    def calculate_interest(self):
        self.__check_account_status()
        interest = self.get_balance() * 0.05
        self._transactions.append(Transaction("Interest credited", interest,"interest"))
        return f"Your account interest is {interest}. It has been added to your account. Your new account balance is {self.get_balance()}"
    



    def freeze_account(self):
        self.is_Frozen = True
        return "Account has been frozen"
    
    
    def unfreeze_account(self):
        self.is_Frozen = False
        return "Account has been unfrozen"
    
    
    def set_minimum_balance(self,amount):
        self._minimum_balance = amount
        return f"Minimum blaance set to {self._minimum_balance}"
    
    
    def close_account(self):
        self._is_closed = True
        self._transactions.clear()
        self._loan_balance = 0.0
        return f"Account closed and all balances cleared"
    







          
    


