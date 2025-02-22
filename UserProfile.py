from NotificationPreferences import NotificationPreferences
class UserProfile:
    # UserProfile represents a user's profile information
    username: str = ""
    email: str = ""
    notification_preferences: NotificationPreferences = None

    #methods
    def __init__(self, username: str, email: str, notification_preferences: NotificationPreferences) -> None:
        #initializes user profile with given username, email, and notification preferences
        pass
