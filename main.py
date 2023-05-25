from function import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Add quotes")
    print("4. Display_quotes ")
    print("5. Exit")


def main():
    quotes = []
    filename = "quotes.txt"

    while True:
        quotes = load_quotes("quotes.txt")
        filename="quotes.txt"
        menu()

        choice = input("Choose your an action (1-5): ")

        if choice == "1":
            print_quote(random_quote(quotes))
        elif choice == "2":
            view_quotes(quotes)
        elif choice=="3":
            add_quote(quotes,filename)
            print("quoted added")
        elif choice == "4" : # gestion de display_count()
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)


        elif choice == "5":

            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
