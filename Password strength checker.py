def check_strength(pw):
    length = len(pw) >= 8
    digit = any(c.isdigit() for c in pw)
    upper = any(c.isupper() for c in pw)
    lower = any(c.islower() for c in pw)
    special = any(c in "!@#$%^&*()" for c in pw)

    score = sum([length, digit, upper, lower, special])

    if score <= 2:
        return "Weak"
    elif score == 3:
        return "Moderate"
    else:
        return "Strong"

password = input("Enter password: ")
print("Strength:", check_strength(password))
