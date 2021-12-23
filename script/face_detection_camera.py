import cv2
detector_wajah = cv2.CascadeClassifier("../model/haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture('../video/berita.mp4')
while True:
    ret, image = cap.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
    minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in bounding_box:
        # x,y koordinat awal box
        # w,h ukuran box lebar & tinggi
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        gambar_wajah = image[y:(y+h),x:(x+w)]
        wajah_blur= cv2.blur(gambar_wajah, (40,40))
        image[y:(y+h),x:(x+w)] = wajah_blur
        # grayb = cv2.cvtColor(box, cv2.COLOR_BGR2GRAY)
        # end = x
        # start = y
    cv2.imshow("hasil", image)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()