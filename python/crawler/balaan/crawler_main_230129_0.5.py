print('while....')

index = 1
url = "backoffice?page="
param = "&andappend=1"

while index < 10:
    tmp = url + str(index) + param
    print(f'index : {index}, {tmp}')        
    index = index + 1

