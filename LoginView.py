from UserProfile import UserProfile
from NotificationPreferences import NotificationPreferences, NotificationFrequency
class LoginView:
    # LoginView handles user interactions for logging in and registering
    username_text: str = ""
    password_text: str = ""
    email_text: str = ""
    frequency: NotificationFrequency = NotificationFrequency.DAILY
    is_enabled: bool = True 

    #methods
    def read_username_textbox(self) -> str:
        #reads username from textbox
        pass

    def read_password_textbox(self) -> str:
        #reads password from textbox
        pass

    def read_email_textbox(self) -> str:
        #reads email from textbox
        pass

    def read_notification_preferences(self) -> None:
        #reads notification preferences from UI and returns them
        pass

    def create_notification_preferences(self) -> NotificationPreferences:
        #creates NotificationPreferences object from stored frequency and status
        pass

    def register_user(self, user_profile: UserProfile, password: str) -> None:
        #registers user using authenticationmanager
        pass

    def display_error(self, message: str) -> None:
        #displays error message to user
        pass

    def transition_to_home_view(self, user_profile: UserProfile) -> None:
        #transitions UI to home view after completing registration
        pass