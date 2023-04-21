import cv2

# 读取图像并转为灰度图像
img = cv2.imread('image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 边缘检测
edges = cv2.Canny(gray, 100, 200)

# 二值化处理
ret, binary = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY)

# 统计像素点数量
edge_pixel_count = cv2.countNonZero(binary)
total_pixel_count = binary.shape[0] * binary.shape[1]

# 计算边缘点占比
edge_ratio = edge_pixel_count / total_pixel_count

print("边缘点占比: {:.2%}".format(edge_ratio))
