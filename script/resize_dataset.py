import cv2
#import time
import os
import glob

folder_gambar_cats ="../dataset/cats"
data_path = os.path.join(folder_gambar_cats,'*g')
files = glob.glob(data_path)
number = 1
for file in files:
    gambar = cv2.imread(file)
    #gray = cv2.cvtColor(gambar, cv2.COLOR_BGR2GRAY)
    gambar_resize = cv2.resize(gambar, (25,25))
    cv2.imwrite("../dataset/training_cats/{}.jpg".format(number), gambar_resize)
    print("Gambar {} berhasil di resize & ubah ke graysclale".format(number))
    number += 1






#gambar_path ="../dataset/cats/1.jpg"
#gambar = cv2.imread(gambar_path)
#gambar_resize = cv2.resize(gambar, (25,25))
#cv2.imwrite("../dataset/resize/1.jpg", gambar_resize)

#cv2.imshow("cat", gambar)
#cv2.waitKey(0)
#time.sleep(5)
#print("resize_done")