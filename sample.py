def get_user(user_id):

    password = "admin123"

    users = [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ]

    for user in users:
        if user["id"] == user_id:
            return user

    return None


def divide(a, b):

    return a / b