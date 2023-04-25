from fastapi.testclient import TestClient
from app.main import app, min_max_average

client = TestClient(app)


def test_average_status():
    response = client.get("/average/thb/2022-01-03")
    assert response.status_code == 200


def test_average_bad_code_status():
    response = client.get("/average/pln/2022-01-03")
    assert response.status_code == 404


def test_average_bad_date_status():
    response = client.get("/average/thb/2022-01-01")
    assert response.status_code == 404


def test_min_max_status():
    response = client.get("/minmax/usd/255")
    assert response.status_code == 200


def test_min_max_bad_code_status():
    response = client.get("/minmax/pln/255")
    assert response.status_code == 404


def test_min_max_bad_n_status():
    response = client.get("/minmax/usd/256")
    assert response.status_code == 404


def test_major_difference_status():
    response = client.get("/difference/usd/255")
    assert response.status_code == 200


def test_major_difference_bad_code_status():
    response = client.get("/difference/pln/255")
    assert response.status_code == 404


def test_major_difference_bad_n_status():
    response = client.get("/difference/usd/256")
    assert response.status_code == 404


def test_min_max_average():
    temp = [4.2024, 4.2006, 4.1905, 4.1649]
    result = min_max_average(temp)
    assert result == {
        "min": 4.1649,
        "max": 4.2024
    }
