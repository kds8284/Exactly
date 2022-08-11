import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

'''
x = np.array([5, 10, 15])
y = np.array([10, 20, 15])

plt.plot(x, y, 'b-o', label='Data 1')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()
'''
'''
## 2. 라인 그래프 생성하기##
x =np.linspace(0, 2, 100)# --> 0부터 2까지는 100개로 나누기
y1 = 0.5*x # -- > 기울기가 0.5 이고, x를 곱한 것( == 선형대수)
y2 = 0.5*x**2 # -- > 기울기가 0.5인 2차 함수(quadratic)
y3 = 0.5*x**3 # -- > 기울기가 0.5인 3차 함수(cublic)

plt.plot(x, y1, label="linear")
plt.plot(x, y2, label="quadratic")
plt.plot(x, y3, label="cublic")

plt.legend() # -- > label를 통한 구분 (그래프 위에 표시)
plt.show() # -- > 그래프 시각화 생성하기
'''
## BGR & RGB
# 1. 이미지 불러오기
image = cv.imread('D:/11001dongseon/Exactly/color.png')

# 2. BGR
plt.figure()
plt.imshow(image)
plt.title("1")
'''
plt.show()
'''
# 3. RGB
rgb =cv.cvtColor(image, cv.COLOR_BGR2RGB)
plt.figure()
plt.imshow(rgb)
plt.title("RGB")
# plt.show()

# 4. Gray
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray)
plt.title("GRAY")
#plt.show()

# 5. Convert to the Gray
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title("GRAY")
#plt.show()

# bluer
blur =cv.blur(image, (50,50))
blur =cv.cvtColor(blur, cv.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(rgb)
plt.title("RGB")
plt.subplot(122)
plt.imshow(blur)
plt.title("Bluer")

#plt.show()

# 7. Edge Detction
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title('Gray')

edges = cv.Canny(gray, 100, 200)
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title("Gray")
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.show() 