"""
Configuration constants for the scheduler utility.
"""
import os
SCHEDULE_DATA_FILE = os.path.join(os.path.dirname(__file__), 'checkin_schedule.csv')
LOG_FILE = 'scheduler.log'
