![Photo](/static/readme.jpeg)

# Newz Shortie!

Welcome to Newz Shortie! This Flask-based web application allows users to fetch news articles from the News API and view them based on their preferred genre.

## Website Link

You can access the website at [https://newz-shortie.onrender.com/](https://newz-shortie.onrender.com/)

## Features

- **News Fetching**: Fetches news articles from the News API.
- **Genre Selection**: Allows users to select their preferred news genre.
- **Genre-based Display**: Displays news articles based on the selected genre.
- **User-friendly Interface**: Simple and intuitive user interface for ease of use.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/bandhan-majumder/Newz_Shortie.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Obtain a News API key from [newsapi.org](https://newsapi.org/) and replace `"YOUR_API_KEY"` in `api_key.py` with your actual API key.
4. Create a file named api_key.py (in the directory where app.py is located)
6. Inside api_key.py , create a variable my_news_api_key = "PROVIDE YOUR KEY"

7. Run the Flask application:

    ```bash
    python app.py
    ```

8. Access the website locally by visiting `http://localhost:5000` in your web browser.

## Usage

1. Visit the website.
2. Select a genre of interest.
3. View news articles from the chosen genre.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Credits

This project was created by [Bandhan Majumder](https://github.com/bandhan-majumder).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
