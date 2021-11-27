from . import parser

class Chapter_Parser(parser.Parser):

    def __init__(self, text):
        self.regex = r"^Kapitel\ (?P<kapitel>\d+)"
        super().__init__(text)

    def parse_text(self, func=None):
        return super().parse_text(func=func)
    
    def match_callback(self, match):
        if match.group('kapitel'):
            self.regex = self.regex + f"|^{match.group('kapitel')}\.([0-9])\ [A-Z][a-z]*.(\ |$)"
    
    def remove_duplicates(self):
        return super().remove_duplicates()
    