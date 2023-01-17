import database

MENU_PROMPT = """

Please choose one of these options:
-- Coffe Bean App --
1) Add a new bean.
2) See all beans.
3) Find a ben by name.
4) See which preparation method is best for a bean.
5) Exit

Your selection:"""


def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "5":
        if user_input == "1":
            name = input("Enter bean name: ")
            method = input("Enter how you've prepared it: ")
            rating = int(input("Enter your rating score (0-100): "))

            database.add_bean(connection, name, method, rating)
        elif user_input == "2":
            beans = database.get_all_Beans(connection)
            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]/100}")
        elif user_input == "3":
            name = input("Enter bean name to find: ")
            beans = database.get_beans_by_name(connection, name)

            for bean in beans:
                print(f"{bean[1]} ({bean[2]}) - {bean[3]}/100")
        elif user_input == "4":
            name = input("Enter bean name to find: ")
            best_method = database.get_best_prep_for_bean(connection, name)

            print(f"The best preparation for {name} is: {best_method[2]}")
        else:
            print("Invalid input, please try again!")


menu()
