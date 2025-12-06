class TableFormatter():
    def headings(self, headers):
        raise NotImplementedError
    
    def row(self, rowdata):
        raise NotImplementedError
    
class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print(f'<tr>', end='')
        
        for h in headers:            
            print(f'<th>{h}<th>', end='')
        
        print(f'<tr>')

    def row(self, rowdata):
        print(f'<tr>', end='')
        
        for r in rowdata:            
            print(f'<th>{r}<th>', end='')
        
        print(f'<tr>')

def create_formatter(fmt):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise RuntimeError(f'Unknown format {fmt}')
    
    return formatter