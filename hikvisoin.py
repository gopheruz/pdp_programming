from hikvisionapi import Client

# Replace IP, username, and password with your device's details
cam = Client('http://109.94.174.13:5050', 'admin', 'Qwerty12')

# Example: Get video stream info
response = cam.Streaming.channels[102].picture(params={'format': 'jpeg'})
with open('snapshot.jpg', 'wb') as f:
    f.write(response.content)
