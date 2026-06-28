import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from main import app, db_sales

client = TestClient(app)

@pytest.fixture
def setup_test_data():
    """Фикстура для заполнения БД тестовыми данными"""
    db_sales.clear()
    data = [
        {"date": datetime(2023, 5, 10), "amount": 1000},
        {"date": datetime(2023, 5, 15), "amount": 2000},
        {"date": datetime(2023, 6, 1), "amount": 5000}, # Другой месяц
        {"date": datetime(2022, 5, 20), "amount": 500},  # Другой год
    ]
    db_sales.extend(data)
    yield
    db_sales.clear()

def test_get_monthly_sales_report(setup_test_data):
    """E2E тест: Запрос -> Фильтрация -> Агрегация"""
    # Запрашиваем отчет за май 2023
    response = client.get("/reports/sales?month=5&year=2023")
    
    assert response.status_code == 200
    data = response.json()
    
    # Проверка агрегации (1000 + 2000 = 3000)
    assert data["total_amount"] == 3000
    assert data["transaction_count"] == 2
    assert data["month"] == 5