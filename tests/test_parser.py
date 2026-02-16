"""
Unit tests for the HealthKitParser class
"""

import unittest
from datetime import datetime
from healthkit_xml_reader.parser import HealthKitParser
from healthkit_xml_reader.models import HealthRecord


class TestHealthKitParser(unittest.TestCase):
    """Test cases for HealthKitParser"""
    
    def setUp(self):
        """Set up test fixtures before each test method"""
        # You'll need to create a sample XML file for testing
        # For now, we'll use a placeholder path
        self.sample_xml_path = 'tests/fixtures/sample_export.xml'
    
    def test_parser_initialization(self):
        """Test that parser initializes correctly"""
        parser = HealthKitParser(self.sample_xml_path)
        self.assertEqual(parser.xml_file_path, self.sample_xml_path)
        self.assertIsNone(parser.tree)
        self.assertIsNone(parser.root)
    
    def test_parse_date(self):
        """Test date parsing utility function"""
        # Test valid date string
        date_str = "2024-02-15 10:30:00 -0500"
        result = HealthKitParser._parse_date(date_str)
        self.assertIsInstance(result, datetime)
        
        # Test None input
        result = HealthKitParser._parse_date(None)
        self.assertIsNone(result)
        
        # Test invalid date string
        result = HealthKitParser._parse_date("invalid-date")
        self.assertIsNone(result)
    
    def test_load_xml_file_not_found(self):
        """Test that FileNotFoundError is raised for missing file"""
        parser = HealthKitParser('nonexistent_file.xml')
        
        with self.assertRaises(FileNotFoundError):
            parser.load_xml()
    
    # TODO: Add more tests once you have sample XML data
    # - test_parse_records()
    # - test_parse_workouts()
    # - test_get_record_types()
    # - test_filter_by_record_type()


if __name__ == '__main__':
    unittest.main()