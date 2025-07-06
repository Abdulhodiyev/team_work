from function import add_user, view_users
import os


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
