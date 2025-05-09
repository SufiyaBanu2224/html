# Initial user data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

# Create
def add_user(user_id, name, email):
    users.append({"id": user_id, "name": name, "email": email})

# Read
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
    return None

# Update
def update_user(user_id, name=None, email=None):
    for user in users:
        if user["id"] == user_id:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return True
    return False

# Delete
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return True
    return False

# Example usage
add_user(3, "Charlie", "charlie@example.com")
print(get_user(1))  # Alice
update_user(2, email="bob.new@example.com")
delete_user(1)
print(users)
