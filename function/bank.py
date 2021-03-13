# 계좌 생성
def open_account ():
    print("새로운 계좌가 생성되었습니다.")
#open_account()

# 입금
def deposit(balance, money):
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance+money))
    return balance + money

# 출금
def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance-money))
        return balance - money
    else:
        print("츨금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 # 수수료
    return commission, balance - money - commission # 튜플 형태 (두개의 값을 ,로 나눔)
    

balance = 0 # 잔액
balance = deposit(balance,1000) # deposit 함수를 호출하면서 0, 1000 인수로
#balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))