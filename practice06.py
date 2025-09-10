def is_valid_phone_number(phone: str):
    return phone.isdigit() and len(phone) == 9

print(is_valid_phone_number('990621632'))