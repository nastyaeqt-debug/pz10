from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import List, Dict

app = FastAPI()

# Имитация базы данных
db_sales = []

@app.get("/reports/sales")
async def get_monthly_sales(month: int, year: int):
    if not (1 <= month <= 12):
        raise HTTPException(status_code=400, detail="Invalid month")
    
    # Фильтрация данных по месяцу и году
    report_data = [
        sale for sale in db_sales 
        if sale["date"].month == month and sale["date"].year == year
    ]
    
    # Агрегация
    total_amount = sum(sale["amount"] for sale in report_data)
    transaction_count = len(report_data)
    
    return {
        "month": month,
        "year": year,
        "total_amount": total_amount,
        "transaction_count": transaction_count
    }

@app.get("/untested-feature")
def untested_feature():
    # Этот код добавит много строк, которые не будут выполнены тестами
    print("Step 1")
    print("Step 2")
    print("Step 3")
    print("Step 4")
    print("Step 5")
    return {"status": "not covered"}

def function1():
    print("No test here")
    return 1

def function2():
    print("No test here either")
    return 2