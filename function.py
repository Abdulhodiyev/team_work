from file_manager import read, writerows, append

FILENAME = "users" 

def add_user():
    name = input("Ismingizni kiriting: ").strip()
    age = input("Yoshingizni kiriting: ").strip()
    append(FILENAME, [name, age])
    print("Ma'lumot muvaffaqiyatli saqlandi ✅")

def view_users():
    users = read(FILENAME)
    if not users:
        print("Ma'lumot topilmadi")
        return
    print("Foydalanuvchilar ro'yxati:")
    
    for i, user in enumerate(users, 1):
        print(f"{i}. Ism: {user[0]}, Yosh: {user[1]}")
    print()

