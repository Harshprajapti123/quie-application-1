import hashlib

# User data and results
users = {}
results = {}

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# User registration
def register():
    username = input("Enter username: ")
    if username in users:
        print("Username already exists!")
        return False
    password = input("Enter password: ")
    users[username] = hash_password(password)
    print("Registration successful!")
    return True

# User login
def login():
    username = input("Enter username: ")
    if username not in users:
        print("Username not found!")
        return False
    password = input("Enter password: ")
    if users[username] == hash_password(password):
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False

# Quiz questions
quizzes = {
    "Python": {
        "What is the keyword used to define a function in Python?": "def",
        "What is the output of print(2 ** 3)?": "8",
        "Which data type is immutable in Python?": "tuple",
        "What is the default port for HTTP?": "80",
        "What is the extension for Python files?": ".py"
    },
    "Java": {
        "Which keyword is used to inherit a class in Java?": "extends",
        "What is the size of an int in Java?": "4 bytes",
        "Which method is the entry point of a Java application?": "main",
        "What does JVM stand for?": "Java Virtual Machine",
        "What is the default value of a boolean in Java?": "false"
    },
    "C++": {
        "Which symbol is used to start a comment in C++?": "//",
        "What is the extension for C++ files?": ".cpp",
        "Who is the creator of C++?": "Bjarne Stroustrup",
        "Which operator is used to access a member of a class in C++?": ".",
        "What is a destructor in C++?": "A special member function called when an object is destroyed"
    }
}

# Take quiz
def take_quiz(subject, username):
    questions = quizzes[subject]
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.strip().lower() == answer.lower():
            score += 1
    print(f"Your score: {score}/{len(questions)}")
    if username in results:
        results[username].append((subject, score))
    else:
        results[username] = [(subject, score)]

# View results
def view_results(username):
    if username not in results:
        print("No results found for this user.")
        return
    for subject, score in results[username]:
        print(f"Subject: {subject}, Score: {score}/5")

# Display main menu
def display_menu():
    print("Quiz Application Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Take Quiz")
    print("4. View Results")
    print("5. Exit")

# Main function to run the application
def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            if login():
                username = input("Enter your username: ")
                while True:
                    display_menu()
                    choice = input("Enter choice: ")
                    if choice == "3":
                        subjects = list(quizzes.keys())
                        print("Choose a subject:")
                        for i, subject in enumerate(subjects, 1):
                            print(f"{i}. {subject}")
                        subject_choice = int(input("Enter choice: "))
                        if 1 <= subject_choice <= len(subjects):
                            take_quiz(subjects[subject_choice - 1], username)
                        else:
                            print("Invalid choice!")
                    elif choice == "4":
                        view_results(username)
