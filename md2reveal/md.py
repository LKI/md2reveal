class MD:
    qr = []

    def __init__(self, filename):
        self.lines = open(filename, "r").readlines()

    def set_qr_url(self, url):
        if 'http' == url[:4]:
            url = '"' + url + '"'
        self.qr = [
            '<section>\n',
            '  <h1>Thank you</h1>\n',
            '  <p>You can find this slide at <div id="qr-url">-</div> or scan this QR code</p>\n',
            '  <canvas id="qr-code"></canvas>\n',
            '  <script src="http://liriansu.com/static/js/qr.min.js"></script>\n',
            '  <script>\n',
            '    qr.canvas({\n',
            '      canvas: document.getElementById("qr-code"),\n',
            '      level : "H",\n',
            '      size  : 8,\n',
            '      value : %s\n' % url,
            '    });\n',
            '    document.getElementById("qr-url").innerHTML = %s;\n' % url,
            '  </script>\n',
            '</section>\n',
        ]

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
        if start > 0:
            indents += [[start, len(res)]]

        for i in reversed(indents):
            for j in range(i[0], i[1]):
                res[j] = "  " + res[j]
            res = res[:i[0]] + ["<section>\n"] + res[i[0]:i[1]] + ["</section>\n"] + res[i[1]:]

        # Add qr code section
        res += self.qr

        return res

    def head(self, line):
        head, idx = 0, 0
        while line.find('#', idx) > -1:
            head, idx = head + 1, line.find('#', idx) + 1
        return head
