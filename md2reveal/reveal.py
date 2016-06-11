from os.path import basename, dirname, join, splitext

class Reveal:
    def __init__(self, lines, theme):
        lines = map(lambda l: "        " + l if l.strip() else "\n", lines)
        section = "\n" + str.join('', lines)
        self.html = open(join(dirname(__file__), "template.html"),
                'r').read().replace("---theme---", theme).replace("---section---", section)

    def generate(self, filename, title):
        open(filename, "w").write(self.html.replace("---title---", title))
