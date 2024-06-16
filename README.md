# Pixture - DRF API
This is the backend API for Pixture, a social media application similar to Instagram, built using Django Rest Framework (DRF). The API provides endpoints for user profiles, posts, likes, comments, and followers.

The live link can be found here - <https://pixture-drf-2d68c7f0119f.herokuapp.com/>

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication and authorization
- CRUD operations for user profiles
- CRUD operations for posts
- Like and unlike posts
- Comment on posts
- Follow and unfollow users
- Custom admin logs to track admin actions

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/social-media-api.git
   cd social-media-api

2. Install the required dependencies:
    ```
    pip install -r requirements.txt

3. Set up the database:
    ```
    python3 manage.py migrate

4. Create a superuser to access the admin panel:
    ```
    python3 manage.py createsuperuser

5. Run the development server:
    ```
    python3 manage.py runserver

## Usage
To use the API, you need to have the server running. You can interact with the API using tools like Postman or through the frontend React application.
Additionally, you can use the deployed version of the API with this link [Pixture API](https://pixture-drf-2d68c7f0119f.herokuapp.com/)

## API Endpoints
### Profiles
* `GET /profiles/ - List all profiles`
![Append /profiles](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendprofiles.jpg?raw=true)

* `GET /profiles/<user_id>/ - Retrieve a specific user profile`
![Append /profiles/<user_id>](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendid.jpg?raw=true)


### Posts
* `GET /posts/ - List all posts`

* `GET /posts/<post_id>/ - Retrieve a specific post`

* `POST /posts/ - Create a new post`
* `PUT /posts/<post_id>/ - Update a post`
* `DELETE /posts/<post_id>/ - Delete a post`

### Likes
* `GET /likes/ - List all likes`

* `POST /likes/ - Like a post`

* `DELETE /likes/<like_id>/ - Unlike a post`

### Comments
* `GET /comments/ - List all comments`

* `GET /comments/<comment_id>/ - Retrieve a specific comment`

* `POST /comments/ - Comment on a post`

* `PUT /comments/<comment_id>/ - Update a comment`

* `DELETE /comments/<comment_id>/ - Delete a comment`

### Followers
* `GET /followers/ - List all followers`

* `POST /followers/ - Follow a user`

* `DELETE /followers/<follower_id>/ - Unfollow a user`

## Database
The API uses an [ElephantSQL](https://www.elephantsql.com/) database to store data.
