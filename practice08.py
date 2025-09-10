print("" \
"----------Menyu----------\n" \
"1. Celsius → Fahrenheit\n" \
"2. Fahrenheit → Celsius\n" \
"0. Exit programing\n")

def c_to_f(celsius):
    return celsius * 9/5 + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
     
    while True:
        user_op = input('Menyudan birontasini tanlang: ')
    
        if user_op.isdigit():
            if user_op == '1':
                user_celsius = int(input('Siz Celsiusdan Fahrenheitga' \
                ' otkazishni tanladingiz: '))
                print(c_to_f(user_celsius))
            elif user_op == '2':
                user_fahrenheit = int(input('Siz Fahrenheitdan Celsiusga' \
                ' otkazishni tanladingiz: '))
                print(f_to_c(user_fahrenheit))
            elif user_op == '0':
                print('Siz Chiqishni tanladingiz')
                break
            else:
                print('iltimos faqat menyudagi' \
                ' sonlardan birontasini tanlang!\n')
        else:
            print('Iltimos faqat raqam kiriting!\n')


main()