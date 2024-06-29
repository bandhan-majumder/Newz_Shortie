# Home Page
![Home](/static/HomePage.png)

# Find your niche section
![Choices](/static/Choices.png)

# Dockerhub Image Repo
<a href="https://hub.docker.com/repositories/bandhan99"><img src="https://www.padok.fr/en/blog/docker-hub-rate-limit" alt="Repo" style="width:42px;height:42px;"></a>

# Newz Shortie!

Welcome to Newz Shortie! This Flask-based web application allows users to fetch news articles from the News API and view them based on their preferred genre.

## Website Link

As AWS charges if I keep my instance running all the time, the application is deployed on Render and can be accessed from [running on Render](https://newz-shortie.onrender.com/). By updating secrets with the new EC2 instance's host, private file (.pem) and user, GitHub action will automatically deploy this application to that instance and can be access at port 5000 (<public_ip>:5000) with **added inbound rule of custom TCP at port 5000**.

## Features

### CI/CD
- **CI/CD pipleine**: ci.yaml and cd.yaml continously do integration and deployment to an EC2 instance ( instance is not running now ) after checking the code with pytest.
- **Code testing**: ci.yaml tests the python code everytime using pytest
  
### Web App
- **News Fetching**: Fetches news articles from the News API.
- **Genre Selection**: Allows users to select their preferred news genre.
- **Genre-based Display**: Displays news articles based on the selected genre.
- **User-friendly Interface**: Simple and intuitive user interface for ease of use.

## Docker (distroless image) and AWS (EC2) 

Read this blog on deploying this app with distroless image container and EC2 instance (AWS) : [MY HASHNODE BLOG](https://bit.ly/4entdPU) 

**To run this project locally, follow these steps:**

1. Run the following command on the terminal 
    ```bash
    git clone https://github.com/bandhan-majumder/Newz_Shortie
    ```
2. go to the folder using cd
   ```bash
   cd Newz_Shortie
   ```
3. Obtain a News API key from [newsapi.org](https://newsapi.org/) and replace `"my_news_api_key"` in `api.py` with actual API key.
4. Install all the requirements using
   ```bash
   pip install -r requirements. txt
   ```
5. Run the app
   ```bash
   python app.py
   ```
6. Access the working application
   <localhost:5000>

## Usage

1. Visit the website.
2. Select a genre of interest.
3. View news articles from the chosen genre.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/<YourFeature>`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/<YourFeature>`).
5. Open a pull request.

## Credits

This project was created by [Bandhan Majumder](https://github.com/bandhan-majumder).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
