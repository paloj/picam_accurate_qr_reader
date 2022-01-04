import io
import time
import picamera
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
font = cv2.FONT_HERSHEY_PLAIN

'''Settings for picamera'''
cam = picamera.PiCamera()
cam.resolution = (640, 480)

'''Settings for other cameras. (x)=cam no.'''
#cam = cv2.VideoCapture(0)

try:
    while True:
        
        time.sleep(0.25)

        '''RASPICAM'''
        stream = io.BytesIO()
        cam.capture(stream, format='jpeg')
        # Construct a numpy array from the stream (picamera)
        data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        # "Decode" the image from the array, preserving colour
        image = cv2.imdecode(data, 1)

        '''OTHER CAMERAS'''
        #return_value, image = cam.read()

        '''LOOK FOR QR CODES'''
        #pyzbar tries to find qr code data from the image
        decodedObjects = pyzbar.decode(image)
        #If codes found then:
        for obj in decodedObjects:
            print("We found data! :", obj.data)
            #Print data to image (optional)
            cv2.putText(image, str(obj.data), (50, 50), font, 2,
                        (255, 0, 0), 3)

        '''DISPLAY IMAGE'''
        cv2.imshow('frame',image)

        if cv2.waitKey(1) == ord('q'):
            break
    print("q pressed")
except KeyboardInterrupt:
    print("\nYou quit wrong")
finally:
    exit()
