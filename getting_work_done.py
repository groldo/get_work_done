import click
from scrapepdf import ScrapePDF
from parser.chapter_parser import Chapter_Parser
from parser.headings_parser import Headings_Parser


@click.group()
def cli():
    pass

@cli.command()
@click.argument('infile', type=click.File('rb'))
@click.argument('startpage', type=int)
@click.argument('endpage', type=int)
@click.option('--out', type=click.File('w'))
def read_pdf(infile, startpage, endpage, out):
    '''
    python3 getting_work_done.py read-pdf example.pdf 6 50 --out test.txt
    '''
    pdf = ScrapePDF(startpage, endpage, infile)
    text = pdf.getText()
    if out:
        for _,txt in enumerate(text):
            out.write(txt)

@cli.command()
@click.argument('infile', type=click.File('r'))
@click.option('--parser', type=str, default='chapter')
@click.option('--out', type=click.File('w'))
def searchText(infile, parser, out):
    '''
    search text
    ex.:
    python3 getting_work_done.py searchtext text.txt --parser heading --out test.csv
    '''
    text = infile.read()
    if parser == 'chapter':
        parser = Chapter_Parser(text.splitlines())
    elif parser == 'heading':
        parser = Headings_Parser(text.splitlines())

    if out:
        import datetime

        count = 0
        for i, txt in enumerate(parser.findings.items()):
            if i%2 == 0:
                due_date = datetime.datetime.now()+datetime.timedelta(days=count)
                due_date = due_date.strftime('%A')
                count +=1
            if i != 0:
                line_sum = txt[-1].line_no - line_cache
                out.write(f'{line_sum},{due_date}\n')
            out.write(f'{i+1},"{txt[0]}",')
            line_cache = txt[-1].line_no
        out.write(f'{line_sum},{due_date}\n')

if __name__ == '__main__':
    cli()

