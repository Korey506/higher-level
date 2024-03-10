#!/usr/bin/python3
"""Test script for the User model."""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Test class for the User model."""

    def __init__(self, *args, **kwargs):
        """Initialize test_User."""
        super().__init__(*args, **kwargs)
        self.model_name = "User"
        self.model_instance = User

    def test_first_name(self):
        """Test the first_name attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.first_name), str)

    def test_last_name(self):
        """Test the last_name attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.last_name), str)

    def test_email(self):
        """Test the email attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.email), str)

    def test_password(self):
        """Test the password attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.password), str)
