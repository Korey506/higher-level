#!/usr/bin/python3
"""Test script for the City model."""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Test class for the City model."""

    def __init__(self, *args, **kwargs):
        """Initialize test_City."""
        super().__init__(*args, **kwargs)
        self.model_name = "City"
        self.model_instance = City

    def test_state_id_attribute(self):
        """Test the state_id attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.state_id), str)

    def test_name_attribute(self):
        """Test the name attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.name), str)
