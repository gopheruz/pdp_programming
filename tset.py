import cv2
import numpy as np

def showIpcamera(urls):
    # Calculate the number of rows and columns for displaying cameras
    num_cameras = len(urls)
    cols = 8  # Number of columns
    rows = (num_cameras + cols - 1) // cols  # Calculate rows needed

    # Create a named window
    window_name = 'IP Camera View'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, 1600, 1200)  # Set window size

    caps = [cv2.VideoCapture(url) for url in urls]

    # Main loop
    while True:
        frames = []
        for cap in caps:
            ret, frame = cap.read()
            if not ret:
                frame = np.zeros((480, 640, 3), dtype=np.uint8)  # Create a black frame if failed to read
            frames.append(frame)

        # Create a blank image to hold all camera feeds
        grid_image = np.zeros((480 * rows, 640 * cols, 3), dtype=np.uint8)

        # Place each camera frame in the grid
        for idx, frame in enumerate(frames):
            row = idx // cols
            col = idx % cols
            if frame is not None:
                # Resize the frame to fit in the grid
                frame = cv2.resize(frame, (640, 480))
                grid_image[row * 480:(row + 1) * 480, col * 640:(col + 1) * 640] = frame

        cv2.imshow(window_name, grid_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    for cap in caps:
        cap.release()
    cv2.destroyAllWindows()

# Generate camera URLs
channels = range(101, 4001, 100)  # Modify range as needed
urls = [f"rtsp://admin:Qwerty12@3.76.113.114:65116/Streaming/Channels/{channel}" for channel in channels]

showIpcamera(urls)
