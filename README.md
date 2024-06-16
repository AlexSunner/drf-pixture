# Pixture - DRF API
This is the backend API for Pixture, a social media application similar to Instagram, built using Django Rest Framework (DRF). The API provides endpoints for user profiles, posts, likes, comments, and followers.

The live link can be found here - <https://pixture-drf-2d68c7f0119f.herokuapp.com/>

## Table of Contents

- Features
- Installation
- Usage
- API Endpoints
- Database
- Technologies used
- Credits
- Tests

## Features

- User authentication and authorization
- Operations for user profiles
- Operations for posts
- Like and unlike posts
- Comment on posts
- Follow and unfollow users
- Admin Panel
- Custom model "Admin Logs" for tracking admin actions

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/AlexSunner/drf-pixture.git

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
### Root Route
![Root Route](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/rootroute.jpg?raw=true)
### Profiles
* `GET /profiles/ - List all profiles`
![Append /profiles](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendprofiles.jpg?raw=true)

* `GET /profiles/<user_id>/ - Retrieve a specific user profile`
![Append /profiles/<user_id>](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendid.jpg?raw=true)


### Posts
* `GET /posts/ - List all posts`
![Append /posts](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendposts.jpg?raw=true)

* `GET /posts/<post_id>/ - Retrieve a specific post`
![Append /posts/<post_id>](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendpostsid.jpg?raw=true)

* `POST /posts/ - Create a new post`
![Put a POST request to add new post](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/putpost.jpg?raw=true)


### Likes
* `GET /likes/ - List all likes`
![Append /likes/](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendlikes.jpg?raw=true)

* `POST /likes/ - Like a post`
![Like a post](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/putlike.jpg?raw=true)


### Comments
* `GET /comments/ - List all comments`
![Append /comments/](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendcomments.jpg?raw=true)

* `GET /comments/<comment_id>/ - Retrieve a specific comment`

* `POST /comments/ - Comment on a post`

* `PUT /comments/<comment_id>/ - Update a comment`

* `DELETE /comments/<comment_id>/ - Delete a comment`
![Comment edit](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/putcomment.jpg?raw=true)

### Followers
* `GET /followers/ - List all followers`
![Append /followers](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/appendfollowers.jpg?raw=true)

* `POST /followers/ - Follow a user`

* `DELETE /followers/<follower_id>/ - Unfollow a user`

### Django Admin Panel
The project includes a robust Django admin panel for managing the application's data and configurations. Through the admin panel, administrators can easily perform CRUD operations on user profiles, posts, likes, comments, and followers. Additionally, the admin panel provides access to custom admin logs, allowing administrators to track and audit all actions performed within the panel, ensuring transparency and accountability.

To access the admin panel, navigate to `/admin` and log in using your superuser credentials.
![admin panel](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/adminsite.jpg?raw=true)

A custom model called Admin Logs is implemented to keep track of actions performed by administrators.
This feature logs the following information:

* Admin user: The admin who performed the action
* Action: The specific action performed (e.g., create, update, delete)
* Timestamp: The timestamp of the action
* Model affected: The model on which the action was performed (e.g., user, post)
* Object ID: The ID of the affected object

This log is accessible through the Django admin panel and provides valuable insights into administrative activities for auditing and monitoring purposes.
![Admin Logs](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/adminlog.jpg?raw=true)

![Admin log details](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/adminlogdetails.jpg?raw=true)

Another custom model called Audit Log is implemented to keep track of posts created by users.

![Audit Log](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/auditlog.jpg?raw=true)

## Technologies Used
- Python
- Django 5.0.6
- Django Rest Framework (DRF)
- Django Allauth
- Django Rest Auth
- Django Filter
- Django CORS Headers
- Django Cloudinary Storage
- Cloudinary
- Django Simple JWT
- Gunicorn
- PostgreSQL (via Psycopg2)
- Pillow
- Whitenoise
- OAuthlib
- Requests-OAuthlib
- SQLParse
- ASGIRef
- The API uses an [ElephantSQL](https://www.elephantsql.com/) database to store data.

## Credits
- This project was created as part of my Portfolio Project 5 while following the "Django Rest Framework" walkthrough tutorial. The tutorial provided invaluable guidance and insights into building a robust backend API using Django and Django Rest Framework. A significant portion of the code in this project, including the serializers, settings, and the followers, profiles, posts, likes, and comments apps, is heavily based on or directly taken from the walkthrough tutorial. Special thanks to the tutorial creators for their easy-to-follow instructions.

## Acknowledgment
- I am fully aware that this project currently lacks both manual and automated testing. Due to time constraints, I was unable to implement these tests. Comprehensive testing is crucial for ensuring the reliability and robustness of the application. Future updates will include unit tests, integration tests, and end-to-end tests to enhance the stability and maintainability of the codebase.

