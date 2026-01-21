import json
import os

USERS_DB = "users.json"

def init_db():
    if not os.path.exists(USERS_DB):
        with open(USERS_DB, 'w') as f:
            json.dump({"admin": "password123", "ali": "hamza2026"}, f)

def authenticate(username, password):
    init_db()
    with open(USERS_DB, 'r') as f:
        users = json.load(f)
    
    if username in users and users[username] == password:
        return True
    return False

def main():
    print("--- User Authentication Service ---")
    username = input("Username: ")
    password = input("Password: ")
    
    if authenticate(username, password):
        print(f"Welcome, {username}! Access Granted.")
    else:
        print("Access Denied. Invalid credentials.")

if __name__ == "__main__":
    main()
