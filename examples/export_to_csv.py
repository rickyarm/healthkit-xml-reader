"""
Example of exporting HealthKit data to CSV format

This example shows how to:
1. Parse specific health metrics
2. Export to CSV file
3. Group data by date
"""

import csv
from datetime import datetime, timedelta
from healthkit_xml_reader import HealthKitParser
from healthkit_xml_reader.utils import group_by_date, calculate_daily_total, simplify_record_type


def export_steps_to_csv(xml_file: str, output_file: str, days: int = 30):
    """
    Export daily step counts to CSV file
    
    Args:
        xml_file: Path to export.xml
        output_file: Path for output CSV file
        days: Number of days to include (default: 30)
    """
    print(f"Parsing step data from {xml_file}...")
    
    # Parse step count records
    parser = HealthKitParser(xml_file)
    step_records = parser.parse_records('HKQuantityTypeIdentifierStepCount')
    
    # Filter to last N days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    
    recent_records = [
        r for r in step_records 
        if r.start_date and start_date <= r.start_date <= end_date
    ]
    
    print(f"Found {len(recent_records)} step records in last {days} days")
    
    # Group by date and calculate daily totals
    grouped = group_by_date(recent_records)
    
    # Write to CSV
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Total Steps', 'Record Count'])
        
        for date_str in sorted(grouped.keys()):
            records = grouped[date_str]
            total_steps = calculate_daily_total(records)
            writer.writerow([date_str, int(total_steps), len(records)])
    
    print(f"✓ Successfully exported {len(grouped)} days to {output_file}")


def export_heart_rate_to_csv(xml_file: str, output_file: str):
    """
    Export heart rate data to CSV file
    
    Args:
        xml_file: Path to export.xml
        output_file: Path for output CSV file
    """
    print(f"Parsing heart rate data from {xml_file}...")
    
    parser = HealthKitParser(xml_file)
    hr_records = parser.parse_records('HKQuantityTypeIdentifierHeartRate')
    
    print(f"Found {len(hr_records)} heart rate records")
    
    # Write to CSV
    print(f"Writing to {output_file}...")
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Heart Rate (bpm)', 'Source'])
        
        for record in hr_records:
            if record.start_date:
                writer.writerow([
                    record.start_date.isoformat(),
                    record.value,
                    record.source_name
                ])
    
    print(f"✓ Successfully exported {len(hr_records)} records to {output_file}")


if __name__ == '__main__':
    # Update these paths to your actual files
    xml_file = 'path/to/your/export.xml'
    
    # Export step data
    export_steps_to_csv(xml_file, 'daily_steps.csv', days=30)
    
    # Export heart rate data
    export_heart_rate_to_csv(xml_file, 'heart_rate.csv')