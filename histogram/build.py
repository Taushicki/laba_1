import matplotlib.pyplot as plt


class BuildHistogram:
    def __init__(self, frequency, title="") -> None:
        self.plot_histogram(frequency, title)

    def plot_histogram(self, frequency, title):
        if "red" in frequency:
            fig, (ax1, ax2, ax3) = plt.subplots(
                1, 3, figsize=(15, 5), sharex=True, sharey=True
            )
            ax1.bar(list(frequency["red"].keys()), list(frequency["red"].values()))
            ax1.set_title("Red Channel")
            ax1.set_yscale("log")

            ax2.bar(list(frequency["green"].keys()), list(frequency["green"].values()))
            ax2.set_title("Green Channel")
            ax2.set_yscale("log")

            ax3.bar(list(frequency["blue"].keys()), list(frequency["blue"].values()))
            ax3.set_title("Blue Channel")
            ax3.set_yscale("log")

            fig.suptitle(title)
            plt.show()

        elif "text" in frequency:
            labels, values = zip(*frequency["text"].most_common())
            plt.bar(labels, values)
            plt.xlabel("ASCII value")
            plt.ylabel("Frequency")
            plt.title(title)
            print(f"Entropy - Text: {frequency['text_entropy']:.4f}")
            plt.show()
        else:
            raise ValueError("Unsupported frequency format")
