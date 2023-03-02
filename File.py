class File:
    """ Set mode (w or r)
        Set filename (no extention)
        Give data to be written
        
        Works with data as with string
    """
    def __init__(self, filename:str, mode: str):
        self.filename = filename
        self.mode = mode
        
    def write(self, data: str):
        """Writes given data to file

        Args:
            data (str): text to be written
        """
        if not (self.mode =="w"): raise "Mode error"
        
        with open(f"{self.filename}.txt", self.mode) as file:
            file.write(data)
    
    def read(self):
        """Returns text data from given file

        Returns:
            str: data
        """
        if not (self.mode == "r"): raise "Mode error"
        with open(self.filename, self.mode) as file:
            return file.read()