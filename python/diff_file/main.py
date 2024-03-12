import sys
import os.path
import pandas as pd
from openpyxl import Workbook
from datetime import datetime
import time

def _print(str, newLine = False):
    print(str, sep = '', end = ',', file = sys.stdout, flush = True)

now = datetime.now()
item1Qty = "0"
item2Qty = "0"

if len(sys.argv) < 3:
    print('ex) main.exe 전일재고파일명.xls 금일재고파일명.xls')
else:    
    if os.path.isfile('./' + str(sys.argv[1])):

        if os.path.isfile('./' + str(sys.argv[2])):                        

            workbook = Workbook()
            sheet = workbook.active
            sheet['A1'] = "상품코드"
            sheet['B1'] = "사진코드"
            sheet['C1'] = "사방넷코드(6)"
            sheet['D1'] = "사방넷코드(10)"
            sheet['E1'] = "구분"
            sheet['F1'] = "브랜드(영문)"
            sheet['G1'] = "브랜드(한글)"
            sheet['H1'] = "카테고리(영문)"
            sheet['I1'] = "카테고리(한글)"
            sheet['J1'] = "시즌"
            sheet['K1'] = "사이즈"
            sheet['L1'] = "상품명"
            sheet['M1'] = "차수제거"
            sheet['N1'] = "원가"
            sheet['O1'] = "전일재고"
            sheet['P1'] = "전일금액"
            sheet['Q1'] = "당일재고"
            sheet['R1'] = "당일금액"                        
            sheet['S1'] = "Result"   
            df1 = pd.read_excel('./' + str(sys.argv[1]), sheet_name = 0)
            df2 = pd.read_excel('./' + str(sys.argv[2]), sheet_name = 0)
            index = 1

            print('Flag\t\t\tLine\t\tCode\t\tQty\t\tCurrent')
            print('------------------------------------------------------------------------------')
     
            for item2 in df2.values.tolist():                    
                index = index + 1                
                isMatch = 0
                item1Qty = 0
                item2Qty = item2[16]               

                for item1 in df1.values.tolist():                                    
                    item1Qty = item1[16]                                        

                    if str(item1[0]) == str(item2[0]):
                        isMatch = 1
                        if item1[16] != item2[16]:                                                        
                            item2Result = item2 + [str(item1[16])]                            
                            sheet.append(item2Result)                            
                            print('Inconsistency\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(item1Qty) + '\t\t' + str(item2Qty))
                        elif item1[16] != item2[16]:
                            print('')

                if isMatch < 1:                    
                    sheet.append(item2 + ['NEW'])
                    print('New Item\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(item1Qty) + '\t\t' + str(item2Qty))
                else:
                    isMatch = 0

            workbook.save("result-" + str(now.timestamp()) + ".xlsx")

        else:
            print('금일재고파일(' + str(sys.argv[2]) + ')을 찾을 수 없습니다.')      
            
    else:
        print('전일재고파일(' + str(sys.argv[1]) + ')을 찾을 수 없습니다.')                

print('------------------------------------------------------------------------------')        
# end        
        
