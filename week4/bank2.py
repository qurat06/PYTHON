def credit(balance,Balance,transaction):
    
    Balance=Balance+balance
    print(Balance)
    return Balance
    
    
def debit(balance,Balance,transaction):
    
    Balance=Balance-balance
    print(Balance)
    return Balance
    
def check_Balance(Balance):
    print("current Balance : ",Balance)
    
def transaction(transaction):
    print("Transaction History")
    for i in transaction:
            print(i)
        
        
Balance=0
transaction=[]
Balance=credit(200,Balance,transaction)
Balance=debit(300,Balance,transaction)
Balance=credit(2000,Balance,transaction)
Balance=credit(200,Balance,transaction)
check_Balance(Balance)
