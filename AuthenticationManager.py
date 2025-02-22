from UserProfile import UserProfile
class AuthenticationManager:
    # AuthenticationManager handles user authentication, validation, and registration logic
    def validate_username(self, username: str) -> bool:
        #validates username format
        pass

    def validate_password(self, password: str) -> bool:
        #validates password strength and length
        pass

    def validate_email(self, email: str) -> bool:
        #validates email format
        pass

    def hash_password(self, password: str) -> str:
        #hashes password for secure storage
        pass

    def save_new_user(self, user_profile: UserProfile, hashed_password: str) -> str:
        #saves new user via userstoragemanager
        pass