import cv2
import numpy as np


def run():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1920)
    cap.set(4, 1080)

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #lower_android = np.array([130, 50, 80])
        #upper_android = np.array([160, 100, 140])
        lower_android = np.array([40, 140, 140])
        upper_android = np.array([140, 255, 255])

        # Display the resulting frame
        width = cap.get(3)
        height = cap.get(4)

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_android, upper_android)
        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame, frame, mask=mask)

        ret, thresh = cv2.threshold(mask, 127, 255, 0)
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        biggest_area = 0
        start_point = (0, 0)
        end_point = (0, 0)

        for c in contours:
            area = cv2.contourArea(c)
            if area > biggest_area:
                biggest_area = area
                x, y, w, h = cv2.boundingRect(c)
                start_point = (x, y)
                end_point = (x + w, y + h)

        cv2.rectangle(res, start_point, end_point, (0, 255, 0), 2)

        #cv2.line(mask, (top, bot), (0, 0), (255, 0, 0), 5)

        #font = cv2.FONT_HERSHEY_SIMPLEX
        #msg = str(width) + ' ' + str(height)
        #cv2.putText(frame, msg, (0, int(height)), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

        #if cv2.waitKey(1) & 0xFF == ord('w'):
            #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #    cv2.imwrite('mask.png', mask)
        #    print('taken image')

        #cv2.circle(res, (int(width/2), int(height/2)), 60, (0,0,255), 3)
        cv2.imshow('frame', res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    run()
