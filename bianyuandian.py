import cv2


# 读入图像
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 获取图像高度和宽度
height, width = img.shape[:2]

# 统计边缘像素中值为255的像素数量
edge_pixels = 0
for i in range(height):
    for j in range(width):
        if i == 0 or j == 0 or i == height-1 or j == width-1:
            if img[i][j] == 255:
                edge_pixels += 1

# 计算边缘点（已置255）的数量占图像总像素数的比例
total_pixels = height * width
edge_pixels_ratio = edge_pixels / total_pixels

print("边缘点（已置255）的数量占图像总像素数的比例为:", edge_pixels_ratio)

