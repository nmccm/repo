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
from file_diff_def import *
import numpy as np

_def = get_def()
_dot = get_dot()
_slash = get_slash()
_new = get_new()
_sbn = get_sbn()

now = datetime.now()

if len(sys.argv) < 3:
    print(getErrorMsg(1003))
    print(getExampleString())
else:    
    if os.path.isfile(_dot + _slash + str(sys.argv[1])):

        if os.path.isfile(_dot + _slash + str(sys.argv[2])):                        

            workbook = Workbook()
            sheet = workbook.active
            sheet = createSheetTitle(sheet)
            df1 = pd.read_excel(_dot + _slash + str(sys.argv[1]), sheet_name = 0)
            df2 = pd.read_excel(_dot + _slash + str(sys.argv[2]), sheet_name = 0)
            df1List = df1.values.tolist()
            df2List = df2.values.tolist()
            index = 0
            resultInconsistencyCount = 0
            resultSabangnetCount = 0
            resultNewItemCount = 0

            print(_def)
            printLogTitle()
            printLine()

            oldNetForceCodeList = []
            oldDic = {}
            
            # 빠르게 찾기 위하여 전일재고의 넷포스 코드 배열 재 생성 및 딕셔너리 생성
            for item in df1List : 
                oldNetForceCodeList.append(item[0])
                oldDic[item[0]] = item
                
            # print(oldNetForceCodeList)
     
            for item2 in df2List :
                index = index + 1 

                # 전일재고에 코드가 존재하는지 체크
                if item2[0] in oldNetForceCodeList :                                     
                    tmpItem1 = oldDic.get(item2[0])

                    if np.isnan(item2[2]) == False : 
                        newSabangnetCode = str(item2[2])[0:6]
                    else:
                        newSabangnetCode = get_def()

                    if np.isnan(tmpItem1[2]) == False :                     
                        oldSabangnetCode = str(tmpItem1[2])[0:6]
                    else:
                        oldSabangnetCode = get_def()                        

                    # 전일재고와 수량이 다르다면..
                    if tmpItem1[16] != item2[16] :                        
                        resultInconsistencyCount = resultInconsistencyCount + 1                                        
                        sheet.append(item2 + [str(tmpItem1[16])])        
                        print(getInconsistencyString() + '\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(tmpItem1[16]) + '\t\t' + str(item2[16]) + '\t\t' + str(oldSabangnetCode) + '\t\t' + str(newSabangnetCode))                    
                    else :                          
                        # 전일재고와 수량이 같지만 사방넷 코드가 다르다면..
                        if str(oldSabangnetCode) != str(newSabangnetCode) : 
                            resultSabangnetCount = resultSabangnetCount + 1
                            sheet.append(item2 + [_sbn])
                            print(getSabangnetString() + '\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(tmpItem1[16]) + '\t\t' + str(item2[16]) + '\t\t' + str(oldSabangnetCode) + '\t\t' + str(newSabangnetCode))                            

                # 전일재고에서 발견하지 못한 넷포스코드는 신규 입고 상품
                else :
                    resultNewItemCount = resultNewItemCount + 1  
                    sheet.append(item2 + [_new])
                    print(getNewItemString() + '\t\t' + str(index) + '\t\t' + str(item2[0]) + '\t\t' + str(0) + '\t\t' + str(item2[16]) + '\t\t' + str('') + '\t\t' + str(''))

            workbook.save(getFilenamePrefix() + str(now.timestamp()) + "." + getFileExt())            
            print(_def)
            print(_def)
            printResultTitle()
            printLine()
            printResult(resultInconsistencyCount, resultSabangnetCount, resultNewItemCount)
            print(_def)

        else:
            print(getErrorMsg(1001, str(sys.argv[2])))            
            
    else:
        print(getErrorMsg(1002, str(sys.argv[1])))            
    
# end        
        
