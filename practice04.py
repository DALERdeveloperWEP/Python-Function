def get_grade(ball):
    if ball <= 100 and ball >= 90:
        return "A"
    elif ball <= 89 and ball >= 80:
        return "B"
    elif ball <= 79 and ball >= 70:
        return "C"
    elif ball <= 69 and ball >= 60:
        return "F"
    else:
        return 'siz ota ololmadingiz'

def main():
    user_ball = int(input('ball kiriting: '))
    grade = get_grade(user_ball)
    print(grade)
    

main()