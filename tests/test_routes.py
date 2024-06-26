from unittest.mock import patch
@patch('app.get_news')
def test_news_type(mock_get_news, client):
    mock_get_news.return_value = [
        {
            "title": "Test Article",
            "description": "Test Description",
            "url": "http://example.com",
            "urlToImage": "http://example.com/image.jpg",
            "publishedAt": "2023-06-26T12:00:00Z",
            "source": {"name": "Test Source"}
        }
    ]
    response = client.get('/niche/technology')
    assert response.status_code == 200
    assert b'Test Article' in response.data
    assert b'Test Source' in response.data

@patch('app.get_news')
def test_news_niche_get(mock_get_news, client):
    mock_get_news.return_value = [
        {
            "title": "Test Article",
            "description": "Test Description",
            "url": "http://example.com",
            "urlToImage": "http://example.com/image.jpg",
            "publishedAt": "2023-06-26T12:00:00Z",
            "source": {"name": "Test Source"}
        }
    ]
    response = client.get('/niche?search=technology')
    assert response.status_code == 200
    assert b'Test Article' in response.data
    assert b'Test Source' in response.data

@patch('app.get_news')
@patch('app.random.randint')
def test_random_news(mock_randint, mock_get_news, client):
    mock_randint.return_value = 0
    mock_get_news.return_value = [
        {
            "title": "Random Article",
            "description": "Random Description",
            "url": "http://example.com",
            "urlToImage": "http://example.com/image.jpg",
            "publishedAt": "2023-06-26T12:00:00Z",
            "source": {"name": "Random Source"}
        }
    ]
    response = client.get('/random')
    assert response.status_code == 200
    assert b'Random Article' in response.data
    assert b'Random Source' in response.data