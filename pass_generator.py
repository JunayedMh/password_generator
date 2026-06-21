import time

while True:

    def generate_password(length=12):

        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digits = "0123456789"
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        all_chars = lowercase + uppercase + digits + special
        randomness = int(time.time() * 1000000) % 1000000
        password = ""

        for i in range(length):
            randomness = (randomness * 1103515245 + 12345) % 2147483648
            pick_pass = randomness % len(all_chars)
            password += all_chars[pick_pass]

        return password

    length = int(input("Enter password length (minimum 8): ") or 12)

    if length < 8:
        print("Password length is too short!")
    else:
        password = generate_password(length)
        print(f"Generated password: ' {password} '")
    print()
    again = input("Do you want to generate another password?> (y/n)")
    again = again.strip().lower()

    if again == "n":
        print("Thanks for generating password.")
        break
