import cv2
import numpy as np
from matplotlib import pyplot as plt

def a(y):
    pass

frame=cv2.imread("/Users/shinsungmin/Documents/working/nunap/aa.jpg")
resize=cv2.resize(frame,(720,480))
skin=cv2.cvtColor(resize,cv2.COLOR_BGR2YCrCb)
ran=cv2.inRange(skin,(0,127,65),(255,173,165))
ig,cr,hs=cv2.findContours(ran,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cor=cr[1]
x,y,w,h=cv2.boundingRect(cor)
hu=cv2.convexHull(cor)
hu[0:,0,0]-=x
hu[0:,0,1]-=y
#print(hu)
x,y,w,h=cv2.boundingRect(cor)
img=cv2.rectangle(resize,(x,y),(x+w,y+h),(0,255,0),2)
cr_img=ran[y:y+h,x:x+w]
ds=cv2.distanceTransform(cr_img,cv2.DIST_L2,5)
cedt=cv2.minMaxLoc(ds)
center=cedt[3]
crc=cv2.cvtColor(cr_img,cv2.COLOR_GRAY2BGR)
#imgg=cv2.drawContours(crc,[hu],0,[0,255,0])
dt=((ds-ds.min())/(ds.max()-ds.min())*255).astype(np.uint8)
dt=cv2.resize(dt,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.blur(dt,(4,4))
xn=dt.shape
i=0
dts=list()
while(i<xn[1]):
    for j in dt[i]:

cv2.namedWindow("x")
cv2.createTrackbar("x","x",0,len(dt[2])-1,a)
xx=0
print(dt)
kk=1
if kk==1:
    while(1):
        cv2.imshow("big", img)
        cv2.imshow("hand", cr_img)
        cv2.imshow("joint", dt)
        cv2.imshow("x",dt[xx])
        plt.plot(dt[126])
        plt.show()
        if cv2.waitKey(1) and 0xFF==ord("q"):
            break
        xx=cv2.getTrackbarPos("x","x")
    cv2.destroyAllWindows()
