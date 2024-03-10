#!/usr/bin/python3
"""Test script for the Amenity model."""

from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(TestBaseModel):
    """Test class for the Amenity model."""

    def __init__(self, *args, **kwargs):
        """Initialize test_Amenity."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.model = Amenity

    def test_amenity_name(self):
        """Test the 'name' attribute of the Amenity model."""
        new_instance = self.model()
        self.assertEqual(type(new_instance.name), str)
