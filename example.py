class hexaria_bosses:

    def input_function(self): # User Input
        chance = int(input("Enter Drop Chance of the item (no need to write %): "))
        account =int(input("Enter how many accounts are you using: "))
        time = int(input("what is the Estimate minutes it would take to complete a run: "))
        difficulty_input = input("Is the Difficulty normal or elite?: ")
        difficulty = 0

        if difficulty_input in ["normal","Normal","N","n"]:
            difficulty = 1.0
        elif difficulty_input in ["elite","Elite","E","e"]:
            difficulty = 1.4
        else:
            print("Improper input")
            exit()
        return chance, account, time, difficulty 
    
    def nicole(self): # Nicole function
        x = hexaria_bosses()
        chance,account,time,difficulty = x.input_function()
        result = 100/(chance * difficulty *account) * time
        print("It would take: {:.0f} Minutes to get 1 item that you are searching for".format(result))

    def skeleton_king(self): 
        x = hexaria_bosses()
        x.nicole()

    def non_bosses(self): # Non_bosses
        x = hexaria_bosses()
        chance,account,time,difficulty = x.input_function()
        if account == 1:
            result = 100/(chance * difficulty * 2 *account) * time
        elif account == 2:
            result = 100/(chance * difficulty * 3 *account) * time
        elif account in [3,4]:
            result = 100/(chance * difficulty * 4 *account) * time
        print("It would take: {:.0f} Minutes to get 1 item that you are searching for".format(result))

    def sedrian(self):
        x = hexaria_bosses()
        x.nicole()

    def roku(self): # roku function
        x = hexaria_bosses()
        x = chance,account,time,difficulty = x.input_function()
        result = 100/(chance * account) * time
        print("It would take: {:.0f} Minutes to get 1 item that you are searching for".format(result))

    def zombified(self):
        x = hexaria_bosses()
        x.roku()
    def exit(self):
        exit()
hexaria_class = hexaria_bosses() # Class call

#start of main method
while(True):
    print("\nHexaria Boss Item Calculator..?")
    print("\n[1]Nicole \n[2]Non-Boss Enemies \n[3]Skeleton King \n[4]Sedrian \n[5]Roku \n[6]zombified \n[7]Exit")
    choice = int(input("\nChoose the boss you're grinding at the moment: "))

    match choice:
        case 1:
            print("Selected: Nicole")
            hexaria_class.nicole()
        case 2:
            print("Selected: Non Boss Enemy")
            hexaria_class.non_bosses()
        case 3:
            print("Selected: Skeleton King")
            hexaria_class.skeleton_king()
        case 4:
            print("Selected: Sedrian")
            hexaria_class.sedrian()
        case 5:
            print("Selected: Roku")
            hexaria_class.roku()
        case 6:
            print("Selected: Zombified")
            hexaria_class.zombified()
        case 7:
            print("Goodbye :>")
            hexaria_class.exit()
    