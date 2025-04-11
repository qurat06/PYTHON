def credit(balance,transaction,amount):
    
    balance=balance+amount
    transaction.append(amount)
    return balance,transaction
    
    
def debit(balance,transaction,amount):
    if balance<amount:
        print=int(input("Insufficient amount"))
    balance-=amount
    transaction.append(amount)
    return balance,transaction
    
def check_balance(balance):
    print("current Balance : ",balance)
    
def show_transaction(transaction):
    print("transaction",transaction)
    
    
    
    
    
balance=0
transaction=[]

while(True):
    print("credit")
    print("debit")
    print("check balance")
    print("tansaction are")
    choice=int(input("enter choice "))
    if choice==1:
        amount=int(input("enter the amount to be credited "))
        balance,transaction=credit(balance,transaction,amount)
    elif choice==2:
        amount=int(input("enter the amount to be debited "))
        balance,transaction=debit(balance,transaction,amount)
    elif choice==3:
        check_balance(balance)
    else:
        show_transaction(transaction)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
