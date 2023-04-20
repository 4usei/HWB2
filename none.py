import cv2
import numpy as np

# 读取图像
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 添加椒盐噪声
noise_img1 = np.copy(img)
salt_vs_pepper = 0.2
noise = np.random.rand(*img.shape)
noise_img1[noise < salt_vs_pepper/2] = 0
noise_img1[noise > 1 - salt_vs_pepper/2] = 255

# 添加高斯噪声
noise_img2 = np.copy(img)
mean = 0
var = 100
sigma = var ** 0.5
gauss = np.random.normal(mean, sigma, img.shape)
noise_img2 = noise_img2 + gauss

# 定义Canny算子的参数
canny_low = 100
canny_high = 200

# 在添加椒盐噪声的图像上进行边缘检测
edges1 = cv2.Canny(noise_img1, canny_low, canny_high)

# 在添加高斯噪声的图像上进行边缘检测
edges2 = cv2.Canny(noise_img2, canny_low, canny_high)

# 显示图像和边缘检测结果
cv2.imshow('Original Image', img)
cv2.imshow('Salt and Pepper Noise Image', noise_img1)
cv2.imshow('Edges with Salt and Pepper Noise', edges1)
cv2.imshow('Gaussian Noise Image', noise_img2)
cv2.imshow('Edges with Gaussian Noise', edges2)
cv2.waitKey(0)
cv2.destroyAllWindows()
