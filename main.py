import PasswordChecker

def main():
    user_pswd = input("Enter a password pls: ")
    result = PasswordChecker.pswd_check(user_pswd)
    if result == True:
        print("Smashed it mate, golf clap.")
    else:
        print("Ugh you total fucking idiot!!")

if __name__ == "__main__":
    main()