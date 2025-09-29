def is_email_unique(users, email):
    count = 0
    for user in users:
        if user.get('email') == email:
            count += 1
    return count == 1