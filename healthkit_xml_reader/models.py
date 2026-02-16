"""
Data models for HealthKit records
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class HealthRecord:
    """
    Represents a single health data record from HealthKit
    
    Attributes:
        record_type: Type of health record (e.g., StepCount, HeartRate)
        source_name: Name of the device/app that recorded the data
        value: The measured value
        unit: Unit of measurement
        start_date: When the measurement started
        end_date: When the measurement ended
        creation_date: When the record was created
    """
    record_type: str
    source_name: str
    value: str
    unit: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    creation_date: Optional[datetime] = None
    
    def __repr__(self) -> str:
        """String representation of the health record"""
        return (f"HealthRecord(type={self.record_type}, "
                f"value={self.value} {self.unit}, "
                f"date={self.start_date})")


@dataclass
class Workout:
    """
    Represents a workout session from HealthKit
    
    Attributes:
        workout_type: Type of workout (e.g., Running, Cycling)
        duration: Duration of the workout
        duration_unit: Unit for duration (usually minutes)
        total_distance: Distance covered during workout
        total_energy_burned: Calories burned
        source_name: Source device/app
        start_date: Workout start time
        end_date: Workout end time
    """
    workout_type: str
    duration: float
    duration_unit: str
    total_distance: Optional[float] = None
    total_energy_burned: Optional[float] = None
    source_name: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    
    def __repr__(self) -> str:
        """String representation of the workout"""
        return (f"Workout(type={self.workout_type}, "
                f"duration={self.duration} {self.duration_unit}, "
                f"date={self.start_date})")


@dataclass
class ActivitySummary:
    """
    Represents daily activity summary from Apple Watch
    
    Attributes:
        date: Date of the activity summary
        active_energy_burned: Active calories burned
        apple_exercise_time: Exercise minutes
        apple_stand_hours: Stand hours achieved
    """
    date: datetime
    active_energy_burned: float
    apple_exercise_time: float
    apple_stand_hours: int
    
    def __repr__(self) -> str:
        """String representation of activity summary"""
        return (f"ActivitySummary(date={self.date}, "
                f"calories={self.active_energy_burned}, "
                f"exercise_min={self.apple_exercise_time}, "
                f"stand_hours={self.apple_stand_hours})")