from datetime import date

def calculate_age(birth_year):
    current_year = date.today()
    return current_year.year - birth_year

user_birth_year = int(input('Birth Year: '))
print(f"{calculate_age(user_birth_year)} Sizning Yoshingiz,\n\
Siz balog‘atga {'yetgansiz' if user_birth_year >= 18 else 'yetmagansiz'}")

