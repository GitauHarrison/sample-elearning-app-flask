![GitHub Open Issues](https://img.shields.io/github/issues/GitauHarrison/somaSOMA-online-school-using-flask) ![GitHub Closed Issues](https://img.shields.io/github/issues-closed/GitauHarrison/somaSOMA-online-school-using-flask) ![GitHub Pull Request Open](https://img.shields.io/github/issues-pr/GitauHarrison/somaSOMA-online-school-using-flask) ![GitHub Pull Request Closed](https://img.shields.io/github/issues-pr-closed/GitauHarrison/somaSOMA-online-school-using-flask) ![GitHub forks](https://img.shields.io/github/forks/GitauHarrison/somaSOMA-online-school-using-flask) ![GitHub Stars](https://img.shields.io/github/stars/GitauHarrison/somaSOMA-online-school-using-flask)

# somaSOMA Online School

_This is the third and final iteration of the somaSoma elearning app. The original application can be seen on [this repo](https://github.com/GitauHarrison/somasoma-eLearning-app). A project started while at [Moringa School](https://moringaschool.com/) with my friends [Mark Mwaura](https://github.com/Markmwaura) and [Alexona Kinuthia](https://github.com/muirurikin), I finally have a complete demo of the vision we had. This is a demo, though there are a handful other live versions I have built._

## Overview

Built with love and from experience, this demo project summarizes the ideas that may be pivotal to any learning center, especially if conducted online. It covers the needs of four types of users:

- Administrators:
    - You control who uses the platform, by registering them, managing their data, temporarily deactivating users or permanently deleting them and their data.
    - You get a bird's eye view of the entire business: what teachers are doing, what students are doing, what paretnts have to say
    - You manage lesson contents by uploading them to the platform

- Teachers:
    - Tasked with guiding students through the lessons
    - They mark students' attendance, compounded to ratify each student's participation.
    - They assess their submitted lesson projects
    - They grade students projects

- Parents:
    - They register their children once approved by the admin. Done so so that student information is accurate.
    - They see how well their child's attendance has been
    - They get to see how they perform in each chapter

- Students:
    - They have access to lessons
    - They are required to complete the lessons in the order they appear
    - Access to subsequent lessons is dependant on the performance on the current chapter/lesson


### Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Additional Details](#additional-details)
- [Application Details](#application-details)
    - [Newsletter](#newsletter)
    - [Multi-user Support](#multi-user-support)
- [Testing It Locally](#testing-it-locally)
- [Areas of Improvement](#areas-of-improvement)


## Features

- Multi-user support
- Newsletter subscription
- Basic user authentication
- Two-factor authentication
- Sending of emails from the app


## Technologies Used

- Flask micro-framework
- Python for programming
- Sprinkles of JavaScript for front-end design
- Twilio Verify API for two-factor authentication
- Twilio SendGrid for email support
- Gunicorn for live app deployment
- Phonenumbers package for beautiful phone numbers
- DatatableJS for interactive tables
- Pytest and pytest-cov for testing
- Psycopg2 for postgresql adaptability
- Postgresql database or fallback to SQLite database
- Flask-sqlalchemy ORM for database management
- Flask-migrate for database migrations
- Flask-moment for time formatting


## Additional Details

| Db Schema Design | UI Design   | Deployment | Contributors    | Tests    |
| --------------- | ------   | ---------- | --------------- | -------- |
| [drawSQL](https://drawsql.app/teams/gitau-harrison/diagrams/sample-elearning-app)        | [Figma](https://www.figma.com/proto/iHXb2ynMTIyelCqlVAk30u/Lean-Sigma?node-id=1%3A2&scaling=min-zoom&page-id=0%3A1&starting-point-node-id=1%3A2) | [Render](https://somasoma.onrender.com)     | [GitHub](https://github.com/GitauHarrison/sample-elearning-app/graphs/contributors)        | [Tests](test_app.py) |


## Application Details

### Newsletter:

- A user interested in receiving periodic updates about somaSOMA can sign up for the newsletter service.
- Registration is limited to those who verify their email addresses only
![How newsletter works](/app/static/images/readme/how_newsletter_works.gif)
- The application automatically sends pre-prepared emails to them at set intervals
![Regular emails](/app/static/images/readme/periodic_emails.gif)
- Admin can email an individual newsletter subscriber to enhance one-on-one communication (optional)
![Admin talks with subscriber](/app/static/images/readme/admin_talks_with_subscriber.gif)


### Multi-user Support

>The application features a **superadmin**, who cannot be deleted. This superadmin is the source of all activities in the app. For example:
>
>- All teachers are added by the superadmin
>- Other admins, with limited powers, are also added by the superadmin
>
>To login as a superadmin, you can use this credentials:
>
>- Visit: **https://somasoma.onrender.com/login**
>- Username: **tastebolder**
>- Password: **somaSOMA123**

- Parent Registration (anonymous user can register as a parent)
    - Done from the home page **https://somasoma.onrender.com/register**
    ![Register parent](/app/static/images/readme/register_parent.gif)

- Student Registration (done ONLY by a registered parent - designed so to allow for their association)
    - Done from the logged-in parent's account **https://somasoma.onrender.com/register/student**
    ![Register student](/app/static/images/readme/register_student.gif)
    - An email will be sent to the student to check their login details
    ![Student login details](/app/static/images/readme/student_login_details.gif)

- Teacher Registration (done only by a logged in admin - not necessarily the superadmin)
    - Done from the logged-in admin's account **https://somasoma.onrender.com/register/teacher**
    ![Register teacher](/app/static/images/readme/register_teacher.gif)
    - An email will be sent to the teacher to check their login details
    ![Teacher login details](/app/static/images/readme/teacher_login_details.gif)

- Other admin registration (done only by a logged in admin - not necessarily the superadmin)
    - Done from the logged-in admin's account **https://somasoma.onrender.com/register/admin**
    ![Register admin](/app/static/images/readme/register_admin.gif)
    - An email will be sent to the admin to check their login details
    ![Teacher login details](/app/static/images/readme/admin_login_details.gif)

## Testing It Locally

- Clone this repo:

    ```python
    $ git clone git@github.com:GitauHarrison/somaSOMA-online-school-using-flask.git
    ```
- Change directory into the cloned repo:

    ```python
    $ cd somaSOMA-online-school-using-flask
    ```
- Create and activate a virtual environment

    ```python
    # Using virtualenvwrapper
    $ mkvirtualenv venv

    # Normal way
    $ python3 -m venv venv
    $ source venv/bin/activate
    ```

- Install needed dependancies:

    ```python
    (venv)$ pip3 install -r requirements.txt
    ```

- Add and update environment variables in a `.env` file as seen in `.env-template`:

    ```python
    (venv)$ cp .env-template .env
    ```

- Start the flask server:

    ```python
    (venv)$ flask run
    ```

- Check the application in your favourite browser by pasting http://127.0.0.1:5000.


## Areas of Improvement

- Notifications of activities taking place within the app
- Capture user gender during registration to help define how to send an email(Mr. or Ms.)
- Other user's can request to delete their own accounts
- Restricted access to subsequent chapters by students unless passmark is achieved
- Marking of students attendance by teachers
- Addition of student project quizzes to be assessed by teachers
- Display of student performance in each chapter on students and parents' profile pages
- Display of graphs to indicate student performance, student enrollment, account activities etc
- Use of blueprints and factory function
- Threading of the process of sending emails to make the app faster (you will notice the app slow down when sending emails)

**NOTE**: The above mentioned features are things I have implemented in other live and in-use applications

[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com) [![forthebadge](https://forthebadge.com/images/badges/uses-js.svg)](https://forthebadge.com)