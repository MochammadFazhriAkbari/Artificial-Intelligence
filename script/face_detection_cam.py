import cv2
detector_wajah = cv2.CascadeClassifier("../model/haarcascade_frontalface_default.xml")

image = cv2.VideoCapture(0)
counter = 0
while True:
    ret, frame = image.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bounding_box = detector_wajah.detectMultiScale(gray, scaleFactor=1.01,
    minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
   
    for (x, y, w, h) in bounding_box:
        counter+=1
        gambar_wajah = frame[y:(y+h),x:(x+w)]
        cv2.imwrite("../output/{}.jpg".format(counter), gambar_wajah)
        wajah_blur= cv2.blur(gambar_wajah, (40,40))
        frame[y:(y+h),x:(x+w)] = wajah_blur

    cv2.imshow("Vid", frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
image.release()
cv2.cv2.destroyAllWindows()


