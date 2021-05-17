from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']


    @classmethod
    def add(cls,data):
        query = "INSERT INTO users (email) VALUES (%(email)s);"
        
        return connectToMySQL('email_validation').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL('email_validation').query_db(query,data)

    @staticmethod
    def validate_email(data):
        is_valid = True
        if len(data['email']) < 3:
            flash("Name must be at least 3 characters!")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']):
            flash("Email must be a valid format!")
            is_valid = False

        if EMAIL_REGEX.match(data['email']):
            flash(f"The email address you entered " + (data['email']) + " is a VALID email address! Thank you!")
            is_valid = True
        return is_valid