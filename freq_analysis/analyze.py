from collections import Counter
from PIL import Image
from math import log2


def compute_entropy(frequency):
    total = sum(frequency.values())
    if total == 0:
        return 0
    entropy = -sum(
        (count / total) * log2(count / total) if count != 0 else 0
        for count in frequency.values()
    )
    return entropy


class TxtAnalyze:
    def analyze_file(self, file_path):
        with open(file_path, "rb") as file:
            content = file.read()
            frequency = Counter(content)
        return {"text": frequency, "text_entropy": compute_entropy(frequency)}


class BmpAnalyze:
    def analyze_file(self, file_path):
        image = Image.open(file_path)
        r, g, b = image.split()
        r_freq = Counter(r.getdata())
        g_freq = Counter(g.getdata())
        b_freq = Counter(b.getdata())
        entropy = {
            "red": compute_entropy(r_freq),
            "green": compute_entropy(g_freq),
            "blue": compute_entropy(b_freq),
        }
        return {"red": r_freq, "green": g_freq, "blue": b_freq, "entropy": entropy}