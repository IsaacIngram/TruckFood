
class DataStorage:

    file_path: str

    def __init__(self, file_path:str):
        """
        Create a data storage object for reading and writing data to .txt file
        :param file_path: The path to the .txt file
        """
        self.file_path = file_path

    def write_data(self, data: str, times_this_week: int) -> None:
        """
        Write data to a datafile
        :param data: The data to write
        :param times_this_week
        :return: None
        """
        with open(self.file_path, 'w') as file:
            file.write(str(data.__hash__()) + "\n" + str(times_this_week))

    def read_data(self) -> (str, int):
        """
        Get data from the datafile
        :return: A string containing the first line of the file and an integer containing the second line
        """
        with open(self.file_path) as file:
            # Append all lines of the file to the same output string
            output: str = ""
            return file.readline(0), int(file.readline(1))

    def compare_data(self, current_data: str):
        """
        Compare a given string with the stored string
        :param current_data: The string to compare
        :return: Whether the strings are equal
        """
        return self.read_data()[0] == str(current_data.__hash__())
