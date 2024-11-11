import requests
from requests.auth import HTTPDigestAuth
import urllib3

# Suppress the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Replace with your device information
device_ip = "86.62.3.158"
username = "admin"
password = "Themeister@25"
# List of possible endpoints
endpoints = [
    "/ISAPI/Intelligent/FDLib/FDSearch",
    "/ISAPI/AccessControl/FDLib/FDSearch",
    "/ISAPI/Intelligent/FaceAnalysis/FDLib/FDSearch",
    "/ISAPI/System/status",
    "/ISAPI/Event/notification/alertStream"
]

# Try each endpoint
for endpoint in endpoints:
    url = f"https://{device_ip}{endpoint}"
    try:
        response = requests.get(url, auth=HTTPDigestAuth(username, password), verify=False)
        if response.status_code == 200:
            print(f"Data retrieved successfully from {endpoint}:")
            print(response.json())
            break
        else:
            print(f"Failed to retrieve data from {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred for {endpoint}: {e}")
