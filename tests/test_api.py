from fastapi.testclient import TestClient

from backend.app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"


def test_dashboard_stats():
    response = client.get("/api/dashboard/stats")

    assert response.status_code == 200

    data = response.json()

    assert "total_threats" in data
    assert "critical_threats" in data
    assert "average_risk" in data


def test_threats():
    response = client.get("/api/threats?limit=5")

    assert response.status_code == 200
    assert len(response.json()) == 5


def test_awareness_modules():
    response = client.get("/api/awareness/modules")

    assert response.status_code == 200
    assert len(response.json()) > 0


def test_quiz():
    response = client.get("/api/quiz")

    assert response.status_code == 200
    assert len(response.json()) == 5