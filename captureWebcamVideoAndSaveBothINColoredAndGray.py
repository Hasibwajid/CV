# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2

vid = cv2.VideoCapture(0)

# videoWriter for save video

out_colored = cv2.VideoWriter(
    'D:\\colored.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (700, 450))
out_gray = cv2.VideoWriter('D:\\gray.avi', cv2.VideoWriter_fourcc(
    *'XVID'), 20, (700, 450), isColor=False)

while vid.isOpened():
    ret, frame = vid.read()

    if ret == True:
        frame = cv2.resize(frame, (700, 450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        colored = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        cv2.imshow('Colored Video', frame)
        cv2.imshow('Grayscale Video', gray)

# to save these videos to writer

        out_colored.write(frame)
        out_gray.write(gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to stop reading frames
            break
    else:
        break

vid.release()
out_colored.release()
out_gray.release()
cv2.destroyAllWindows()
