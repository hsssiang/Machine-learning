import os
import cv2
import time
from PIL import Image
import numpy as np

start_time = time.time()
file_path = r"HW1-image/reference/processing/"
test_file_path = r"HW1-image/test/"
target = list()
all_file = list()
imag_array = list()
test_index = ["cat", "dog", "cat", "dog", "cat", "cat", "dog", "dog", "dog", "cat", "cat", "dog", "cat", "dog", "dog",
              "cat", "dog", "dog", "cat", "cat"]
for i in range(1, 101):
    all_file.append(str(i) + ".jpg")
    if i < 51:
        target.append("cat")
    else:
        target.append("dog")
for r in range(1, 20, 2):
    acc = 0
    for i in range(1, 21):
        cat = 0
        dog = 0
        compute_outcome = list()
        test_file = "pic" + str(i) + ".jpg"
        temp = Image.open(test_file_path + test_file)
        test_image = temp.resize((64, 64))
        test_image_array = np.array(test_image)
        for file in all_file:
            train_image = Image.open(file_path + file)
            train_image_array = np.array(train_image)
            ori_array = test_image_array - train_image_array
            outcome = 0
            for j in range(3):
                for k in range(64):
                    for q in range(64):
                        outcome += ori_array[k, q, j]
            outcome = outcome / (3 * 64 * 64)
            compute_outcome.append(outcome)
        sort_outcome = sorted(compute_outcome, reverse=True)
        for g in range(r):
            if compute_outcome.index(sort_outcome[g]) > 50:
                dog += 1
            else:
                cat += 1
        if dog > cat:
            compare = "dog"
        else:
            compare = "cat"
        if compare == test_index[i - 1]:
            acc += 1
    print( "[ ( K =" , r ,") Accuracy", acc / 20 , "]" )
print("--- %s seconds ---" % (time.time() - start_time))





