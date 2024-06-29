from datetime import datetime, timedelta
from app import get_yesterdays_date

def test_get_yesterdays_date():
    expected_date = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')
    assert get_yesterdays_date() == expected_date