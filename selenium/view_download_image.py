################################################################################################
# Python coder : sjkim (kim.sajoong@gmail.com)
# last update  : 2021-Feb-09
#----------------------------------------------------------------------------------------------#
import os
import cv2
import numpy as np
import imutils
from glob import glob
from pprint import pprint
#----------------------------------------------------------------------------------------------#
cwd      = os.getcwd()
data_dir = os.path.join("dataset", "*")
dir_list = glob(f"{data_dir}")
print(cwd)
print("="*50)
print("====== 이미지 살펴볼 폴더 번호를 선택하세요. =======") 
print("="*50)
for i, src_dir in enumerate(dir_list, start=1):
    print(f"[{i:03d}] : {src_dir}")
print("="*50)
#----------------------------------------------------------------------------------------------#
while True:    
    try:
        choice = int(input("[번호] >>> "))
    except Exception as e:
        continue
    finally:
        if 1 <= choice <= i:
            break
        else:
            continue
print("="*50)        
print(f"당신의 선택은 {choice}번 [{dir_list[choice-1]}] 폴더입니다.")
print("="*50)
#----------------------------------------------------------------------------------------------#
src_dir   = dir_list[choice-1]
file_list = glob(os.path.join(src_dir,"*.*"))
pprint(file_list)
print("="*50)
#----------------------------------------------------------------------------------------------#
cwd = os.getcwd()

for file in file_list:
    
    path = os.path.join(cwd, file)              # full path 만들기
    #print(path)
    
    if path.lower().endswith("gif"):            # gif error 처리
        gif = cv2.VideoCapture(path)
        img = gif.read()
    else:        
        img_array = np.fromfile(path, np.uint8)  # 한글 이름 오류 처리
        img       = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    
    if 2_000 < img.shape[1] <= 3_000:  
        print("original", file, img.shape)
        img = imutils.resize(img, width=int(img.shape[1]*(7/10)))
        print("resized", file, img.shape)
        
    if 3_000 < img.shape[1] <= 4_000:  
        print("original", file, img.shape)
        img = imutils.resize(img, width=int(img.shape[1]*(6/10)))
        print("resized", file, img.shape)
        
    if 4_000 < img.shape[1] <= 5_000: 
        print("original", file, img.shape)
        img = imutils.resize(img, width=int(img.shape[1]*(4/10)))
        print("resized", file, img.shape)
        
    cv2.imshow("Image", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
#----------------------------------------------------------------------------------------------#
