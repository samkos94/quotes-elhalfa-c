from functions import add_quote

def menu():
    print("1. Add a quote")
    print("2. Display quotes")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    quotes = []
    filename = "quotes.txt"

    while True:
        choice = menu()

        if choice == "1":
            add_quote(quotes, filename)
            print("Quote added successfully!")
        elif choice == "2":
            display_quotes(filename)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
