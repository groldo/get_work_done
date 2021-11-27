from dataclasses import dataclass
@dataclass
class Finding():

    line: str
    line_no: int

    def __iter__(self):
        return self.line,self.line_no
