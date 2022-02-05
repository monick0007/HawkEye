import cv2
import datetime
import time
from wireshark_capture import wireshark_cap
from logger_varify import check_keylog
vc=cv2.VideoCapture(0)   
# url='http://192.168.2.13:8080/video'
# vc.open(url)
time.sleep(5)
s=0
# if not vc.isOpened():
#         print("Cannot open camera")
#         exit()
# cv2.namedWindow("starting capturing", cv2.WINDOW_NORMAL) 
while True:
    s=s+1
    image_capture,check=vc.read()
    imS = cv2.resize(check, (960, 540))                # Resize image

    print(image_capture)
    print(check)
    cv2.startWindowThread()
    # gray=cv2.cvtColor(imS,cv2.COLOR_BGR2GRAY)
    # cv2.namedWindow("imS")
    cv2.imshow("stating capture",check)
    # cv2.imshow("starting capture",check)
    final1=wireshark_cap()
    print("finished phase 1 intitiating phase 2")
    final2=check_keylog()
    key=cv2.waitKey(1)
    if key==ord('q') or (final1 is None and final2 is None):
        break
    else:
        print(final1)
        print(final2)
        break
print(s)    
vc.release()
cv2.destroyAllWindows()

