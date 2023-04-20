import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

# 读取图像
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# 添加椒盐噪声
noise_img1 = np.copy(img)
salt_vs_pepper = 0.2
noise = np.random.rand(*img.shape)
noise_img1[noise < salt_vs_pepper/2] = 0
noise_img1[noise > 1 - salt_vs_pepper/2] = 255

# 定义Canny算子的参数
canny_low = 100
canny_high = 200

# 在添加椒盐噪声的图像上进行边缘检测
edges1 = cv2.Canny(noise_img1, canny_low, canny_high)

end_time = time.time()
total_time = end_time - start_time

print("代码运行耗时：", total_time, "秒")



# 显示图形
plt.subplot(121), plt.imshow(img_RGB), plt.title('原始图像'), plt.axis('off')  # 坐标轴关闭
plt.subplot(122), plt.imshow(Prewitt, cmap=plt.cm.gray), plt.title('Prewitt算子'), plt.axis('off')
plt.show()