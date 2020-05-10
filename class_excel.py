# coding: utf-8
class Excel:
#    def __init__(self, book="http://pppro.cefet-rj.br/~breno/new.xlsx", _sheet=0):
    def __init__(self, book="/Users/Breno/Desktop/mega4.xlsx", _sheet=0):
        import xlrd
        #import urllib.request
        #file_name, headers = urllib.request.urlretrieve(book)
        file_name = book
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
            conc.append(self._worksheet.cell_value(row,1))
        return conc

    def data(self):
        import xlrd
        data=[]
        for row in range(1,self._worksheet.nrows):
            data.append(self._worksheet.cell_value(row,2))
        return data

    def data_num(self):
        import xlrd
        data=[]
        for row in range(1,self._worksheet.nrows):
            data.append(self._worksheet.cell_value(row,10))
        return data
		
    def num(self):
        import xlrd
        num=[]
        for row in range(1,self._worksheet.nrows):
            num.append((self._worksheet.cell_value(row,3),self._worksheet.cell_value(row,4),self._worksheet.cell_value(row,5),self._worksheet.cell_value(row,6),self._worksheet.cell_value(row,7),self._worksheet.cell_value(row,8),))
        return num

    def seed(self):
        import xlrd
        sem=[]
        for row in range(1,self._worksheet.nrows):
            sem.append(self._worksheet.cell_value(row,9))
        return sem

    def d1(self):
        import xlrd
        data=[]
        for row in range(1,self._worksheet.nrows):
            data.append(self._worksheet.cell_value(row,2))
        return data

    def sorteado(self,a):
        #import itertools
        num=self.num()
        for j in range(len(num)):
            l=sorted(list(num[j]))
            #print(l)
            if tuple(l)==a:
               return True
        return False


    def num_quad(self,a):
        #import itertools
        cont=0
        num=self.num()
        if self.sorteado(a) == True:
           return cont
        a=sorted(list(a))
        for j in range(1998,len(num)):
            l=sorted(list(num[j]))
            if (l[0],l[1],l[2],l[3])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[1],l[2],l[4])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[1],l[2],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[1],l[3],l[4])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[1],l[3],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[2],l[3],l[4])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[2],l[3],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[0],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[3],l[4],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[2],l[3],l[4],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[1],l[2],l[3],l[4])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[1],l[2],l[3],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
#			   
            if (l[1],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[1],a[2],a[4]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[1],a[2],a[5]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[1],a[3],a[4]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[1],a[3],a[5]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[0],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[3],l[4],l[5])==(a[2],a[3],a[4],a[5]):
               cont+=1
            #print((j+1)/(len(num)+1))
#			print((j+1)/(len(num)+1))   
        return cont


    def num_quin(self,a):
        #import itertools
        cont=0
        num=self.num()
        if self.sorteado(a) == True:
           return cont
        a=sorted(list(a))
        for j in range(1998,len(num)):
            l=sorted(list(num[j]))
            if (l[0],l[1],l[2],l[3],l[4])==(a[0],a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[4])==(a[0],a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[4])==(a[0],a[1],a[2],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[4])==(a[0],a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[4])==(a[0],a[2],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[4])==(a[1],a[2],a[3],a[4],a[5]):
               cont+=1
##
            if (l[0],l[1],l[2],l[3],l[5])==(a[0],a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[5])==(a[0],a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[5])==(a[0],a[1],a[2],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[5])==(a[0],a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[5])==(a[0],a[2],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[3],l[5])==(a[1],a[2],a[3],a[4],a[5]):
               cont+=1
##
            if (l[0],l[1],l[2],l[4],l[5])==(a[0],a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[2],l[4],l[5])==(a[0],a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4],l[5])==(a[0],a[1],a[2],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4],l[5])==(a[0],a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4],l[5])==(a[0],a[2],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[2],l[4],l[5])==(a[1],a[2],a[3],a[4],a[5]):
               cont+=1
##
            if (l[0],l[1],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[1],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4],l[5])==(a[0],a[1],a[2],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4],l[5])==(a[0],a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4],l[5])==(a[0],a[2],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[1],l[3],l[4],l[5])==(a[1],a[2],a[3],a[4],a[5]):
               cont+=1
##
            if (l[0],l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[0],l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4],l[5])==(a[0],a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4],l[5])==(a[0],a[2],a[3],a[4],a[5]):
               cont+=1
            if (l[0],l[2],l[3],l[4],l[5])==(a[1],a[2],a[3],a[4],a[5]):
               cont+=1
##
            if (l[1],l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3],a[4]):
               cont+=1
            if (l[1],l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[3],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4],l[5])==(a[0],a[1],a[2],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4],l[5])==(a[0],a[1],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4],l[5])==(a[0],a[2],a[3],a[4],a[5]):
               cont+=1
            if (l[1],l[2],l[3],l[4],l[5])==(a[1],a[2],a[3],a[4],a[5]):
               cont+=1
            #print((j+1)/(len(num)+1))
##
        return cont


    def saidas(self):
        #import itertools
        num=self.num()
        s=[]
        for i in range(0,60):
#            s.append(0)
            cont=0
            #print(s)
            for j in range(len(num)):#range(len(num)):
                l=sorted(list(num[j]))
                #print(j)
                for t in range(len(l)):
                    #print(l[t])
                    #print(i+1)
                    if l[t]==(i+1):
                       cont+=1
                       #print(cont)
                       #break
            s.append(cont)
        return s

    def comb(self):
        num=self.num()
        s=[]
        for i in range(0,60):
            #s[i]=[]
            for n in range(i,60):
                if i!=n:
                    cont=0
                    for j in range(len(num)):#range(len(num)):
                        l=sorted(list(num[j]))
                        for t in range(len(l)):
                            if l[t]==(i+1):
                                for a in range(len(l)):
                                    if l[a]==(n+1):
                                       cont+=1
                    s.append(cont)
        return s

