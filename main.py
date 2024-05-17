from histogram.build import BuildHistogram
from freq_analysis.analyze import *


if __name__ == '__main__':
    # for i, freq in enumerate(BmpAnalyze('res/bmp_img.bmp').create_histogram()):
    #     print(f"Byte value {i}: {freq} occurrences")
    # for i, freq in enumerate(TxtAnalyze('res/txtfile.txt').create_histogram()):
    #     print(f"Character '{chr(i)}' ({i}): {freq} occurrences")
        
    
    # BuildHistogram(BmpAnalyze('res/bmp_photoshop.bmp').create_histogram())
    # BuildHistogram(BmpAnalyze('res/bmp_template.bmp').create_histogram())
    # BuildHistogram(BmpAnalyze('res/bmp_img.bmp').create_histogram())
    # BuildHistogram(BmpAnalyze('res/bmp_black.bmp').create_histogram())
    
    # BuildHistogram(TxtAnalyze('res/txtfile.txt').create_histogram())
    BuildHistogram(TxtAnalyze('res/literatura.txt').create_histogram())
    # BuildHistogram(TxtAnalyze('res/scientific.txt').create_histogram())
    # BuildHistogram(TxtAnalyze('res/gpt.txt').create_histogram())
