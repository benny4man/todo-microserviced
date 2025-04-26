from jose import jwt, JWTError

SECRET_KEY = "245dfgdrre#^634b563dsfger45b6%^*$^sdgtbvsvdfgse"
ALGORITHM = "HS256"

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
