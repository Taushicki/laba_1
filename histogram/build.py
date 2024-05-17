import matplotlib.pyplot as plt


class BuildHistogram:
    def __init__(self, histogram) -> None:
        self.__build(histogram)
        
        
        
    def __build(self, histogram):
        plt.figure(figsize=(10, 6))
        plt.bar(range(256), histogram, color='skyblue')
        plt.title('Histogram of ASCII Characters')
        plt.xlabel('ASCII Code')
        plt.ylabel('Frequency')
        plt.xlim(0, 255)
        plt.show()        