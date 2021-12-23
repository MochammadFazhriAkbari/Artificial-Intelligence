import cv2
import os
import glob
detector_wajah = cv2.CascadeClassifier("../model/haarcascade_frontalface_default.xml")

data_path = os.path.join('../output_model/wanita 1', '*g')
files = glob.glob(data_path)
output = 1
for file in files:
    print(file)
    image = cv2.imread(file)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    #image = cv2.imread("../images/rekt.jpg"    
    bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
    minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in bounding_box:
        output +=1
        gambar_wajah = image[y:(y+h),x:(x+w)]
        cv2.imwrite("..//output_model/wanita filtered/a_{}.jpg".format(output), gambar_wajah)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.waitKey(1)
    

    


#image = cv2.imread("../images/rekt.jpg")



    # x,y koordinat awal box
    # w,h ukuran box lebar & tinggi
    #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # grayb = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
    # end = x
    # start = y
#cv2.imshow("hasil", image)
#cv2.imwrite("../output/hasil_4.jpg", image)
#cv2.waitKey(0)
