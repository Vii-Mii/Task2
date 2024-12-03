# Joke API Fetcher

This project is a Django-based API that interacts with the **JokeAPI** to fetch jokes, process them, and store them in a database. The API provides an endpoint to retrieve stored jokes.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/joke-api-fetcher.git](https://github.com/Vii-Mii/Task2.git
cd Task2/joke_project

pip install pipenv
pipenv install
pipenv shell


python manage.py makemigrations
python manage.py migrate


python manage.py fetch_jokes

python manage.py runserver

GET http://127.0.0.1:8000/api/jokes/

