import re

from .findings import Finding

class Parser():

    def __init__(self, text):
        self.text = text
        self.findings = {}
        self.parse_text(self.match_callback)

    def parse_text(self, func=None):
        for i, line in enumerate(self.text):
            match = re.search(self.regex, line)
            if match:
                if not self.findings.get(line):
                    finding = Finding(line, i)
                    self.findings[line] = finding
                if func:
                    func(match)
