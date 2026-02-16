"""
HealthKit XML Reader
A Python package to parse and analyze Apple HealthKit export.xml files
"""

__version__ = "0.1.0"
__author__ = "rickyarm"

from .parser import HealthKitParser
from .models import HealthRecord, Workout, ActivitySummary

__all__ = [
    "HealthKitParser",
    "HealthRecord", 
    "Workout",
    "ActivitySummary"
]