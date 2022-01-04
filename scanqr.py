import io
import time
import picamera
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
font = cv2.FONT_HERSHEY_PLAIN

try:
    while True:
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            time.sleep(0.5)
            camera.resolution = (640, 480)
            camera.capture(stream, format='jpeg')
        # Construct a numpy array from the stream
        data = np.fromstring(stream.getvalue(), dtype=np.uint8)
        # "Decode" the image from the array, preserving colour
        image = cv2.imdecode(data, 1)
        #pyzbar tries to find qr code data from the image
        decodedObjects = pyzbar.decode(image)
        for obj in decodedObjects:
            print("We found data! :", obj.data)
            cv2.putText(image, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)
        cv2.imshow('frame',image)
        #time.sleep(1)
        #cv2.waitKey(1)
        if cv2.waitKey(1) == ord('q'):
            break
    print("q pressed")
except KeyboardInterrupt:
    print("\nYou quit wrong")
finally:
    exit()
