import logging

logger = logging.getLogger(__name__)


def test_get_root(client):
    response = client.get("/")
    response_data = response.data.decode('utf-8')
    assert response_data == f"To use this app: http://localhost:5000/data?date=YYYYMMDD"
