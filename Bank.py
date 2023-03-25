from typing import Union
import uvicorn
from fastapi import FastAPI,status,HTTPException
app = FastAPI()

Balances = {"Admin":0,"NoAdmin":0,"Susana":0}

Database = {"Admin":"Borgir","NoAdmin":"NoBorgir","Susana":"Distancia"}

@app.post("/Login",status_code=status.HTTP_202_ACCEPTED)
def  Login (Usuario:str,Contrasena:str):
    for key,value in Database.items():
        if Usuario == key and Contrasena == value:
            return True
#    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization Required")
    return False

@app.post("/Register",status_code=status.HTTP_201_CREATED)
def Register (New_User:str,New_Password:str):
    if New_User not in Database:
        Database[New_User] = New_Password
        Balances[New_User] = 0
        return
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

@app.delete("/Delete",status_code=status.HTTP_204_NO_CONTENT)
def Remove (Usuario:str,Contrasena:str,Usuario_Deleteble:str):
    Confirmacion = Login(Usuario,Contrasena)
    if (Usuario == "Admin" or Usuario == Usuario_Deleteble) and Confirmacion and Usuario_Deleteble in Database.keys():
        Database.pop(Usuario_Deleteble)
        Balances.pop(Usuario_Deleteble)
        return
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="U no admin")
        
@app.put("/Modify",status_code=status.HTTP_202_ACCEPTED)
def Modify (Usuario:str,Contrasena:str,Nueva_Contrasena:str):
    Confirmacion = Login(Usuario,Contrasena)
    if Confirmacion:
        Database.update ({Usuario:Nueva_Contrasena})
        return
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You must be the user you want to modify")

@app.post("/Balance")
def Obtain (Usuario,Contrasena):
    Confirmacion = Login(Usuario,Contrasena)
    
    if Confirmacion:
        return Balances[Usuario]
    return False

@app.post ("/Add_Balance")
def Add (Usuario,Contrasena,Dinero_Anadir:int):
    Confirmacion = Login(Usuario,Contrasena)
    if  Confirmacion and Dinero_Anadir > 0:
        Balances[Usuario] = Balances[Usuario] + Dinero_Anadir
        return True
    return False

@app.post ("/Withdrawal")
def Withdraw (Usuario,Contrasena,Dinero_rEDUCIR:int):
    Confirmacion = Login(Usuario,Contrasena)
    if  Confirmacion and Dinero_rEDUCIR<=Balances[Usuario]:
        Balances[Usuario] = Balances[Usuario] - Dinero_rEDUCIR
        return True
    return False
        









if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)