class MD:
    indent_level = 0
    sections = []

    def __init__(self, filename):
        self.lines = open(filename, "r").readlines()

    def dump_reveal(self):
        self.new_section()
        for l in self.lines:
            head = self.head(l)
            if head != 0:
                self.save_section()
                self.new_section()
            self.add_line(l)
        return self.sections

    def head(self, line):
        head, idx = 0, 0
        while line.find('#', idx) > -1:
            head, idx = head + 1, line.find('#', idx) + 1
        return head

    def new_section(self):
        self.section    = "  " * self.indent_level + "<section"
        self.tag_closed = False
        self.sec_closed = False

    def add_line(self, line):
        if not self.tag_closed:
            self.section += " data-markdown>\n"
            self.tag_closed = True
        self.section += line

    def save_section(self, level=1):
        self.add_line("")
        while level > 0:
            self.section += "</section>\n"
            level -= 1
        self.sec_closed = True
        if self.section != "<section data-markdown>\n</section>\n":
            self.sections += [self.section]

if __name__ == "__main__":
    for i in MD('hello.md').dump_reveal():
        print i,
