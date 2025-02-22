from enum import Enum

class NotificationFrequency(Enum):
    #possible notification frequencies
    DAILY = "daily"
    WEEKLY = "weekly"

class NotificationPreferences:
    #NotificationPreferences stores a user's notification settings
    frequency: NotificationFrequency = NotificationFrequency.DAILY
    is_enabled: bool = True

    def __init__(self, frequency: NotificationFrequency, is_enabled: bool) -> None:
        #initializes notification preferences
        pass
