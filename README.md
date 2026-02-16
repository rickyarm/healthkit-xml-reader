# HealthKit XML Reader

A Python package to parse and analyze Apple HealthKit export.xml files.

## Features

- Parse health records (steps, heart rate, workouts, etc.)
- Filter by date range and record type
- Export data to CSV
- Simple and intuitive API
- Type hints for better IDE support

## Installation
```bash
# Clone the repository
git clone https://github.com/rickyarm/healthkit-xml-reader.git
cd healthkit-xml-reader

# Install in development mode
pip install -e .
```

## Quick Start

### Export Your Apple Health Data

1. Open the Health app on your iPhone
2. Tap your profile picture (top right)
3. Scroll down and tap "Export All Health Data"
4. Share the export.zip file to your computer
5. Unzip to get the `export.xml` file

### Basic Usage
```python
from healthkit_xml_reader import HealthKitParser

# Load your health data
parser = HealthKitParser('path/to/export.xml')

# Get all step count records
steps = parser.parse_records('HKQuantityTypeIdentifierStepCount')

# Display first few records
for record in steps[:5]:
    print(f"{record.start_date}: {record.value} steps")

# Parse workouts
workouts = parser.parse_workouts()
for workout in workouts[:5]:
    print(f"{workout.workout_type}: {workout.duration} minutes")
```

### Command Line Usage
```bash
# List all available record types
python scripts/parse_health_data.py export.xml --list-types

# Show step data from last 30 days
python scripts/parse_health_data.py export.xml --type StepCount --days 30

# Show heart rate data
python scripts/parse_health_data.py export.xml --type HeartRate --days 7
```

## Examples

See the `examples/` directory for more detailed usage examples:

- `basic_parse.py` - Simple parsing example
- `export_to_csv.py` - Export data to CSV format

## Project Structure
```
healthkit-xml-reader/
├── healthkit_xml_reader/   # Main package
│   ├── parser.py          # XML parsing logic
│   ├── models.py          # Data models
│   └── utils.py           # Utility functions
├── tests/                 # Unit tests
├── examples/              # Usage examples
├── scripts/               # Command-line scripts
└── docs/                  # Documentation
```

## Development
```bash
# Run tests
python -m unittest discover tests

# Install development dependencies
pip install -r requirements.txt
```

## Integration with macOS Shortcuts

This tool can be integrated with macOS Shortcuts app for automated health data analysis. See documentation for details.

## License

MIT License - see LICENSE file for details

## Author

rickyarm

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.
```

---

### File 13: `requirements.txt`
```
# No external dependencies required!
# The package uses only Python standard library modules:
# - xml.etree.ElementTree (XML parsing)
# - dataclasses (data models)
# - datetime (date/time handling)
# - typing (type hints)

# Development dependencies (optional):
# pytest>=7.0.0
# black>=22.0.0
# mypy>=0.950