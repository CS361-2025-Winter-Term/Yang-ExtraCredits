from UserProfile import UserProfile
class UserStorageManager:
    # UserStorageManager manages storage and retrieval of user data from the database
    def find_user_by_username(self, username: str) -> UserProfile:
        #finds and returns user profile by username, returns None if not found
        pass

    def save_user_to_database(self, user_profile: UserProfile, hashed_password: str) -> bool:
        #saves new user profile and hashed password to database
        #returns True if save is successful, False otherwise
        pass
