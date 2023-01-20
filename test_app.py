# Database configuration is imported first prior to
# all other configurations

import os
os.environ['DATABASE_URL'] = 'sqlite://'

from app import app, db
import unittest


class TestElearningApp(unittest.TestCase):

    # Application context

    def setUp(self):
        self.app = app

        # Disable csrf protection
        self.app.config['SECRET_KEY'] = 'somaSOMA'
        self.app.config['WTF_CSRF_ENABLED'] = False

        self.appctx = self.app.app_context()
        self.appctx.push()
        db.create_all() # < --- create database during setup
        self.client = self.app.test_client() # < --- test client

    def tearDown(self):
        db.drop_all() # < --- discard database after each test
        self.appctx.pop()
        self.app = None
        self.appctx = None
        self.client = None

    def test_elearning_app(self):
        assert self.app is not None
        assert app == self.app

    def test_home_page_access(self):
        ''''''
        response = self.client.get('/')
        response_home = self.client.get('/home')
        assert response.status_code == 200
        assert response_home.status_code == 200

    def test_registration_form(self):
        response = self.client.get('/register')
        assert response.status_code == 200
        html = response.get_data(as_text=True)

        # All these fields must be included
        assert 'name="first_name"' in html
        assert 'name="last_name"' in html
        assert 'name="username"' in html
        assert 'name="email"' in html
        assert 'name="password"' in html
        assert 'name="confirm_password"' in html
        assert 'name="phone_number"' in html
        assert 'name="residence"' in html
        assert 'name="register"' in html

    def test_registration_form_validation(self):
        response = self.client.post('/register', data={
            'first_name': 'test',
            'last_name': 'user',
            'username': 'testuser',
            'email': 'testuser@email.com',
            'password': 'testuser2023',
            'confirm_password': 'testuser2023',
            'phone_number': '+254700111222',
            'residence': 'Nairobi'
        })
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'Field must be equal to confirm_password' in html

    def test_parent_registration(self):
        response = self.client.post('/register', data={
            'first_name': 'test',
            'last_name': 'user',
            'username': 'testuser',
            'email': 'testuser@email.com',
            'password': 'testuser2023',
            'confirm_password': 'testuser2023',
            'phone_number': '+254700111222',
            'residence': 'Nairobi'
        }, follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == '/login' # redirected to the login page

    def test_parent_login(self):
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'testuser2023'
        }, follow_redirect=True)
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert 'Hi, testuser!' in html
