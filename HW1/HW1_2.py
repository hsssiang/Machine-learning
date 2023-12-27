import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_biggest_index(arr):
    return np.where(arr == np.max(arr))


# 開啟 CSV 檔案
og_data = pd.read_csv("")   # Put the .csv file path here!!
og_df = pd.DataFrame(og_data)

my_data={
    "Name":[],
    "Sex":[],
    "Age":[],
    "HR":[],
    "Height":[],
    "Weight":[],
    "BP":[]
}
my_df = pd.DataFrame(my_data)
name_arr = []

for i in range(0, len(og_df)):
    if og_df["0"][i] in name_arr:
        my_df.at[name_arr.index(og_df["0"][i]), og_df["1"][i]] = og_df["2"][i]    # og_df["1"][i]：代表原始資料的第 1th 資料（Age, Height...)
    else:
        name_arr.append(og_df["0"][i])
        my_df = pd.concat([my_df,pd.DataFrame({
            "Name":og_df["0"][i],
            "Sex":[0],
            "Age":[0],
            "HR":[0],
            "Height":[0],
            "Weight":[0],
            "BP":[0]
        })], ignore_index = True)
        my_df.at[name_arr.index(og_df["0"][i]), og_df["1"][i]] = og_df["2"][i]    # og_df["1"][i]：代表原始資料的第 1th 資料（Age, Height...)

for i in my_df:
    if i == "Name" or i == "Sex":
        continue
    else:
        my_df[i] = pd.to_numeric(my_df[i])


# 計算平均
my_df.loc[len(my_df.index)] = ["","",my_df["Age"].mean(), my_df["HR"].mean(), my_df["Height"].mean(), my_df["Weight"].mean(), my_df["BP"].mean()]

print(my_df)
print()

print("【 Biggest value of all types 】")
print("Type\tvalue\tname")
print("------------------------------------")
for i in my_df:
    if i == "Name" or i == "Sex":
        continue
    print(i, end="\t")
    arr = [x for x in my_df[i]]
    big_index = get_biggest_index(arr)
    print(my_df[i][big_index[0][0]], end="\t")
    for j in big_index[0]:
        print(my_df["Name"][j], end=', ')
    print()

my_df = my_df.loc[~((my_df['Height'] == 0) | (my_df['Weight'] == 0))]
my_df = my_df.reset_index(drop=True)
print(my_df)

height_M = [my_df["Height"][i] for i in range(0,len(my_df.index)-1) if my_df["Sex"][i] == 'M']
weight_M = [my_df["Weight"][i] for i in range(0,len(my_df.index)-1) if my_df["Sex"][i] == 'M']
height_F = [my_df["Height"][i] for i in range(0,len(my_df.index)-1) if my_df["Sex"][i] == 'F']
weight_F = [my_df["Weight"][i] for i in range(0,len(my_df.index)-1) if my_df["Sex"][i] == 'F']

# 製圖
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title("scatter of (Height, Weigth)") 
plt.scatter(height_M,weight_M, color="blue")
plt.scatter(height_F,weight_F, color="red")

plt.subplot(2, 2, 2) 
plt.title("Histogram chart of Age") 
plt.xlabel('Age')
plt.ylabel('Amounts')
plt.hist(my_df["Age"], bins=30, alpha=1, label='Data 1', rwidth=0.9)

# pie
plt.subplot(2, 2, 3) 

arr = [0,0,0,0,0,0,0,0,0,0]
types = ["0~9","10~19","20~29","30~39","40~49","50~59","60~69","70~79","80~89","90~99"]
for i in my_df["Age"]:
    arr[int(i//10)] += 1
plt.pie(arr, radius=1.2, autopct="%1.1f%%",labels=types)


# Sexual pie
arr = [0,0]
types = ["Male","Female"]
color = ["b","r"]
for i in my_df["Sex"]:
    if i == "M":
        arr[0] += 1
    elif i == "F":
        arr[1] += 1

plt.subplot(2, 2, 4) 
plt.pie(arr, radius=1.2, autopct="%1.1f%%",labels=types, colors=color)
plt.show()


