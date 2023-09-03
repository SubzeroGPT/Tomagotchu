# Tomagotchu.py

import os
import time

def main():
    print("Welcome to Tomagotchu!")
    while True:
        print("\nMenu:")
        print("1. Feed Tomagotchu")
        print("2. Play with Tomagotchu")
        print("3. Run a Script")
        print("4. Install a Package")
        print("5. Exit")
        
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            feed_tomagotchu()
        elif choice == '2':
            play_with_tomagotchu()
        elif choice == '3':
            run_script()
        elif choice == '4':
            install_package()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def feed_tomagotchu():
    print("\nFeeding Tomagotchu...")

def play_with_tomagotchu():
    print("\nPlaying with Tomagotchu...")

def run_script():
    script = input("\nEnter the path of the script you want to run: ")
    os.system(script)

def install_package():
    package = input("\nEnter the name of the package you want to install: ")
    os.system(f"pkg install {package}")

if __name__ == "__main__":
    main()
