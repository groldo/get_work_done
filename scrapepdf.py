from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

class ScrapePDF():


    def __init__(self, startpage, endpage, file):
        self.startpage = startpage
        self.endpage = endpage
        self.file = file
    
    def getText(self):
        pages = range(self.startpage, self.endpage)
        self.content = []

        for i in pages:

            self.content.append(extract_text(self.file, page_numbers=[i]))
            print("page {} done".format(i))

        return self.content
    
    def getTextElements(self):
        pages = range(self.startpage, self.endpage)
        for i in pages:
            for page_layout in extract_pages(self.file, page_numbers=[i]):
                for element in page_layout:
                    if isinstance(element, LTTextContainer):
                        print(element.get_text())
    