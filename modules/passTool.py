import bcrypt

def createdHashPass(contra: str):
    contra = contra.encode()
    passSalt = bcrypt.gensalt()
    passhash = bcrypt.hashpw(password= contra , salt= passSalt)
    passhash = passhash.decode()
    return passhash


def checkPassHash(contra : str , contraHash : str):
    return bcrypt.checkpw(password= contra.encode() , hashed_password= contraHash.encode())


