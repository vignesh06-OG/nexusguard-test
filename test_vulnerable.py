# test_vulnerable.py
import os

# 1. Hardcoded Secret (SECURITY RISK!)
API_KEY = "sk-1234567890abcdef1234567890abcdef"

def login_user(username, password):
    # 2. SQL Injection Vulnerability (SECURITY RISK!)
    # Never use f-strings for SQL queries like this!
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print(f"Executing: {query}")
    return "User logged in!"

def get_data(user_input):
    # 3. Command Injection Risk (SECURITY RISK!)
    # Never use os.system with user input
    os.system(f"echo {user_input}")

def insecure_crypto():
    # 4. Use of insecure algorithm
    import hashlib
    password = "password123"
    return hashlib.md5(password.encode()).hexdigest()

if __name__ == "__main__":
    print(login_user("admin' OR '1'='1", "pass"))
    get_data("; rm -rf /")
