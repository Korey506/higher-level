#!/usr/bin/python3
"""Test script for the State model."""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Test class for the State model."""

    def __init__(self, *args, **kwargs):
        """Initialize test_state."""
        super().__init__(*args, **kwargs)
        self.model_name = "State"
        self.model_instance = State

    def test_name(self):
        """Test the name attribute."""
        new_instance = self.model_instance()
        self.assertEqual(type(new_instance.name), str)
