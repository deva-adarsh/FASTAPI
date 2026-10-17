import secrets

# This code will generate the secreat key
SECRET_KEY=secrets.token_urlsafe(32)
print(SECRET_KEY)