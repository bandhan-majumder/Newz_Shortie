import pytest

@pytest.fixture
def mock_news_data():
    return {
        "articles": [
            {
                "title": "Test Article 1",
                "description": "Description 1",
                "url": "http://example.com/1",
                "urlToImage": "http://example.com/image1.jpg",
                "publishedAt": "2023-06-26T12:00:00Z",
                "source": {"name": "Test Source 1"}
            },
            {
                "title": "Test Article 2",
                "description": "Description 2",
                "url": "http://example.com/2",
                "urlToImage": "http://example.com/image2.jpg",
                "publishedAt": "2023-06-26T13:00:00Z",
                "source": {"name": "Test Source 2"}
            }
        ]
    }