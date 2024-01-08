# Art_Gallery_Bot
Art Gallery Bot is a Telegram bot designed to provide a platform for users to register, showcase their artwork, and find inspiration from others' creative works.

## Technologies Used:
aiogram v3.2.0: A powerful and user-friendly Python library for building Telegram bots.

aiogram-widgets: Enhance your bot's functionality with interactive widgets using aiogram-widgets.

MongoDB: A NoSQL database for storing and managing user registrations and artwork information.

Docker: Containerization to ensure consistent deployment across various environments.

Railway: Simplify deployment and hosting with Railway, making it easier to manage and scale your bot.

## Getting Started:
Installation: Clone the repository and install the required dependencies.

```
git clone https://github.com/your-username/Art_Gallery_Bot.git
cd Art_Gallery_Bot
pip install -r requirements.txt
```
Configuration: Set up your MongoDB credentials and Telegram API token in the configuration files.

```
cp config.example.py config.py
```
Edit config.py with your MongoDB URI and Telegram API token.

Running Locally: Launch the bot locally for testing.

```
python main.py
```
Docker: Use Docker for containerized deployment.

```
docker build -t art_gallery_bot .
docker run -d art_gallery_bot
```
Video Demo:

https://github.com/blenassefa2/Art_Gallery_Bot/assets/62964622/d3311b82-b44a-4c46-af23-949b7b684c49


Contributing:
Feel free to contribute to the project by creating issues and pull_requests.

License:
This project is licensed under the [MIT License] - see the [LICENSE] file for details.

