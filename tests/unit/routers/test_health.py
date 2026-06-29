from src.routers.health import health_check


def test_health_check_returns_ok_status():
    result = health_check()
    assert result == {"status": "ok"}
