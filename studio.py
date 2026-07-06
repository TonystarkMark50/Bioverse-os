from generator.project import create_project

def menu():
    while True:
        print("\n" + "="*60)
        print("           BioVerse Studio v1.0")
        print("="*60)

        print("1. Create BioVerse OS Project")
        print("2. Exit")

        choice = input("\nSelect: ")

        if choice == "1":
            create_project()

        elif choice == "2":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()