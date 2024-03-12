import time
import os

kwdList = [
    "XXW00G0DE50NHV B999","XXM0GW05470RE0 B608 7","XXM0GW05470RE0 C405","XXM64C00640RE0 C405","XXW79A0DE70MID B001","XXW79A0DE70MID B999",
    "XXW79A0HM60MBW B999","XXM0GW05470EK0 B999",
    "XXW0FW050305J1 9996","6231775","6300068","6231539","6226438","6301346","6235350","6218025","6224892","6235347","6218031","6238773","6235331",
]


# os.path.isdir()

f = open("logs/240130.log", 'w')
for i in range(1, 11):
    data = "%dline.....\n" % i
    print(data)
    f.write(data)
f.close()

# for item in kwdList:
#     print(item)
#     time.sleep(1)