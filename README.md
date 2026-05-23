# Book Review System API
A complete Django REST Framework project for managing books and reviews, featuring secure JWT authentication and custom role-based permissions.
------------------------------------------------------------------------------------------------------------------
## Project Structure

```text
BookReviewSystem/
│
├── BookReviewSystem/       # Main project configuration folder
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── catalog/                # Main application folder
│   ├── migrations/
    ├── fixtures/
        ├── data.json
│   ├── models.py
│   ├── serializers.py
    ├── permissions.py
│   ├── urls.py
│   └── views.py
│
├── requirements.txt        # Project dependencies and libraries
└── README.md               # Project documentation
```
## How to Run the Project Locally :
Follow these steps to set up and run the project on your local machine:
git clone https://github.com/SuhaAnalystDev/BookReviewSystem.git
cd BookReviewSystem
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

## How to test each endpoint (using Postman):
You Can Check the data.json File For All the Data Testing Or Check Folder Test_images.

## Description of Authentication Mechanism used:
*
This project utilizes Simple JWT (JSON Web Token) for secure authentication and session management.
**Mechanism:** Users authenticate via their credentials to obtain an Access Token and a Refresh Token.
--
**Usage:** For protected endpoints, the Access Token must be included in the HTTP request header as a Bearer Token:
**Plaintext**
Authorization: Bearer <your_access_token>

