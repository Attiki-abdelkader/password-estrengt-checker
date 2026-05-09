import re

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # 1. Length Check
    if len(password) >= 8:
        strength += 1
    if len(password) >= 12:
        strength += 1

    # 2. Number Check
    if re.search(r"\d", password):
        strength += 1

    # 3. Uppercase and Lowercase Check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1

    # 4. Special Characters Check
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Determine Final Grade
    if strength <= 1:
        remarks = "Very Weak"
    elif strength == 2:
        remarks = "Weak"
    elif strength == 3:
        remarks = "Fair"
    elif strength == 4:
        remarks = "Strong"
    elif strength == 5:
        remarks = "Very Strong"

    return remarks

def main():
    print("--- Password Strength Checker ---")
    user_password = input("Enter password to check: ")
    result = check_password_strength(user_password)
    print(f"Analysis Result: {result}")

if __name__ == "__main__":
    main()
