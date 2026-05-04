import datetime
import os

class JournalManager:
    def __init__(self, filename="journal.txt"):
        self._filename = filename 

    @property
    def filename(self):
        return self._filename


    def add_entry(self, text):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(self._filename, "a", encoding="utf-8") as file:
            file.write(f"[{timestamp}]\n {text}\n\n")

        print("Entry saved!\n")

    def view_entries(self):
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                content = file.read()
                entries = content.strip().split("\n\n")
    
            if not content.strip():
                print("No entries found.\n")
                return

            print("\n--- All Journal Entries ---")
            for entry in entries:
                print(entry.strip())
            print()

        except FileNotFoundError:
            print("-"*30,"\n")
            print("No journal file found.")
            print("-"*30,"\n")

    def search_entries(self, keyword):
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                content = file.read()
                entries = content.strip().split("\n\n")

            found = False
            print("\n--- Search Results ---\n")

            for entry in entries:
                if keyword.lower() in entry.lower():
                    print(f"{entry.strip()}\n")
                    found = True

            if not found:
                print("-"*30,"\n")
                print("No matching entries found.")
                print("-"*30,"\n")

        except FileNotFoundError:
            print("No journal file found.\n")


def main():
    journal = JournalManager()

    while True:
        print("Journal Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Search Entries")
        print("4. delete all entries")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            text = input("Write your journal entry:\n")
            journal.add_entry(text)

        elif choice == "2":
            journal.view_entries()

        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            journal.search_entries(keyword)

        elif choice == "4":           
            if os.path.exists(journal.filename):
                confirm= input("Are you sure you want to delete all entries? (y/n): ")
                if confirm.lower() == "y":
                    with open(journal.filename, "w", encoding="utf-8") as file:
                        file.write("")
                    print("All entries deleted successfully!\n")
                else:
                    print("Operation cancelled.\n")
            else:
                print("-"*30,"\n")
                print("No journal file found.\n")
                print("-"*30,"\n")

        elif choice == "5":
            print("-"*30,"\n")
            print("Goodbye!")
            print("-"*30,"\n")
            break

        else:
            print("Invalid choice. Try again.\n")

main()    
