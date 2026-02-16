"""
Utility functions for HealthKit data processing
"""

from datetime import datetime, timedelta
from typing import List, Dict, Any
from .models import HealthRecord


def filter_by_date_range(
    records: List[HealthRecord],
    start_date: datetime,
    end_date: datetime
) -> List[HealthRecord]:
    """
    Filter health records by date range
    
    Args:
        records: List of HealthRecord objects
        start_date: Start of date range
        end_date: End of date range
    
    Returns:
        Filtered list of records within the date range
    """
    return [
        record for record in records
        if record.start_date and start_date <= record.start_date <= end_date
    ]


def group_by_date(records: List[HealthRecord]) -> Dict[str, List[HealthRecord]]:
    """
    Group health records by date (ignoring time)
    
    Args:
        records: List of HealthRecord objects
    
    Returns:
        Dictionary with date strings as keys and lists of records as values
    """
    grouped = {}
    
    for record in records:
        if record.start_date:
            date_key = record.start_date.strftime('%Y-%m-%d')
            if date_key not in grouped:
                grouped[date_key] = []
            grouped[date_key].append(record)
    
    return grouped


def calculate_daily_total(records: List[HealthRecord]) -> float:
    """
    Calculate the total value for a list of records
    
    Args:
        records: List of HealthRecord objects
    
    Returns:
        Sum of all record values (converted to float)
    """
    total = 0.0
    
    for record in records:
        try:
            total += float(record.value)
        except (ValueError, TypeError):
            # Skip records that can't be converted to float
            continue
    
    return total


def simplify_record_type(record_type: str) -> str:
    """
    Simplify HealthKit record type names by removing prefix
    
    Example:
        'HKQuantityTypeIdentifierStepCount' -> 'StepCount'
    
    Args:
        record_type: Full HealthKit record type string
    
    Returns:
        Simplified record type name
    """
    prefixes = [
        'HKQuantityTypeIdentifier',
        'HKCategoryTypeIdentifier',
        'HKCharacteristicTypeIdentifier'
    ]
    
    for prefix in prefixes:
        if record_type.startswith(prefix):
            return record_type.replace(prefix, '')
    
    return record_type


def convert_unit(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert between common health metric units
    
    Args:
        value: Numeric value to convert
        from_unit: Source unit
        to_unit: Target unit
    
    Returns:
        Converted value
    
    Note:
        Currently supports basic conversions. Expand as needed.
    """
    # Distance conversions
    if from_unit == 'mi' and to_unit == 'km':
        return value * 1.60934
    elif from_unit == 'km' and to_unit == 'mi':
        return value / 1.60934
    
    # Weight conversions
    elif from_unit == 'lb' and to_unit == 'kg':
        return value * 0.453592
    elif from_unit == 'kg' and to_unit == 'lb':
        return value / 0.453592
    
    # If no conversion needed or not supported
    return value