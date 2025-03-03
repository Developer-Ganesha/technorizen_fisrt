import jwt

token = "your_access_token_here"  # Replace with your actual token
decoded_token = jwt.decode(token, options={"verify_signature": False})
print(decoded_token)
