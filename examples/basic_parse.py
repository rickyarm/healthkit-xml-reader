"""
Basic example of parsing Apple Health export.xml file

This example shows how to:
1. Load an XML file
2. Parse health records
3. Display basic information
"""

from healthkit_xml_reader import HealthKitParser
from healthkit_xml_reader.utils import simplify_record_type


def main():
    # Path to your exported Apple Health data
    # Update this path to point to your actual export.xml file
    xml_file = 'path/to/your/export.xml'
    
    # Create parser instance
    print("Loading HealthKit data...")
    parser = HealthKitParser(xml_file)
    
    # Get all available record types
    print("\nAvailable record types:")
    record_types = parser.get_record_types()
    for record_type in record_types[:10]:  # Show first 10
        simplified = simplify_record_type(record_type)
        print(f"  - {simplified}")
    
    print(f"\n... and {len(record_types) - 10} more types")
    
    # Parse step count records
    print("\nParsing step count records...")
    step_records = parser.parse_records('HKQuantityTypeIdentifierStepCount')
    print(f"Found {len(step_records)} step count records")
    
    # Display first few records
    print("\nSample records:")
    for record in step_records[:5]:
        print(f"  {record.start_date}: {record.value} {record.unit} ({record.source_name})")
    
    # Parse workouts
    print("\nParsing workouts...")
    workouts = parser.parse_workouts()
    print(f"Found {len(workouts)} workouts")
    
    # Display first few workouts
    print("\nSample workouts:")
    for workout in workouts[:5]:
        print(f"  {workout.start_date}: {workout.workout_type} - {workout.duration} {workout.duration_unit}")


if __name__ == '__main__':
    main()