def credit(balance,Balance):
    
    Balance=Balance+balance
    print(Balance)
    return Balance
    
    
def debit(balance,Balance):
    
    Balance=Balance-balance
    print(Balance)
    return Balance
    
def check_Balance(Balance):
    print("current Balance : ",Balance)
    
    
    
Balance=0
Balance=credit(200,Balance)
Balance=debit(300,Balance)
check_Balance(Balance)
