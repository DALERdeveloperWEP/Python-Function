secret = 7
guess = int(input('PC secret soni toping: '))

def check_guess(secret_PC, guess_user):
    return secret_PC == guess_user

def print_result(is_correct):

    if is_correct:
        print("To'g'ri")
    else:
        print("Xato")


print_result(check_guess(secret,guess))