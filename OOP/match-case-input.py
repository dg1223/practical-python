class Address:
    # constructor
    def __init__(self):
        self.name = ''
        self.address = ''

class MethodParams:
    def get_choice(self):
        print("My Address Book\n")
        print("A - Add New Address")
        print("D - Delete Address")
        print("M - Modify Address")
        print("V - View Addresses")
        print("Q - Quit\n")

        return input("Choice: ")
    
    def add_address(self, addr):
        print(f"Name: {addr.name}, Address: {addr.address} added.")

    def delete_address(self, name):
        print(f"You wish to delete {name}'s address.")

    def modify_address(self, addr):
        addr.address = 'New Python Station'

    def view_address(self, names):
        for name in names:
            print(f"You want to view address of {name}.")
    
    def make_decision(self, choice):
        addr = Address()

        match choice.lower():
            case 'a':
                addr.name = 'Joe'
                addr.address = 'Python Station'
                self.add_address(addr)
            case 'd':
                addr.name = 'Robert'
                self.delete_address(addr.name)
            case "m":
                addr.name = "Matt"
                self.modify_address(addr)
                print(f"Name is now {addr.name}.")
            case 'v':
                name_list = ["Cheryl", "Joe", "Matt", "Robert"]
                self.view_address(name_list)
            case "q":
                print("Bye.")
            case _:
                print(f"{choice} is not valid.")

def main():
    mp = MethodParams()
    choice = ""
    while choice.lower() != 'q':
        choice = mp.get_choice()
        mp.make_decision(choice)
        input("Press Enter to continue...\n")

if __name__ == "__main__":
    main()