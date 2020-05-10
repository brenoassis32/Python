# coding: utf-8

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

class Taco:
    def __init__(self, book="http://www.nepa.unicamp.br/taco/contar/download.php?arquivo=Taco_4a_edicao_2011.xls", _sheet=0):
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
            first_row.append(self._worksheet.cell_value(0,col)+self._worksheet.cell_value(1,col)+" "+self._worksheet.cell_value(2,col))
        return first_row
    
    def food_num (self):
        import xlrd
        d=dict()
        for row in range(3,self._worksheet.nrows):
            t_row=[]
            for col in range(self._worksheet.ncols):
                t_row.append((self._worksheet.cell_value(row,col)))
            num = t_row[0]
#            print(num)
            t_row.remove(t_row[0])
#            print(t_row)
            value = " / ".join((str(e) if isinstance(e,float) else (e)) for e in t_row)
            d[num]=value
        return d
    
    def food_list(self):
        new=[]
        d=self.food_num()
        for key in d:
            if isinstance(key, float):
               new.append(d[key].split(' / ')[0])
        return new

    def food_type(self):
        import xlrd
        import operator
        l=[]
        c=0
        d=dict()
        for row in range(self._worksheet.nrows):
            t_row=[]
            for col in range(self._worksheet.ncols):
                t_row.append(self._worksheet.cell_value(row,col))
            num = t_row[0]
            t_row.remove(t_row[0])
            if isinstance(num,float):
               d[row]=num
            if (self._worksheet.cell_value(row,0)!="") and (self._worksheet.cell_value(row,2)=="") and (self._worksheet.cell_value(row,3)=="") and c<15:
               l.append(self._worksheet.cell_value(row,0))
               c+=1

        return l
    
    def food_num_type(self):
        import xlrd
        import operator
        l=[]
        l = [[] for i in self.food_type()]
        c=0
        d=dict()
        for row in range(self._worksheet.nrows):
            t_row=[]
            for col in range(self._worksheet.ncols):
                t_row.append(self._worksheet.cell_value(row,col))
            num = t_row[0]
            t_row.remove(t_row[0])
            if isinstance(num,float):
               d[row]=num
            if (self._worksheet.cell_value(row,0)!="") and (self._worksheet.cell_value(row,2)=="") and (self._worksheet.cell_value(row,3)=="") and (c<len(self.food_type())) and (row>5):
               l[c].append(max(d.items(), key=operator.itemgetter(1))[1])
               c+=1
        flat_list=[]
        for sublist in l:
            for item in sublist:
                flat_list.append(item)
        return flat_list
     
    def literal_food(self):
#        reload(sys)
#        sys.setdefaultencoding('utf-8')
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
#        l = [[] for i in range(len(self.food_num_type()))]        
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[0]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[0]
                         l[i].append(new)
        return l

    def literal_energy(self):
#        reload(sys)
#        sys.setdefaultencoding('utf-8')
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
#        l = [[] for i in range(len(self.food_num_type()))]        
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[2]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[2]
                         l[i].append(new)
        return l

    def literal_protein(self):
#        reload(sys)
#        sys.setdefaultencoding('utf-8')
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
#        l = [[] for i in range(len(self.food_num_type()))]        
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[4]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[4]
                         l[i].append(new)
        return l
   
    def literal_fat(self):
#        reload(sys)
#        sys.setdefaultencoding('utf-8')
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
#        l = [[] for i in range(len(self.food_num_type()))]        
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[5]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[5]
                         l[i].append(new)
        return l

    def literal_carbo(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[7]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[7]
                         l[i].append(new)
        return l

    def literal_fib(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[8]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[8]
                         l[i].append(new)
        return l

    def literal_Ca(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[10]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[10]
                         l[i].append(new)
        return l

    def literal_K(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[17]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[17]
                         l[i].append(new)
        return l


    def literal_Z(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[19]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[19]
                         l[i].append(new)
        return l

    def literal_Fe(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[15]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[15]
                         l[i].append(new)
        return l

    def literal_Mg(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[11]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[11]
                         l[i].append(new)
        return l

    def literal_Na(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[16]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[16]
                         l[i].append(new)
        return l

    def literal_Mn(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[13]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[13]
                         l[i].append(new)
        return l

    def literal_Cu(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[18]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[18]
                         l[i].append(new)
        return l

    def literal_P(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[14]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[14]
                         l[i].append(new)
        return l

    def literal_VitC(self):
        import xlrd
        list1=self.food_num_type()
        d=self.food_num()
        l = [[] for i in self.food_num_type()]        
        for i in range(len(list1)):
            for num in d:
                if isinstance(num,float):
                   if i==0:
                      if num <= list1[i]:
                         new=d[num].split(' / ')[27]
                         l[i].append(new)
                   else:
                      if num <= list1[i] and num > list1[i-1]:
                         new=d[num].split(' / ')[27]
                         l[i].append(new)
        return l

