class TxtAnalyze:
    def __init__(self, path) -> None:
        self.__path = path
        
    def create_histogram(self):
        with open(self.__path, 'r', encoding='ascii') as f:
            histogram = [0] * 256
            
            for line in f:
                for char in line:
                    value = ord(char)
                    histogram[value] += 1
        
        return histogram
    
    
class BmpAnalyze:
    
    def __init__(self, path) -> None:
        self.__path = path
        
        
    def create_histogram(self):
        with open (self.__path, 'rb') as f:
            f.read(54)
            histogram = [0] * 256
            byte = f.read(1)
            while byte:
                value = int.from_bytes(byte, byteorder='little')
                histogram[value] += 1
                byte = f.read(1) 

        return histogram