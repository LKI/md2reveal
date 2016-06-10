class MD:
    def __init__(self, filename):
        self.lines = open(filename, "r").readlines()

    def dump_sections(self, title):
        # Add section tag
        res = ['<section>\n', '  <h1>{}</h1>\n'.format(title), '</section>\n', '<section data-markdown>\n']
        for l in self.lines:
            if self.head(l) > 0:
                res += ['</section>\n', '<section data-markdown>\n']
            res += [l]
        res += ['</section>\n']

        # Remove empty section
        i = len(res) - 1
        while i >= 0:
            if res[i] == '<section data-markdown>\n' and res[i+1] == '</section>\n':
                res = res[:i] + res[i+2:]
            else:
                i -= 1

        # Indent
        indents, indent, start = [], 0, -1
        for i in range(len(res)):
            head = self.head(res[i])
            if (head == 1 and start > -1) or (head == 2 and indent > 2):
                indents += [[start, i-1]]
            if head >= 0:
                indent = head
            if head == 1:
                start = -1
            elif head == 2 or (head == 3 and start == -1):
                start = i-1

        for i in reversed(indents):
            for j in range(i[0], i[1]):
                res[j] = "  " + res[j]
            res = res[:i[0]] + ["<section>\n"] + res[i[0]:i[1]] + ["</section>\n"] + res[i[1]:]
        return res

    def head(self, line):
        head, idx = 0, 0
        while line.find('#', idx) > -1:
            head, idx = head + 1, line.find('#', idx) + 1
        return head
