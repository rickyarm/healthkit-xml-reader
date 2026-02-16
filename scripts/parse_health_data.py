#!/usr/bin/env python3
"""
Command-line script to parse Apple Health data

Usage:
    python scripts/parse_health_data.py path/to/export.xml [options]
    
Options:
    --type TYPE      Filter by record type (e.g., StepCount, HeartRate)
    --days N         Show data from last N days
    --output FILE    Export to CSV file
"""

import sys
import argparse
from datetime import datetime, timedelta
from pathlib import Path

# Add parent directory to path so we can import the package
sys.path.insert(0, str(Path(__file__).parent.parent))

from healthkit_xml_reader import HealthKitParser
from healthkit_xml_reader.utils import simplify_record_type, filter_by_date_range


def main():
    """Main entry point for the script"""
    parser = argparse.ArgumentParser(
        description='Parse and analyze Apple Health export data'
    )
    parser.add_argument(
        'xml_file',
        help='Path to Apple Health export.xml file'
    )
    parser.add_argument(
        '--type',
        dest='record_type',
        help='Filter by record type (e.g., StepCount, HeartRate)'
    )
    parser.add_argument(
        '--days',
        type=int,
        default=7,
        help='Number of days to show (default: 7)'
    )
    parser.add_argument(
        '--list-types',
        action='store_true',
        help='List all available record types and exit'
    )
    
    args = parser.parse_args()
    
    # Initialize parser
    print(f"Loading data from {args.xml_file}...")
    health_parser = HealthKitParser(args.xml_file)
    
    # List types if requested
    if args.list_types:
        print("\nAvailable record types:")
        record_types = health_parser.get_record_types()
        for rt in record_types:
            simplified = simplify_record_type(rt)
            print(f"  {simplified}")
        print(f"\nTotal: {len(record_types)} types")
        return
    
    # Parse records
    if args.record_type:
        # Add HK prefix if not present
        full_type = args.record_type
        if not full_type.startswith('HK'):
            full_type = f'HKQuantityTypeIdentifier{args.record_type}'
        
        print(f"\nParsing {args.record_type} records...")
        records = health_parser.parse_records(full_type)
    else:
        print("\nParsing all records...")
        records = health_parser.parse_records()
    
    # Filter by date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=args.days)
    filtered_records = filter_by_date_range(records, start_date, end_date)
    
    print(f"Found {len(filtered_records)} records in last {args.days} days")
    
    # Display sample records
    print(f"\nShowing first 10 records:")
    for record in filtered_records[:10]:
        record_type = simplify_record_type(record.record_type)
        print(f"  [{record.start_date}] {record_type}: {record.value} {record.unit}")
    
    if len(filtered_records) > 10:
        print(f"  ... and {len(filtered_records) - 10} more")


if __name__ == '__main__':
    main()
```

---

### File 11: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Testing
.pytest_cache/
.coverage
htmlcov/

# macOS
.DS_Store

# Health data (keep your personal data private!)
export.xml
export.zip
apple_health_export/
*.csv

# Output files
output/
results/