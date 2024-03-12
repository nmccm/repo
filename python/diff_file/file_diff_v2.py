# Author : nmccm (nmccm@naver.com)
# Date : 2024-02-01
# 
# 두개의 엑셀파일을 비교하여 이격 데이터만 별도 파일로 저장하는 프로그램 (비교컬럼 : A=상품코드, C=사방넷코드(6), Q=당일재고)
#
# 조건 1 : 두개의 파일 중 첫번째 파일 기준으로 당일 재고가 변경된 데이터를 찾아 파일에 저장
# 조건 2 : 두개의 파일 중 첫번째 파일 기준으로 신규 데이터를 찾아 파일에 저장
# 조건 3 : 두개의 파일 중 첫번째 파일 기준으로 사방넷 코드가 변경된 데이터를 찾아 파일에 저장

import sys
import os.path
import pandas as pd
from openpyxl import Workbook
from datetime import datetime

def _print(str, newLine = False):
    print(str, sep = '', end = ',', file = sys.stdout, flush = True)

def printLine():
    print('-----------------------------------------------------------------------------------------------------------------')

def printLogTitle():
    print('Flag\t\t\tLine\t\tCode\t\tQty\t\tCurrent\t\tSBN\t\tCurrent')

def printResultTitle():
    print('Flag\t\t\tTotal Count')

def printResult(flag1 = 0, flag2 = 0, flag3 = 0):
    print('Inconsistency\t\t' + str(flag1))
    print('Sabangnet\t\t' + str(flag2))
    print('New Item\t\t' + str(flag3))

_def = ""
now = datetime.now()

if len(sys.argv) < 3:
    print('ERROR : 올바른 형식으로 다시 시도해주세요.')
    print('ex> file_diff.exe 전일재고파일명.xls 금일재고파일명.xls')
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
            df1List = df1.values.tolist()
            df2List = df2.values.tolist()
            index = 0
            resultInconsistencyCount = 0
            resultSabangnetCount = 0
            resultNewItemCount = 0

            print(_def)
            printLogTitle()
            printLine()
    
            for item2 in df2List :
                index = index + 1                               
                isMatch = 0
                item1Qty = 0
                item2Qty = item2[16]               

                for item1 in df1List:
                    item1Qty = item1[16]                                        

                    if str(item1[0]) == str(item2[0]):
                        isMatch = 1
                        if item1[16] != item2[16]:
                            item2Result = item2 + [str(item1[16])]                            
                            resultInconsistencyCount = resultInconsistencyCount + 1
                            sheet.append(item2Result)                            
                            print('Inconsistency\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(item1Qty) + '\t\t' + str(item2Qty))
                        elif item1[16] == item2[16] and len(str(item2[2])) > 6 and item1[2] != item2[2]:
                            item2Result = item2 + ['SBN']
                            resultSabangnetCount = resultSabangnetCount + 1
                            sheet.append(item2Result)                                         
                            print('Sabangnet\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(item1Qty) + '\t\t' + str(item2Qty) + '\t\t' + str(item1[2]) + '\t\t' + str(item2[2]))

                if isMatch < 1:                  
                    resultNewItemCount = resultNewItemCount + 1  
                    sheet.append(item2 + ['NEW'])
                    print('New Item\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(item1Qty) + '\t\t' + str(item2Qty))
                else:
                    isMatch = 0

            workbook.save("result-" + str(now.timestamp()) + ".xlsx")            
            print(_def)
            print(_def)
            printResultTitle()
            printLine()
            printResult(resultInconsistencyCount, resultSabangnetCount, resultNewItemCount)
            print(_def)

        else:
            print('ERROR : 금일재고파일(' + str(sys.argv[2]) + ')을 찾을 수 없습니다.')      
            
    else:
        print('ERROR : 전일재고파일(' + str(sys.argv[1]) + ')을 찾을 수 없습니다.')                
    
# end        
        
