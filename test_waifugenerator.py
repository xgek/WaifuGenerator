# test_waifugenerator.py
"""
Tests for WaifuGenerator module.
"""

import unittest
from waifugenerator import WaifuGenerator

class TestWaifuGenerator(unittest.TestCase):
    """Test cases for WaifuGenerator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WaifuGenerator()
        self.assertIsInstance(instance, WaifuGenerator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WaifuGenerator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
