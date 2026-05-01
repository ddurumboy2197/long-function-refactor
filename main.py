def get_user_input():
    return input("Ismingizni kiriting: ")

def get_user_age():
    while True:
        try:
            return int(input("Yoshingizni kiriting: "))
        except ValueError:
            print("Iltimos, to'g'ri yoshni kiriting.")

def calculate_birthday():
    current_year = 2024
    user_age = get_user_age()
    user_birthday_year = current_year - user_age
    return user_birthday_year

def get_user_birthday():
    user_birthday_year = calculate_birthday()
    return user_birthday_year

def get_user_favorite_color():
    return input("Sevimli rangingizni kiriting: ")

def get_user_favorite_food():
    return input("Sevimli ovqatingizni kiriting: ")

def get_user_hobbies():
    return input("Sevimli mashg'ulotingizni kiriting: ")

def get_user_info():
    user_name = get_user_input()
    user_birthday = get_user_birthday()
    user_color = get_user_favorite_color()
    user_food = get_user_favorite_food()
    user_hobbies = get_user_hobbies()
    return {
        "ism": user_name,
        "tug'ilgan_yili": user_birthday,
        "sevimli_rang": user_color,
        "sevimli_ovqat": user_food,
        "sevimli_mashg'ulot": user_hobbies
    }

def main():
    user_info = get_user_info()
    print("Foydalanuvchi ma'lumotlari:")
    for key, value in user_info.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
