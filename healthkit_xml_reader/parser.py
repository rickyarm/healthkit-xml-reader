"""
Core XML parsing functionality for HealthKit export files
"""

import xml.etree.ElementTree as ET
from typing import List, Dict, Optional
from datetime import datetime
from .models import HealthRecord, Workout, ActivitySummary


class HealthKitParser:
    """
    Main parser class for Apple HealthKit export.xml files
    
    Usage:
        parser = HealthKitParser('export.xml')
        records = parser.parse_records()
    """
    
    def __init__(self, xml_file_path: str):
        """
        Initialize parser with path to export.xml file
        
        Args:
            xml_file_path: Path to the Apple Health export.xml file
        """
        self.xml_file_path = xml_file_path
        self.tree = None
        self.root = None
        
    def load_xml(self) -> None:
        """
        Load and parse the XML file
        
        Raises:
            FileNotFoundError: If XML file doesn't exist
            ET.ParseError: If XML is malformed
        """
        try:
            self.tree = ET.parse(self.xml_file_path)
            self.root = self.tree.getroot()
        except FileNotFoundError:
            raise FileNotFoundError(f"XML file not found: {self.xml_file_path}")
        except ET.ParseError as e:
            raise ET.ParseError(f"Failed to parse XML: {e}")
    
    def parse_records(self, record_type: Optional[str] = None) -> List[HealthRecord]:
        """
        Parse health records from the XML file
        
        Args:
            record_type: Optional filter for specific record type 
                        (e.g., 'HKQuantityTypeIdentifierStepCount')
        
        Returns:
            List of HealthRecord objects
        """
        if self.root is None:
            self.load_xml()
        
        records = []
        
        # Find all Record elements in the XML
        for record_elem in self.root.findall('.//Record'):
            # Get attributes from the XML element
            attrs = record_elem.attrib
            
            # Filter by type if specified
            if record_type and attrs.get('type') != record_type:
                continue
            
            # Create HealthRecord object from XML attributes
            record = HealthRecord(
                record_type=attrs.get('type'),
                source_name=attrs.get('sourceName'),
                value=attrs.get('value'),
                unit=attrs.get('unit'),
                start_date=self._parse_date(attrs.get('startDate')),
                end_date=self._parse_date(attrs.get('endDate')),
                creation_date=self._parse_date(attrs.get('creationDate'))
            )
            records.append(record)
        
        return records
    
    def parse_workouts(self) -> List[Workout]:
        """
        Parse workout data from the XML file
        
        Returns:
            List of Workout objects
        """
        if self.root is None:
            self.load_xml()
        
        workouts = []
        
        # Find all Workout elements
        for workout_elem in self.root.findall('.//Workout'):
            attrs = workout_elem.attrib
            
            workout = Workout(
                workout_type=attrs.get('workoutActivityType'),
                duration=float(attrs.get('duration', 0)),
                duration_unit=attrs.get('durationUnit'),
                total_distance=float(attrs.get('totalDistance', 0)) if attrs.get('totalDistance') else None,
                total_energy_burned=float(attrs.get('totalEnergyBurned', 0)) if attrs.get('totalEnergyBurned') else None,
                source_name=attrs.get('sourceName'),
                start_date=self._parse_date(attrs.get('startDate')),
                end_date=self._parse_date(attrs.get('endDate'))
            )
            workouts.append(workout)
        
        return workouts
    
    def get_record_types(self) -> List[str]:
        """
        Get a list of all unique record types in the XML file
        
        Returns:
            List of record type strings
        """
        if self.root is None:
            self.load_xml()
        
        record_types = set()
        for record in self.root.findall('.//Record'):
            record_type = record.attrib.get('type')
            if record_type:
                record_types.add(record_type)
        
        return sorted(list(record_types))
    
    @staticmethod
    def _parse_date(date_string: Optional[str]) -> Optional[datetime]:
        """
        Parse ISO format date string to datetime object
        
        Args:
            date_string: ISO format date string
        
        Returns:
            datetime object or None if parsing fails
        """
        if not date_string:
            return None
        
        try:
            # Apple Health uses ISO 8601 format with timezone
            # Example: "2024-02-15 10:30:00 -0500"
            return datetime.fromisoformat(date_string.replace(' ', 'T', 1))
        except (ValueError, AttributeError):
            return None