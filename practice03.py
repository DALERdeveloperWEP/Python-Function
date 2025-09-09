def is_even(number):
    return number % 2 == 0

def print_even_message(number):

    if is_even(number):
        print(f'{number} juft son')
    else:
        print(f'{number} Toq son')
user_num = int(input('Son kiriting: '))
print_even_message(user_num)