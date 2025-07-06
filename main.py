from file_manager import read, append
import os

FILENAME = "users" 

def show_menu():
    print("""
        ╔═══════════════════════════════╗
        ║           AUTH MENU           ║
        ╠═══════════════════════════════╣
        ║   1. Ma'lumot qo'shish        ║
        ║   2. Ma'lumotlarni ko'rish    ║
        ║   3. Chiqish                  ║
        ╚═══════════════════════════════╝
        """)


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

def main():

    while True:
        show_menu()
        choice = input("Tanlovingiz (1-3): ").strip()
        if choice == '1':
            add_user()
        elif choice == '2':
            view_users()
        elif choice == '3':
            print("Dastur yakunlandi.")
            break
        else:
            print("Qayta urinib ko'ring ❌")

if __name__ == "__main__":
    main()
