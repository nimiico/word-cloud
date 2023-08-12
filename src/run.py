import matplotlib.pyplot as plt
from wordcloud import WordCloud


class WordCloudGenerator:
    def __init__(self, file_path):
        with open(file_path) as f:
            self.text = f.read()

    def run(self, output_path, **kwargs):
      wordcloud = WordCloud(
        **kwargs,
      ).generate(self.text)


      wordcloud.to_file(output_path)

if __name__ == '__main__':
    wc_gen = WordCloudGenerator('data/movies.txt')
    wc_gen.run(
        'output.png',
        width=600, height=400,
        background_color='white',
        )
