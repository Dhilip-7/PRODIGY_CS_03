import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    length = len(password)
    if length < 8:
        feedback.append("Too short, aim for 8+ characters.")
    elif length < 12:
        score += 1
        feedback.append("Decent length (8-11 chars).")
    else:
        score += 2
        feedback.append("Great length (12+ chars)!")
    
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Has uppercase: Nice!")
    else:
        feedback.append("Add some uppercase letters.")
    
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Has lowercase: Good job!")
    else:
        feedback.append("Mix in some lowercase letters.")
    
    if re.search(r"[0-9]", password):
        score += 1
        feedback.append("Numbers included: Sweet!")
    else:
        feedback.append("Throw in some numbers.")
    
    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
        feedback.append("Special chars: Awesome!")
    else:
        feedback.append("Add special chars like !@#$%.")
    
    strength = "Weak" if score <= 2 else "Moderate" if score <= 4 else "Strong"
    
    return {
        "strength": strength,
        "score": score,
        "feedback": feedback
    }

def main():
    print("Password Strength Checker")
    print("-----------------------")
    
    while True:
        password = input("Enter a password (or 'q' to quit): ")
        if password.lower() == 'q':
            print("See ya!")
            break
            
        result = check_password_strength(password)
        
        print("\nResults:")
        print(f"Strength: {result['strength']}")
        print(f"Score: {result['score']}/5")
        print("Tips:")
        for tip in result['feedback']:
            print(f"- {tip}")
        print()

if __name__ == "__main__":
    main()
