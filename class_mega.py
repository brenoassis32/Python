# coding: utf-8
class Mega:
#    def __init__(self, book="http://pppro.cefet-rj.br/~breno/new.xlsx", _sheet=0):
    def __init__(self, book="http://pppro.cefet-rj.br/~breno/mega.xlsx", _sheet=0):
        import xlrd
        import urllib.request
        file_name, headers = urllib.request.urlretrieve(book)
        self.book=xlrd.open_workbook(file_name)
        self._sheet=_sheet
        self._worksheet=self.book.sheet_by_index(self._sheet)
    
    @property
    def sheet(self):
        return self._sheet
    @sheet.setter
    def sheet(self,value):
        import xlrd
        self._sheet=value
        self._worksheet=self.book.sheet_by_index(value)

    @property
    def worksheet(self):
        return self._worksheet
    @worksheet.setter
    def worksheet(self,value):
        import xlrd
        self._worksheet=self.book.sheet_by_index(value)
    
    def first_row(self):
        import xlrd
        first_row=[]
        for col in range(self._worksheet.ncols):
            first_row.append(self._worksheet.cell_value(0,col))
        return first_row
    
    def concurso(self):
        import xlrd
        conc=[]
        for row in range(1,self._worksheet.nrows):
            conc.append(self._worksheet.cell_value(row,0))
        return conc

    def data(self):
        import xlrd
        data=[]
        for row in range(1,self._worksheet.nrows):
            data.append(self._worksheet.cell_value(row,1))
        return data

    def num(self):
        import xlrd
        num=[]
        for row in range(1,self._worksheet.nrows):
            num.append((self._worksheet.cell_value(row,2),self._worksheet.cell_value(row,3),self._worksheet.cell_value(row,4),self._worksheet.cell_value(row,5),self._worksheet.cell_value(row,6),self._worksheet.cell_value(row,7),))
        return num
		
    def num_four(self):
        import xlrd
        num=[]
        for row in range(1,self._worksheet.nrows):
            num.append((self._worksheet.cell_value(row,2),self._worksheet.cell_value(row,3),self._worksheet.cell_value(row,4),self._worksheet.cell_value(row,5)))
        return num

    def num_five(self):
        import xlrd
        num=[]
        for row in range(1,self._worksheet.nrows):
            num.append((self._worksheet.cell_value(row,2),self._worksheet.cell_value(row,3),self._worksheet.cell_value(row,4),self._worksheet.cell_value(row,5),self._worksheet.cell_value(row,6)))
        return num