#!/usr/bin/python3
"""Test script for the Review model."""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Test class for the Review model."""

    def __init__(self, *args, **kwargs):
        """Initialize test_review."""
        super().__init__(*args, **kwargs)
        self.model_name = "Review"
        self.model_instance = Review

    def test_place_id(self):
        """Test the place_id attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.place_id), str)

    def test_user_id(self):
        """Test the user_id attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.user_id), str)

    def test_text(self):
        """Test the text attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.text), str)
