from fastapi import FastAPI
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

# MySQL connection
db = mysql.connector.connect(
    host="mysql",
    port=3306,
    user="root",
    password="rootpassword",
    database="banking"
)

cursor = db.cursor()

class DepositRequest(BaseModel):
    amount: float


@app.post("/account/{account_number}/deposit/")
async def deposit(account_number: str, deposit_request: DepositRequest):
    amount = deposit_request.amount
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE account_number = %s", (amount, account_number))
    db.commit()
    return {"message": "Deposit successful"}

@app.post("/account/{account_number}/withdraw/")
async def withdraw(account_number: str, amount: float):
    cursor.execute("UPDATE accounts SET balance = balance - %s WHERE account_number = %s", (amount, account_number))
    db.commit()
    return {"message": "Withdrawal successful"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
