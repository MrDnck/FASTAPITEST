

def validate_login(correoEmisor, correoReceptor, passEmisor, passReceptor):
    if correoEmisor == correoReceptor and passEmisor == passReceptor:
        return True
    else:
        return False
