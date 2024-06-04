from freq_analysis.analyze import BmpAnalyze, TxtAnalyze
from histogram.build import BuildHistogram


if __name__ == '__main__':
    BuildHistogram(BmpAnalyze().analyze_file('res/bmp_photoshop.bmp'))
    BuildHistogram(BmpAnalyze().analyze_file('res/bmp_template.bmp'))
    BuildHistogram(BmpAnalyze().analyze_file('res/bmp_img.bmp'))
    BuildHistogram(BmpAnalyze().analyze_file('res/bmp_adobe.bmp'))

    BuildHistogram(TxtAnalyze().analyze_file('res/txtfile.txt'))
    BuildHistogram(TxtAnalyze().analyze_file('res/literatura.txt'))
    BuildHistogram(TxtAnalyze().analyze_file('res/scientific.txt'))
    BuildHistogram(TxtAnalyze().analyze_file('res/dialog.txt'))
