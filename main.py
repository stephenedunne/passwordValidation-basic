import PasswordChecker

def main():
    user_pswd = input("Enter a password: ")
    result = PasswordChecker.pswd_check(user_pswd)
    if result == True:
        print("Password accepted")
    else:
        print("Invalid password")

if __name__ == "__main__":
    main()
