def ask_question(question: str, correct_answer: str):
    user_answer = input( question + ": ")

    tekshirish = check_answer(user_answer, correct_answer)

    if tekshirish:
        print("To'g'ri")
    else:
        print("Xato")

def check_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

ask_question("Python qanday tiplangan dasturlash tili?","Dynamically")
ask_question("Pythonda nechta tur funtionlar mabjud?","6")

