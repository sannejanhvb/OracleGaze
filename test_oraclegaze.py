# test_oraclegaze.py
"""
Tests for OracleGaze module.
"""

import unittest
from oraclegaze import OracleGaze

class TestOracleGaze(unittest.TestCase):
    """Test cases for OracleGaze class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OracleGaze()
        self.assertIsInstance(instance, OracleGaze)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OracleGaze()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
