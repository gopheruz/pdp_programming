import cctv
nvr_ip =  '109.94.174.13'  
nvr_username = 'admin'      
nvr_password = 'Qwerty12'   

channels = range(101, 4003, 100) 


nvr_urls = [f'rtsp://{nvr_username}:{nvr_password}@{nvr_ip}/Streaming/Channels/{channel}' for channel in channels]

for i in nvr_urls:
    cctv.showIpcamera(i)