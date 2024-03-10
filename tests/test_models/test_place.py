#!/usr/bin/python3
"""Test script for the Place model."""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Test class for the Place model."""

    def __init__(self, *args, **kwargs):
        """Initialize test_Place."""
        super().__init__(*args, **kwargs)
        self.model_name = "Place"
        self.model_instance = Place

    def test_city_id(self):
        """Test the city_id attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.city_id), str)

    def test_user_id(self):
        """Test the user_id attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.user_id), str)

    def test_name(self):
        """Test the name attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.name), str)

    def test_description(self):
        """Test the description attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.description), str)

    def test_number_rooms(self):
        """Test the number_rooms attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.number_rooms), int)

    def test_number_bathrooms(self):
        """Test the number_bathrooms attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.number_bathrooms), int)

    def test_max_guest(self):
        """Test the max_guest attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.max_guest), int)

    def test_price_by_night(self):
        """Test the price_by_night attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.price_by_night), int)

    def test_latitude(self):
        """Test the latitude attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.latitude), float)

    def test_longitude(self):
        """Test the longitude attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.longitude), float)

    def test_amenity_ids(self):
        """Test the amenity_ids attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.amenity_ids), list)
