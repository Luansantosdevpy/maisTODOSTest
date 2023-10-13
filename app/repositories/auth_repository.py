from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create_user(self, data):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass
