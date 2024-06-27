# Home Page
![Home](/static/HomePage.png)

# Find your niche section
![Choices](/static/Choices.png)

# Dockerhub Image Repo
<a href="https://hub.docker.com/repositories/bandhan99"><img src="https://www.padok.fr/en/blog/docker-hub-rate-limit" alt="Repo" style="width:42px;height:42px;"></a>

# Newz Shortie!

Welcome to Newz Shortie! This Flask-based web application allows users to fetch news articles from the News API and view them based on their preferred genre.

## Website Link

You can access the website [Here](https://newz-shortie.onrender.com/)

## Features

- **News Fetching**: Fetches news articles from the News API.
- **Genre Selection**: Allows users to select their preferred news genre.
- **Genre-based Display**: Displays news articles based on the selected genre.
- **User-friendly Interface**: Simple and intuitive user interface for ease of use.

## CREATE EC2 and setup DOCKER

Read this blog : https://bit.ly/4entdPU

To run this project locally, follow these steps:

1. Create a new EC2 instance
2. Edit inbound rule and add custom tcp at port 5000

3. Download Docker in that ec2
4. ```bash
   sudo apt update
   sudo apt install docker.io -y
   ```
5. Check Docker daemon status via
   ```bash
   sudo systemctl status docker
   ```
6. If it is not running, make it run with
   ```bash
   sudo systemctl start docker
   ```
7. Grant access to user to run Docker commands
   ```bash
   sudo usermod -aG docker ubuntu
   ```
8. Check if it's working properly or not
   ```bash
   docker run hello-world
   ```
   it should return this as output
   ```bash
   Hello from Docker!
   This message shows that your installation appears to be working correctly.

   To generate this message, Docker took the following steps:
   1. The Docker client contacted the Docker daemon.
   2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
     (amd64)
   3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
   4. The Docker daemon streamed that output to the Docker client, which sent it
     to your terminal.

   To try something more ambitious, you can run an Ubuntu container with:
   $ docker run -it ubuntu bash

   Share images, automate workflows, and more with a free Docker ID:
   https://hub.docker.com/
   ```

## Clone, create image & container

9. Clone the repository:

    ```bash
    git clone https://github.com/bandhan-majumder/Newz_Shortie.git
    ```
10. Obtain a News API key from [newsapi.org](https://newsapi.org/) and replace `"YOUR_API_KEY"` in `api_key.py` with actual API key.
   
11. Generate Docker image:

    ```bash
    docker build -t <custom_img_name>
    ```
12. Get the image id
   ```bash
    sudo docker images
   ```
13. Spin up the container and expose the 5000 port (default port of flask appliocation).
   ```bash
    sudo docker -p 5000:5000 -it <image_id>
   ```
14. Go to browser and search for `public_ip_of_ec2instace:5000`

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
