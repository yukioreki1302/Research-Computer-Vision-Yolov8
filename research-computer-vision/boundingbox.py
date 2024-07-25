import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np
import statistics 
img =cv2.imread("C:/Users/ADMIN/Desktop/Computer Vision/lesson4/frame_0000.jpg")
h = img.shape[0]
w = img.shape[1]
print('w-img: ',h)
print('h-img: ',w)
folder_path = "C:/Users/ADMIN/Desktop/Computer Vision/lesson4/runs/detect/predict/labels"
file_list = []

n = 1140


for i in range(1, n+1):
    file_name = f"fish_{i}.txt"
    file_path = folder_path + "/" + file_name
    file_list.append(file_path)

listxy=[]
listx_left=[]
listx_right=[]



for file_path in file_list:
    with open(file_path, "r") as file:
        content = file.readlines()
        for l in content:
            lines = l.split()
            xc = float(lines[1])
            yc = float(lines[2])
            x = (float(xc) * w)/1000
            y = (float(yc) * h)/1000
            listxy.append((x,y))


            listxleft = sorted(listxy,key=lambda i:i[0])[:3]
            listxright = sorted(listxy,reverse=True, key=lambda i:i[0])[:3]
        for i in listxleft:
            if (i in listxy):
                listxy.remove((i))

        for i in listxright:
                if (i in listxy):
                    listxy.remove(i)

        for i in listxleft:
            listx_left.append(i)
            
        for i in listxright:
            listx_right.append(i)

min_x = min(listxy, key=lambda i: i[0])[0]
max_x = max(listxy, key=lambda i: i[0])[0]

temp_listx_left = [coord for coord in listx_left if coord[0] <= min_x-0.008]
temp_listx_right = [coord for coord in listx_right if coord[0]+0.008 >= max_x] #listx_right chỉ chứa các phần tử có tọa độ x lớn hơn hoặc bằng max_x.
listx_left = temp_listx_left
listx_right = temp_listx_right
for i in listxy:
    if (i[0] >= min(temp_listx_right, key=lambda i: i[0])[0]):
        listxy.remove(i)
'''
print(max(listxy, key=lambda i: i[0])[0])
print(min(temp_listx_right, key=lambda i: i[0])[0])
'''


x_left = [pair[0] for pair in listx_left]
y_left = [pair[1] for pair in listx_left]
x_middle = [pair[0] for pair in listxy]
y_middle = [pair[1] for pair in listxy]
x_right = [pair[0] for pair in listx_right]
y_right = [pair[1] for pair in listx_right]

print(listx_left)
# plt.scatter(x_middle, y_middle, c='red')
# plt.scatter(x_left, y_left, c='yellow')
# plt.scatter(x_right, y_right, c='green')
# plt.xlabel('X')
# plt.ylabel('Y')
#plt.title('Scatter Plot')

'''
x_values = [coord[0] for coord in temp_listx_left]
y_values = [coord[1] for coord in temp_listx_left]
median_x = statistics.median(x_values)
median_y = statistics.median(y_values)
mode_x = statistics.mode(x_values)
mode_y = statistics.mode(y_values)
print("Median của tọa độ x:", median_x)
print("Median của tọa độ y:", median_y)
print("Mode của tọa độ x:", mode_x)
print("Mode của tọa độ y:", mode_y)
mean_x_left = sum(i[0] for i in temp_listx_left)/len(temp_listx_left)
print("Giá trị trung bình của tọa độ x:", mean_x_left)
mean_y_left = sum(i[1] for i in temp_listx_left)/len(temp_listx_left)
print("Giá trị trung bình của tọa độ y:", mean_y_left)
'''
# median_x = statistics.median(x_right)
# print("Median của tọa độ x:", median_x)
# mode_x = statistics.mode(x_right)
# print("Mode của tọa độ x:", mode_x)
# mean_x_left = sum(i for i in x_right)/len(listx_right)
# print("Giá trị trung bình của tọa độ x:", mean_x_left)

# plt.hist(x_right)
# plt.xlabel('Value')
# plt.ylabel('Frequency')
# plt.title('Histogram Plot')

# plt.show()


    


