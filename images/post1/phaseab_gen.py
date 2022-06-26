import matplotlib.pyplot as plt
import numpy as np

yA=[0,]
xA=[0,0,1,1,4,4,5,5,8,8]

yB=[0,0,1,1,0,0,1,1,0]

xB=[0,2,2,3,3,6,6,7,7]

l1=plt.plot(xA,yA,'r', label="Phase A")
l2=plt.plot(xB,yB,'b', label="Phase A")
plt.xticks([])
plt.yticks([])
plt.title("Phase A/B waveform")
plt.xlabel("time")
plt.ylabel("Voltage Level")
plt.legend()
plt.show()