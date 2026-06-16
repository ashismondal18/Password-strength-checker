import re

common_passwords = {
    "password", "123456", "123456789", "qwerty", "abc123", "password1", 
    "admin", "welcome", "iloveyou","india","123","@123", "123123", "letmein", "monkey", 
    "football", "shadow", "master", "dragon", "sunshine", "trustno1", 
    "superman", "hello", "freedom", "whatever", "qazwsx", "654321", 
    "qwerty123", "1q2w3e4r", "1qaz2wsx", "asdf", "zxcv", "qwertyuiop", 
    "mnbvcxz", "poiuytrewq", "12345678", "87654321", "password123", 
    "passw0rd", "p@ssw0rd", "iloveyou123", "abcd1234", "asdfgh", "zxcvbn", 
    "qwertyu", "poiuytre", "lkjhgfdsa", "zaq12wsx", "qazwsxedc",
    "plmokn", "wsxedc", "rfvtgb", "aaaaaa", "12345", "1234567890", "111", 
    "1234", "111111", "222222", "333333", "444444", "555555", "666666", 
    "696969", "777777", "888888", "999999", "000000","789","0000000000", "abcabc", "ababab", 
    "456456", "789789", "qwertyqwerty","asdfghjkl","zxcvbnm","soccer", "baseball", 
    "basketball", "hockey", "golf", "tennis", "cricket", "lakers", 
    "yankees", "madrid", "arsenal", "chelsea"
}

def check_password_strength(password):
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if (len(password) >= 8 and has_upper and has_lower and has_digit and has_special
            and password.lower() not in common_passwords
            and not any(pattern in password.lower() for pattern in common_passwords)):
        return "Very Strong"
    else:
        return "Weak"

def get_feedback(password):
    feedback = []

    # Criteria checks
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if len(password) < 8:
        feedback.append("Password is too short. It must be at least 8 characters.")
    if not has_upper:
        feedback.append("Add at least one uppercase letter.")
    if not has_lower:
        feedback.append("Add at least one lowercase letter.")
    if not has_digit:
        feedback.append("Include at least one digit.")
    if not has_special:
        feedback.append("Use at least one special character (e.g., !, @, #, $).")
    if password.lower() in common_passwords:
        feedback.append("Password is too common. Choose something more unique.")
    if any(pattern in password.lower() for pattern in common_passwords):
        feedback.append("Avoid using predictable keyboard patterns or repeated sequences.")

    # Final strength
    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special and not feedback:
        strength = "Very Strong password!"
    else:
        strength = "Weak password!"

    return feedback, strength
