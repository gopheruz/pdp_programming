import cv2
def showIpcamera(url):
    print(url)
    cap = cv2.VideoCapture(url)

    if not cap.isOpened():
        print("Error: Could not open camera stream.")
        exit()

    window_name = 'Hikvision Camera View'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL) 
    cv2.resizeWindow(window_name, 800, 600) 

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        cv2.imshow(window_name, frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


