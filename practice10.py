user_password = input('password: ')
parametir = len(user_password) > 8

def is_strong_password(password: str):
    if password:
        print('Kuchli parol')
    else:
        print('Kuchsiz parol') 

is_strong_password(parametir)