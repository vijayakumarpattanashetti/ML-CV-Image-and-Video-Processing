import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('5_op(pic_0).png',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
hist,bins = np.histogram(res.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(res.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
cv2.imshow('res.png',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
