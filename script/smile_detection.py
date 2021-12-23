import cv2
import time
#fps = > frame per second
detector_wajah = cv2.CascadeClassifier("../model/haarcascade_frontalface_default.xml")
detector_senyum = cv2.CascadeClassifier("../model/haarcascade_smile.xml")
#read gambar 
image = cv2.imread("../images/rekt.jpg")
# ubah ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#deteksi wajah
bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
   minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

for (x, y, w, h) in bounding_box:
    # ini kode untuk membuat persegi pada suatu gambar
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    box_wajah = cv2.rectangle(gray, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # mau slicing gambar
    # koordinat awal persegi (x,y) , koordinat akhir ((x+w),(y+h))
    gambar_wajah = image[y:(y+h),x:(x+w)]
    cv2.imwrite("../output/hasil_crop.jpg", gambar_wajah)
    bounding_box_senyum = detector_senyum.detectMultiScale(box_wajah, 1.01, 15)
    if len(bounding_box_senyum) > 0:
        cv2.putText(image, "senyum terdeteksi", (x,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    # grayb = cv2.cvtColor(box_wajah, cv2.COLOR_BGR2GRAY)
    # end = x
    # start = y
cv2.imshow("hasil", image)
cv2.imwrite("../output/hasil_haarcascade.jpg", image)
cv2.waitKey(0)


