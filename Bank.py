from typing import Union
import uvicorn
from fastapi import FastAPI,status,HTTPException
app = FastAPI()

Database = {"Admin":"Borgir","NoAdmin":"NoBorgir","Susana":"Distancia"}

@app.post("/Login",status_code=status.HTTP_202_ACCEPTED)
def  Login (Usuario:str,Contrasena:str):
    for key,value in Database.items():
        if Usuario == key and Contrasena == value:
            return
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization Required")

@app.post("/Register",status_code=status.HTTP_201_CREATED)
def Register (New_User:str,New_Password:str):
    if New_User not in Database:
        Database[New_User] = New_Password
        return
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

@app.delete("/Delete",status_code=status.HTTP_204_NO_CONTENT)
def Remove (Usuario:str,Contrasena:str,Usuario_Deleteble:str):
    Confirmacion = Login(Usuario,Contrasena)
    if Usuario == "Admin" and Confirmacion and Usuario_Deleteble in Database.keys():
        Database.pop(Usuario_Deleteble)
        return
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="U no admin")
        
@app.put("/Modify",status_code=status.HTTP_202_ACCEPTED)
def Modify (Usuario:str,Contrasena:str,Nueva_Contrasena:str):
    Confirmacion = Login(Usuario,Contrasena)
    if Confirmacion:
        Database.update ({Usuario:Nueva_Contrasena})
        return
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You must be the user you want to modify")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)