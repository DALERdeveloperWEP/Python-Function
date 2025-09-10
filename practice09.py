print("" \
"----------Menyu----------\n" \
"1. Pul qo'shish\n" \
"2. Pul yechish\n" \
"0. balance ko'rish\n")



def deposit(balance, amount):
    return balance + amount
def withdraw(balance, amount):
    return balance - amount
def check_balance(balance):
    return balance

def main():
    user_balance = 100
    while True:
        user_op = input('Menyudan birontasini tanlang: ')
    
        if user_op.isdigit():
            if user_op == '1':
                user_add = int(input("Siz Pul qo'shish tanladingiz\nsuma: "))
                user_balance = deposit(user_balance,user_add)
            elif user_op == '2':
                user_remove = int(input("Siz Pulyechish tanladingiz\nsuma: "))
                user_balance = withdraw(user_balance,user_remove)
            elif user_op == '0':
                print(check_balance(user_balance))
            else:
                print('iltimos faqat menyudagi' \
                ' sonlardan birontasini tanlang!\n')
        else:
            print('Iltimos faqat raqam kiriting!\n')
        
        user_exit = input("Davom etirasizmi? (Ha/Yo'q): ")
        if user_exit =="Yo'q":break

        
main()