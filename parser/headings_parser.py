from . import parser

class Headings_Parser(parser.Parser):

    def __init__(self, text):
        self.regex = r"^(?P<section>\d+)\.(?P<subsection>\d+)"
        super().__init__(text)

    def parse_text(self, func=None):
        return super().parse_text(func=func)
    
    def match_callback(self, match):
        if match.group('section'):
            self.regex = self.regex + f"|^{match.group('section')}\.([0-9])\ [A-Z][a-z]*.(\ |$)"
    
    def remove_duplicates(self):
        return super().remove_duplicates()