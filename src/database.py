from pymongo import MongoClient
from pymongo import database


class Database:

    _client: MongoClient
    _database: database.Database

    def connect(self, host: str, user: str, password: str, port: str, database_name: str) -> None:
        """
        Connect to a database using the provided credentials
        :param database_name: The name of the database to connect to
        :param host: The host of the database
        :param user: The user to use
        :param password: The password for the user
        :param port: The port to connect through
        :return: None
        """
        # Connect to the client
        self._client = MongoClient("mongodb://" + user + ":" + password + "@" + host + ":" + port)
        # Get the database
        self._database = self._client[database_name]

    def disconnect(self):
        """
        Disconnect from the MongoDB
        :return:
        """
        self._client.close()

    def set_description(self) -> None:
        """
        Set the description
        :return: None
        """
        return None
        # TODO implement set_description

    def get_description(self) -> int:
        """
        Get the description
        :return: An integer
        """
        pass
        # TODO implement get_description

    def set_start_date(self, date: str) -> None:
        """
        Set the start date
        :param date:
        :return: None
        """
        pass
        # TODO implement set_start_date

    def set_end_date(self, date: str) -> None:
        """
        Set the end date
        :param date:
        :return: None
        """
        pass
        # TODO implement set_end_date

    def get_start_date(self) -> str:
        """
        Get the start date
        :return: A string
        """
        pass
        # TODO implement get_start_date

    def get_end_date(self) -> str:
        """
        Get the end date
        :return: A string
        """
        pass
        # TODO implement get_end_date

    def set_timestamp(self, timestamp: str) -> None:
        """
        Set the timestamp
        :param timestamp: A string
        :return: None
        """
        pass
        # TODO implement set_timestamp

    def get_timestamp(self) -> str:
        """
        Get the timestamp
        :return: A string
        """
        pass
        # TODO implement get_timestamp
