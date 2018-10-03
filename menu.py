#Utility functions for generating and interacting with numeric command line menus.

class Menu:
    #NOT CURRENTLY USED
    @staticmethod
    #offer each option as a numbered menu       
    def numeric_menu(self, menu_items):
        for x in range(0, len(menu_items)):
            print(str(x + 1) + ") " + menu_items[x])
        print("Please enter the number you wish to choose, or enter exit to cancel:")
        return self.parse_menu_input(menu_items);
    
    #NOT CURRENTLY USED
    @staticmethod
    #offer each option as a numbered menu and format the output      
    def numeric_menuf(self, menu_items, formatter):
        for x in range(0, len(menu_items)):
            print(str(x + 1) + ") " + formatter(menu_items[x]))
        print("Please enter the number you wish to choose, or enter exit to cancel:")
        return self.parse_menu_input(self, menu_items);
    
    #Split from menu choice in case other forms of parsing required,
    #which could then be passed as an arg to choose_source ie. this would be numeric,
    #another could be string etc.
    @staticmethod
    def parse_menu_input(self, menu_items):
        response = input(">>>")
        if response == "exit":
            return -1
        try:
            response = int(response)
            if (response > 0 and response <= len(menu_items)):
                return menu_items[response - 1]
        except ValueError:
            pass
        print("Please enter a valid number, or type exit to cancel.")
        return self.parse_menu_input(self, menu_items)
    
    
    @staticmethod
    def confirm_change(confirm_statement):
        print(confirm_statement + " (y/n):")
        response = input(">>>")
        if(response == "y" or response == "yes" or response == "YES"):
            return True
        elif(response == "n" or response == "no" or response == "NO"):
            return False
        print("Invalid input.")
        return Menu.confirm_source_addition(match)