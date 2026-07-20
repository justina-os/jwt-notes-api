from fastapi import APIRouter,HTTPException,Depends
from pydantic import BaseModel
from backend.db import get_connection
from backend.auth import hash_password, verify_password

login=APIRouter()
from jose import jwt,JWTError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/")


SECRET_KEY = "supersecretkey123"
ALGORITHM = "HS256"
expire=timedelta(minutes=30)

class  Detail(BaseModel):
    mail_id:str
    password:str




def create_token(data:dict):
    copy=data.copy()
    time=datetime.now()+expire
    copy.update({"exp":time})

    encode=jwt.encode(copy,SECRET_KEY,algorithm=ALGORITHM)

    return encode
    

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("sub")
        print(payload)

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return user_id

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

@login.post("/login")
def log_in(detail:Detail):
   

    con=get_connection()
    cur=con.cursor(dictionary=True)

    cur.execute("select * from login where mail_id=%s",(detail.mail_id,))
    isExist=cur.fetchone()
    
    cur.close()
    con.close()

    

    if isExist:
        isverified=verify_password(detail.password,isExist["password"])
        if isverified:
            token = create_token({"sub": str(isExist["user_id"])})
            return {"access_token": token, "token_type": "bearer"}
        else:
            raise HTTPException(status_code=401,detail="Invalid credentials")
    else:
        raise HTTPException(status_code=404 ,detail="User not found")
    
@login.post("/signup")
def sign_in(detail:Detail):
    con=get_connection()
    cur=con.cursor(dictionary=True)

    cur.execute("select * from login where mail_id=%s",(detail.mail_id,))
    isExist=cur.fetchone()
    password=hash_password(detail.password)


    try:
        if not isExist:
            cur.execute("insert  into login (mail_id,password) values(%s,%s)",(detail.mail_id,password))
            con.commit()
            return {"message": "User created"}
        else:
            raise HTTPException(
                 status_code=400,
                 detail="User already exists"
                   )
    finally:

        cur.close()
        con.close()


        
def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    return verify_token(token)