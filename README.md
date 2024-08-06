# Pixture - DRF API
This is the backend API for Pixture, a social media application similar to Instagram, built using Django Rest Framework (DRF). The API provides endpoints for user profiles, posts, likes, comments, and followers.

The live link can be found here - <https://pixture-drf-2d68c7f0119f.herokuapp.com/>

## Table of Contents

- Features
- Installation
- Usage
- API Endpoints
- Manual Testing
- Database
- Technologies used
- Credits

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

### Entity Relationship Diagram
![ERD](https://github.com/AlexSunner/drf-pixture/blob/main/readme_images/ERD.jpg?raw=true)
### Models and CRUD Breakdown
A detailed breakdown of models within the backend:
| Model         | Endpoints                      | Create | Retrieve | Update | Delete |
| ------------- | ------------------------------ | ------ | -------- | ------ | ------ |
| Profile       | /profiles                      | Yes    | Yes      | Yes    | No     |
| Post          | /posts                         | Yes    | Yes      | Yes    | Yes    |
| Comment       | /comments                      | Yes    | Yes      | Yes    | Yes    |
| Like          | /likes                         | Yes    | No       | No     | Yes    |
| Followers     | /followers                     | Yes    | Yes      | No     | Yes    |
| Audit Logs    | /audit_logs                    | Yes    | Yes      | Yes    | Yes    |

## API Endpoints
### Profile Endpoints
- **Create Profile (`POST /profiles`)**: Create a new profile.
- **Retrieve Profile (`GET /profiles/{id}`)**: Get details of a specific profile.
- **Update Profile (`PUT /profiles/{id}`)**: Update an existing profile.

### Post Endpoints
- **Create Post (`POST /posts`)**: Create a new post.
- **Retrieve Post (`GET /posts/{id}`)**: Get details of a specific post.
- **Update Post (`PUT /posts/{id}`)**: Update an existing post.
- **Delete Post (`DELETE /posts/{id}`)**: Remove a specific post.

### Comment Endpoints
- **Create Comment (`POST /comments`)**: Add a new comment to a post.
- **Retrieve Comment (`GET /comments/{id}`)**: Get details of a specific comment.
- **Update Comment (`PUT /comments/{id}`)**: Update an existing comment.
- **Delete Comment (`DELETE /comments/{id}`)**: Remove a specific comment.

### Like Endpoints
- **Create Like (`POST /likes`)**: Like a post.
- **Delete Like (`DELETE /likes/{id}`)**: Unlike a post.

### Follow Endpoints
- **Create Follow (`POST /follows`)**: Follow a user.
- **Retrieve Follow (`GET /follows/{id}`)**: Get follow details.
- **Delete Follow (`DELETE /follows/{id}`)**: Unfollow a user.

### Audit Logs Endpoints
- **List Audit Logs (`GET /audit_logs`)**: Retrieve a list of all audit logs.
- **Retrieve Audit Log (`GET /audit_logs/{id}`)**: Retrieve details of a specific audit log by ID.
- **Create Audit Log (`POST /audit_logs/`)**: Create a new audit log entry.
- **Update Audit Log (`PUT /audit_logs/{id}/`)**: Update a specific audit log entry by ID. This can only be done as a Superuser.
- **Delete Audit Log (`DELETE /audit_logs/{id}/`)**: Delete a specific audit log entry by ID. This can only be done as a Superuser.

## Error Handling
The API uses standard HTTP status codes to indicate the success or failure of an API request:
- `200 OK`: Successful request.
- `201 Created`: Resource created successfully.
- `400 Bad Request`: The server cannot process the request due to client error.
- `401 Unauthorized`: Authentication is required and has failed or not been provided.
- `403 Forbidden`: The user does not have the necessary permissions.
- `404 Not Found`: The requested resource is not found.

## Manual Testing

### Profile Endpoints Test Cases

#### TC1: List Profiles as Logged Out User
**Description**: Verify that logged-out users can list all profiles.
**Preconditions**: User is not logged in.
**Steps**:
1. Navigate to the profiles listing page.
**Expected Result**: The user can see a list of profiles without being prompted to log in.
**Actual Result**: The user sees a list of profiles without login requirements.

#### TC2: Retrieve Profile as Logged Out User
**Description**: Verify that logged-out users can retrieve a specific profile.
**Preconditions**: User is not logged in. Have a valid profile ID.
**Steps**:
1. Navigate to the detail view of a profile using its valid ID.
**Expected Result**: The user can view the profile details without being prompted to log in.
**Actual Result**: The profile details are visible to the user without login.

#### TC3: Update Profile as Logged In User
**Description**: Verify that logged-in users can update their own profile.
**Preconditions**: User is logged in.
**Steps**:
1. Navigate to the edit page of their profile.
2. Make changes to the profile's details.
3. Submit the updates.
**Expected Result**: The profile is updated successfully, and the user sees the updated profile view.
**Actual Result**: The profile update is successful, and the changes are reflected.

#### TC4: Attempt Update on Another User's Profile
**Description**: Verify that logged-in users cannot update profiles they do not own.
**Preconditions**: User is logged in and does not own the profile they attempt to edit.
**Steps**:
1. Attempt to navigate to the edit page of a profile not owned by the user.
**Expected Result**: The user is denied access indicating they do not have permission to edit the profile.
**Actual Result**: The user is denied access to edit the profile.

### Post Endpoints Test Cases

#### TC1: List Posts as Logged Out User
**Description**: Verify that logged-out users can list all posts.
**Preconditions**: User is not logged in.
**Steps**:
1. Navigate to the posts listing page.
**Expected Result**: The user can see a list of posts without being prompted to log in.
**Actual Result**: The user sees a list of posts without login requirements.

#### TC2: Create Post as Logged In User
**Description**: Verify that logged-in users can create a new post.
**Preconditions**: User is logged in.
**Steps**:
1. Navigate to the create post page.
2. Fill in the required fields for creating a post.
3. Submit the form to create a new post.
**Expected Result**: The post is created successfully, and the user is redirected to the post's detail view.
**Actual Result**: The post creation is successful.

#### TC3: Attempt Post Creation as Logged Out User
**Description**: Verify that logged-out users cannot create a post.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the create post page.
**Expected Result**: The user should not have access to create a post.
**Actual Result**: The user can not create a post.

#### TC4: Retrieve Post with Valid ID as Logged Out User
**Description**: Verify that logged-out users can retrieve a post using a valid ID.
**Preconditions**: User is not logged in. Have a valid post ID.
**Steps**:
1. Navigate to the detail view of a post using its valid ID.
**Expected Result**: The user can view the post details without being prompted to log in.
**Actual Result**: The post details are visible to the user without login.

#### TC5: Attempt Retrieval of Post with Invalid ID as Logged Out User
**Description**: Verify that logged-out users cannot retrieve a post using an invalid ID.
**Preconditions**: User is not logged in. Have an invalid post ID.
**Steps**:
1. Attempt to navigate to the detail view of a post using an invalid ID.
**Expected Result**: The user receives a 404 Not Found error.
**Actual Result**: The user encounters a 404 Not Found error.

#### TC6: Update Own Post as Logged In User
**Description**: Verify that logged-in users can update a post they own.
**Preconditions**: User is logged in and owns at least one post.
**Steps**:
1. Navigate to the edit page of a post owned by the user.
2. Make changes to the post's content.
3. Submit the updates.
**Expected Result**: The post is updated successfully, and the user is redirected to the post's updated detail view.
**Actual Result**: The post update is successful, and the changes are reflected.

#### TC7: Attempt Update on Post Not Owned by Logged In User
**Description**: Verify that logged-in users cannot update posts they do not own.
**Preconditions**: User is logged in and does not own the post they attempt to edit.
**Steps**:
1. Attempt to navigate to the edit page of a post not owned by the user.
**Expected Result**: The user is prevented from accessing the edit page indicating they do not have permission to edit the post.
**Actual Result**: The user is denied access to edit the post.

#### TC8: Delete Own Post as Logged In User
**Description**: Verify that logged-in users can delete a post they own.
**Preconditions**: User is logged in and owns at least one post.
**Steps**:
1. Navigate to the delete page of a post owned by the user.
2. Confirm the deletion.
**Expected Result**: The post is deleted successfully, and the user is redirected to the post list view.
**Actual Result**: The post deletion is successful.

#### TC9: Attempt Delete on Post Not Owned by Logged In User
**Description**: Verify that logged-in users cannot delete posts they do not own.
**Preconditions**: User is logged in and does not own the post they attempt to delete.
**Steps**:
1. Attempt to navigate to the delete page of a post not owned by the user.
**Expected Result**: The user is denied access indicating they do not have permission to delete the post.
**Actual Result**: The user is denied access to delete the post.

### Comment Endpoints Test Cases

#### TC1: List Comments as Logged Out User
**Description**: Verify that logged-out users can list all comments.
**Preconditions**: User is not logged in.
**Steps**:
1. Navigate to the comments listing page.
**Expected Result**: The user can see a list of comments without being prompted to log in.
**Actual Result**: The user sees a list of comments without login requirements.

#### TC2: Create Comment as Logged In User
**Description**: Verify that logged-in users can create a new comment.
**Preconditions**: User is logged in.
**Steps**:
1. Navigate to the create comment page.
2. Fill in the required fields for creating a comment.
3. Submit the form to create a new comment.
**Expected Result**: The comment is created successfully, and the user is redirected to the comment's detail view.
**Actual Result**: The comment creation is successful.

#### TC3: Attempt Comment Creation as Logged Out User
**Description**: Verify that logged-out users cannot create a comment.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the create comment page.
**Expected Result**: The user should not be able to create a comment.
**Actual Result**: The user can not create a comment.

#### TC4: Retrieve Comment with Valid ID as Logged Out User
**Description**: Verify that logged-out users can retrieve a comment using a valid ID.
**Preconditions**: User is not logged in. Have a valid comment ID.
**Steps**:
1. Navigate to the detail view of a comment using its valid ID.
**Expected Result**: The user can view the comment details without being prompted to log in.
**Actual Result**: The comment details are visible to the user without login.

#### TC5: Attempt Retrieval of Comment with Invalid ID as Logged Out User
**Description**: Verify that logged-out users cannot retrieve a comment using an invalid ID.
**Preconditions**: User is not logged in. Have an invalid comment ID.
**Steps**:
1. Attempt to navigate to the detail view of a comment using an invalid ID.
**Expected Result**: The user receives a 404 Not Found error.
**Actual Result**: The user encounters a 404 Not Found error.

#### TC6: Update Own Comment as Logged In User
**Description**: Verify that logged-in users can update a comment they own.
**Preconditions**: User is logged in and owns at least one comment.
**Steps**:
1. Navigate to the edit page of a comment owned by the user.
2. Make changes to the comment's content.
3. Submit the updates.
**Expected Result**: The comment is updated successfully, and the user is redirected to the comment's updated detail view.
**Actual Result**: The comment update is successful, and the changes are reflected.

#### TC7: Attempt Update on Comment Not Owned by Logged In User
**Description**: Verify that logged-in users cannot update comments they do not own.
**Preconditions**: User is logged in and does not own the comment they attempt to edit.
**Steps**:
1. Attempt to navigate to the edit page of a comment not owned by the user.
**Expected Result**: The user is prevented from accessing the edit page indicating they do not have permission to edit the comment.
**Actual Result**: The user is denied access to edit the comment.

#### TC8: Delete Own Comment as Logged In User
**Description**: Verify that logged-in users can delete a comment they own.
**Preconditions**: User is logged in and owns at least one comment.
**Steps**:
1. Navigate to the delete page of a comment owned by the user.
2. Confirm the deletion.
**Expected Result**: The comment is deleted successfully, and the user is redirected to the comment list view.
**Actual Result**: The comment deletion is successful.

#### TC9: Attempt Delete on Comment Not Owned by Logged In User
**Description**: Verify that logged-in users cannot delete comments they do not own.
**Preconditions**: User is logged in and does not own the comment they attempt to delete.
**Steps**:
1. Attempt to navigate to the delete page of a comment not owned by the user.
**Expected Result**: The user is denied access indicating they do not have permission to delete the comment.
**Actual Result**: The user is denied access to delete the comment.

### Like Endpoints Test Cases

#### TC1: List Likes as Logged Out User
**Description**: Verify that logged-out users can list likes.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the likes listing page.
**Expected Result**: The user should see a list of likes.
**Actual Result**: The user sees a list of likes.

#### TC2: Create Like as Logged In User
**Description**: Verify that logged-in users can create a new like.
**Preconditions**: User is logged in.
**Steps**:
1. Navigate to the create like page.
2. Select the post to like.
3. Submit the form to create a new like.
**Expected Result**: The like is created successfully, and the user is redirected to the post's detail view.
**Actual Result**: The like creation is successful.

#### TC3: Attempt Like Creation as Logged Out User
**Description**: Verify that logged-out users cannot create a like.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the create like page.
**Expected Result**: The user should not be able to create a like.
**Actual Result**: The user can not create a like.

#### TC4: Delete Own Like as Logged In User
**Description**: Verify that logged-in users can delete a like they own.
**Preconditions**: User is logged in and owns at least one like.
**Steps**:
1. Navigate to the delete page of a like owned by the user.
2. Confirm the deletion.
**Expected Result**: The like is deleted successfully, and the user is redirected to the post's detail view.
**Actual Result**: The like deletion is successful.

#### TC5: Attempt Delete on Like Not Owned by Logged In User
**Description**: Verify that logged-in users cannot delete likes they do not own.
**Preconditions**: User is logged in and does not own the like they attempt to delete.
**Steps**:
1. Attempt to navigate to the delete page of a like not owned by the user.
**Expected Result**: The user is denied access indicating they do not have permission to delete the like.
**Actual Result**: The user is denied access to delete the like.

### Follow Endpoints Test Cases

#### TC1: List Follows as Logged Out User
**Description**: Verify that logged-out users can list follows.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the follows listing page.
**Expected Result**: The user should see a list of followers.
**Actual Result**: The user can see a list of followers.

#### TC2: Create Follow as Logged In User
**Description**: Verify that logged-in users can create a new follow.
**Preconditions**: User is logged in.
**Steps**:
1. Navigate to the create follow page.
2. Select the user to follow.
3. Submit the form to create a new follow.
**Expected Result**: The follow is created successfully, and the user is redirected to the followed user's profile.
**Actual Result**: The follow creation is successful.

#### TC3: Attempt Follow Creation as Logged Out User
**Description**: Verify that logged-out users cannot create a follow.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the create follow page.
**Expected Result**: The user should not be able to create a follow.
**Actual Result**: The user can not create a follow.

#### TC4: Delete Own Follow as Logged In User
**Description**: Verify that logged-in users can delete a follow they own.
**Preconditions**: User is logged in and owns at least one follow.
**Steps**:
1. Navigate to the delete page of a follow owned by the user.
2. Confirm the deletion.
**Expected Result**: The follow is deleted successfully, and the user is redirected to the user's profile view.
**Actual Result**: The follow deletion is successful.

#### TC5: Attempt Delete on Follow Not Owned by Logged In User
**Description**: Verify that logged-in users cannot delete follows they do not own.
**Preconditions**: User is logged in and does not own the follow they attempt to delete.
**Steps**:
1. Attempt to navigate to the delete page of a follow not owned by the user.
**Expected Result**: The user should not be able to delete a follow.
**Actual Result**: The user is denied access to delete the follow.

### Audit Log Endpoints Test Cases

#### TC1: List Audit Logs as Logged Out User
**Description**: Verify that logged-out users can list audit logs.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the audit logs listing page.
**Expected Result**: The user can see a list of audit logs.
**Actual Result**: The user sees a list of audit logs.

#### TC2: List Audit Logs as Logged In User (Non-Superuser)
**Description**: Verify that logged-in users (non-superusers) can list audit logs.
**Preconditions**: User is logged in as a non-superuser.
**Steps**:
1. Attempt to navigate to the audit logs listing page.
**Expected Result**: The user can see a list of audit logs.
**Actual Result**: The user sees a list of audit logs.

#### TC3: List Audit Logs as Superuser
**Description**: Verify that superusers can list audit logs.
**Preconditions**: User is logged in as a superuser.
**Steps**:
1. Navigate to the audit logs listing page.
**Expected Result**: The user can see a list of audit logs.
**Actual Result**: The user sees a list of audit logs.

#### TC4: Create Audit Log as Logged In User (Non-Superuser)
**Description**: Verify that logged-in users (non-superusers) can create audit logs.
**Preconditions**: User is logged in as a non-superuser.
**Steps**:
1. Attempt to navigate to the create audit log page.
2. Fill in the required fields for creating an audit log.
3. Submit the form to create a new audit log.
**Expected Result**: The audit log is created successfully, and the user is redirected to the audit log's detail view.
**Actual Result**: The audit log creation is successful.

#### TC5: Create Audit Log as Superuser
**Description**: Verify that superusers can create a new audit log.
**Preconditions**: User is logged in as a superuser.
**Steps**:
1. Navigate to the create audit log page.
2. Fill in the required fields for creating an audit log.
3. Submit the form to create a new audit log.
**Expected Result**: The audit log is created successfully, and the user is redirected to the audit log's detail view.
**Actual Result**: The audit log creation is successful.

#### TC6: Update Audit Log as Logged In User (Non-Superuser)
**Description**: Verify that logged-in users (non-superusers) cannot update audit logs.
**Preconditions**: User is logged in as a non-superuser.
**Steps**:
1. Attempt to navigate to the edit page of an audit log.
**Expected Result**: The user is denied access.
**Actual Result**: The user is denied access to edit the audit log.

#### TC7: Update Audit Log as Superuser
**Description**: Verify that superusers can update an audit log.
**Preconditions**: User is logged in as a superuser.
**Steps**:
1. Navigate to the edit page of an audit log.
2. Make changes to the audit log's details.
3. Submit the updates.
**Expected Result**: The audit log is updated successfully, and the user is redirected to the audit log's updated detail view.
**Actual Result**: The audit log update is successful, and the changes are reflected.

#### TC8: Delete Audit Log as Logged In User (Non-Superuser)
**Description**: Verify that logged-in users (non-superusers) cannot delete audit logs.
**Preconditions**: User is logged in as a non-superuser.
**Steps**:
1. Attempt to navigate to the delete page of an audit log.
**Expected Result**: The user is denied access.
**Actual Result**: The user is denied access to delete the audit log.

#### TC9: Delete Audit Log as Superuser
**Description**: Verify that superusers can delete an audit log.
**Preconditions**: User is logged in as a superuser.
**Steps**:
1. Navigate to the delete page of an audit log.
2. Confirm the deletion.
**Expected Result**: The audit log is deleted successfully, and the user is redirected the audit log list view.
**Actual Result**: The audit log deletion is successful.

#### TC10: Create Audit Log as Logged Out User
**Description**: Verify that logged-out users cannot create an audit log.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the create audit log page.
**Expected Result**: The logged out user should not be able to post audit logs.
**Actual Result**: The user can not post audit logs.

#### TC11: Update Audit Log as Logged Out User
**Description**: Verify that logged-out users cannot update an audit log.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the edit page of an audit log.
**Expected Result**: The logged out user should not be able to update audit logs.
**Actual Result**: The user can not update audit logs.

#### TC12: Delete Audit Log as Logged Out User
**Description**: Verify that logged-out users cannot delete an audit log.
**Preconditions**: User is not logged in.
**Steps**:
1. Attempt to navigate to the delete page of an audit log.
**Expected Result**: The logged out user should not be able to delete audit logs.
**Actual Result**: The user can not delete audit logs.


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

