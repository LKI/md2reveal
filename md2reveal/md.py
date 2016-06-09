class MD:
    def __init__(self, filename):
        self.lines = open(filename, "r").readlines()

    def dump_sections(self):
        # Add section tag
        res = ['<section data-markdown>\n']
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
        indent, start = 0, -1
        for i in range(0, len(res)):
            head = self.head(res[i])
            if head == 2 and indent <= 2:
                indent = 2
                start  = i-1
            elif head > 2:
                indent = head
                start  = start or (i-1)
            elif head > 1 and start > -1:
                res = res[:start] + ["<section>\n"] + res[start:i-1] + ["</section>\n"] + res[i-1:]
                for j in range(start, i-1):
                    res[j] = res[j] + "  "
                start = -1
                indent = 0
        return res

    def head(self, line):
        head, idx = 0, 0
        while line.find('#', idx) > -1:
            head, idx = head + 1, line.find('#', idx) + 1
        return head
