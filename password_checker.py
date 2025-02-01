import re

def check_password_strength(password):
    strength = 0
    strength_criteria = [
        (r'[a-z]', "lowercase letter"),
        (r'[A-Z]', "uppercase letter"),
        (r'\d', "digit"),
        (r'[!@#$%^&*(),.?":{}|<>]', "special character")
    ]
    
    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        print("Password should be at least 8 characters long.")
    
    # Check for other criteria
    for pattern, message in strength_criteria:
        if re.search(pattern, password):
            strength += 1
    
    # Strength score interpretation
    if strength == 5:
        return "Strong Password"
    elif 3 <= strength < 5:
        return "Moderate Password"
    else:
        return "Weak Password"

# Input and Output
password = input("Enter a password to check strength: ")
result = check_password_strength(password)
print(f"Password strength: {result}")
