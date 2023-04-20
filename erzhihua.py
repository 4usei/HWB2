import cv2


# 读取图像
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 定义阈值
thresh_value =127
max_value = 255

# 对图像进行二值化处理
ret, thresh = cv2.threshold(img, thresh_value, max_value, cv2.THRESH_BINARY)




# 显示二值化结果
cv2.imshow('Thresholded Image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()






