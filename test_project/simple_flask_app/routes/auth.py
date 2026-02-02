from services.auth_service import authenticate

def login():
    user = authenticate()
    if user:
        return "Login Success"
    return "Login Failed"
