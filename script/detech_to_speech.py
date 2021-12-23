import requests
import playsound
import cv2
detector_wajah =cv2.CascadeClassifier("../model/haarcascade_frontalface_default.xml")
image = cv2.imread("../images/rekt.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
    minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
orang = []
for (x, y, w, h) in bounding_box:
    box = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0))
    orang.append(box)
url = 'http://lisanx.pptik.id/'
if (len(orang)) > 0:
    teks = "Hello, good morning Fazhri !"
cv2.imshow("hasil", image)
x = requests.post(url, data = teks)
file = " {}.mp3".format("file_respon")
with open(file, "wb") as f:
    f.write(x.content)
playsound.playsound(file)