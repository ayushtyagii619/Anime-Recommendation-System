# Anime Recommendation System API

This project is a Django REST Framework-based API that integrates with the AniList GraphQL API to provide anime search functionality, personalized recommendations, and user preference management.

## Features
- **User Authentication:** User registration and login using JWT tokens.
- **Anime Search:** Search for anime by name or genre using the AniList API.
- **User Preferences:** Save and manage user preferences such as favorite genres and watched anime.
- **Anime Recommendations:** Get personalized anime recommendations based on user preferences.

---

## Setup and Run Locally

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PostgreSQL
- Virtualenv (optional)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/anime-recommendation-api.git
   cd anime-recommendation-api


2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
4. Set up your environment variables: Create a .env file in the project root and configure the following:

   ```env
   SECRET_KEY=your_secret_key
   DATABASE_NAME=your_database_name
   DATABASE_USER=your_database_user
   DATABASE_PASSWORD=your_database_password
   DATABASE_HOST=127.0.0.1
   DATABASE_PORT=5432
5. Apply migrations:

   ```bash
   python manage.py migrate
6. Run the development server:

   ```bash
   python manage.py runserver
### Endpoints
### Authentication
1. Register
### URL
POST /auth/register

## Request Body:
```json
      {
       "email": "user@example.com",
       "name": "John Doe",
       "password": "yourpassword",
       "password2": "yourpassword"
      }
```
## Response:
```json
   {
       "MSG": "User registration complete."
   }
```
## Login
   ```json
   URL: POST /auth/login
```
## Request Body:
   ```json
   {
       "email": "user@example.com",
       "password": "yourpassword"
   }
```
## Response:

```json
{
    "token": {
        "refresh": "refresh_token",
        "access": "access_token"
    },
    "msg": "login successful"
}
```
## Anime Search
## URL: 
GET /anime/search
## Query Parameters:

- name (optional): Search anime by name.
- genre (optional): Filter anime by genre.
## Example Request:
GET /anime/search?name=Naruto

## Response:

```json
[
    {
        "id": 123,
        "title": {
            "romaji": "Naruto"
        },
        "description": "A story about a young ninja...",
        "genres": ["Action", "Adventure"]
    }
]
```
## User Preferences
## Get Preferences
## URL: 
GET /user/preferences
## Headers:

## Authorization: Bearer access_token
## Response:
```json
{
    "favorite_genres": "Action,Adventure",
    "watched_anime": "123,456"
}
```
## Set Preferences
## URL: 
POST /user/preferences
## Headers:
## Authorization: Bearer access_token
## Request Body:
```json
{
    "favorite_genres": "Comedy,Drama",
    "watched_anime": "789,1011"
}
```
## Response:

```json
{
    "favorite_genres": "Comedy,Drama",
    "watched_anime": "789,1011"
}
```
## Anime Recommendations
## URL: 
GET /anime/recommendations
## Headers:

## Authorization: Bearer access_token
## Response:

```json
[
    {
        "id": 567,
        "title": {
            "romaji": "One Piece"
        },
        "description": "A story about pirates...",
        "genres": ["Action", "Adventure"]
    }
]
```
## Dependencies
## Install all dependencies using the command:

```bash
pip install -r requirements.txt
```

# Contact
For queries, feel free to reach out:

# Email:
```bash
ayush952877@gmail.com
```
# GitHub: 
```bash
ayushtyagii619
```
