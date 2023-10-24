import function

def menuFiles():
    with open("//Users/danyangli/Documents/Study/JUST_IT/Project/Database/optionMenu.txt") as mainMenu:
          userMainMenu = mainMenu.read()
    with open("/Users/danyangli/Documents/Study/JUST_IT/Project/Database/reportsMenu.txt") as mainMenu:
          userReportMenu = mainMenu.read()
    return userMainMenu, userReportMenu 

def films_menu():
    options = 0 
    optionsList = ["1","2","3","4","5"] 
    userChoices = menuFiles()

    while options not in optionsList: 
         print(userChoices[0])
         options = input("Enter an option from the films main menu choices above: ") 

         if options not in optionsList:
            print(f"{options} is not a valid choice in the films menu!")
    return options

def report_subMenu():
    options = 0
    optionsList = ["1","2","3","4","5"]
    reportChoices = menuFiles()

    while options not in optionsList:
        print(reportChoices[1])


        options = input("Enter an option from the report sub menu choices above: ")

        if options not in optionsList:
            print(f"{options} is not a valid choice in the reports sub menu!")
    return options

mainProgram = True

while mainProgram: 
    mainMenu = films_menu()  

    if mainMenu == "1":
        function.insert_data() 
        
    elif mainMenu == "2":
        function.delete_data()

    elif mainMenu == "3":
        function.update_data()

    elif mainMenu == "4":
        function.read_data()
    
    elif mainMenu == "5":
        mainProgram = False
        reportsProgram = True

        while reportsProgram:
            reportSubMenu = report_subMenu()

            if reportSubMenu == "1":
                function.all_films()
            elif reportSubMenu == "2":
                genre = input("Enter the genre: ")
                function.by_genre(genre)
            elif reportSubMenu == "3":
                year = input("Enter the year: ")
                function.by_year(year)
            elif reportSubMenu == "4":
                rating = input("Enter the rating: ")
                function.by_rating(rating)
            elif reportSubMenu == "5":
                reportsProgram = False
    else:
        mainProgram = False

input("Press enter to return to Quit the films application: ")