from os.path import basename, dirname, join, splitext

class Reveal:
    def __init__(self, lines, theme):
        self.html = open(join(dirname(__file__), "..", "template.html"),
                'r').read().replace("---theme---", theme).replace("---section---", str.join(
                    "        ", lines))

    def generate(self, filename, title):
        open(filename, "w").write(self.html.replace("---title---", title))
