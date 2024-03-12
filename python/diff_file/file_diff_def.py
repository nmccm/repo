def getInconsistencyString() : 
    return 'Inconsistency'

def getSabangnetString() : 
    return 'Sabangnet'

def getNewItemString() : 
    return 'New Item'

def getFilenamePrefix() :
    return 'result-'

def getFileExt() : 
    return 'xlsx'

def printLogTitle() :
    print('Flag\t\t\tLine\t\tCode\t\tQty\t\tCurrent\t\tSBN\t\tCurrent')

def printResultTitle() :
    print('Flag\t\t\tTotal Count')

def printResult(flag1 = 0, flag2 = 0, flag3 = 0) :
    print(getInconsistencyString() + '\t\t' + str(flag1))
    print(getSabangnetString() + '\t\t' + str(flag2))
    print(getNewItemString() + '\t\t' + str(flag3))

def printLine() : 
    print('-----------------------------------------------------------------------------------------------------------------')

def getErrorMsg(code = 0, arg = '') :
    if code == 1001 :
        return 'ERROR : 금일재고파일(' + str(arg) + ')을 찾을 수 없습니다.'    
    if code == 1002 :
        return 'ERROR : 전일재고파일(' + str(arg) + ')을 찾을 수 없습니다.'
    if code == 1003 : 
        return 'ERROR : 올바른 형식으로 다시 시도해주세요.'
    
def getExampleString() :
    return 'ex> file_diff.exe 전일재고파일명.xls 금일재고파일명.xls'

def createSheetTitle(sheet) :
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
    return sheet

def get_def() :
    return ''

def get_dot() :
    return '.'

def get_slash() :
    return '/'

def get_new() :
    return 'NEW'

def get_sbn() :
    return 'SBN'