import msvcrt


def prompt_user():
    print("Press 'Q' to continue.")

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode().upper()
            print(key)

            if key == "Q":
                print("Continuing...")
                break
            else:
                print("Invalid input. Press 'Q' to continue.")


prompt_user()

"""
if y == "Q":
        return -1
    elif y == "E":
        return 1
    elif y == "0":
        return "0"
    elif y == "":
        return 0
    else:
        print("Invalid input. Please enter 'Q', 'E', '0', or press Enter.")

        """
