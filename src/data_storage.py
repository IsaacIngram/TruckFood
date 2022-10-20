
class DataStorage:

    file_path: str

    def __init__(self, file_path:str):
        """
        Create a data storage object for reading and writing data to .txt file
        :param file_path: The path to the .txt file
        """
        self.file_path = file_path

    def write_data(self, data: str) -> None:
        """
        Write data to a datafile
        :param data: The data to write
        :return: None
        """
        with open(self.file_path, 'w') as file:
            file.write(data)

    def read_data(self) -> str:
        """
        Get data from the datafile
        :return: A string containing the content of the file
        """
        with open(self.file_path) as file:
            # Append all lines of the file to the same output string
            output: str = ""
            for line in file:
                output = output + "\n" + line
            return output
