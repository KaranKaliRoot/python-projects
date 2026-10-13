
#https://pixe.la/v1/users/rudrabhardwaj/graphs/graph1.html------------main link
import requests
from datetime import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "rudrabhardwaj"
TOKEN = "bahsqdf36t87485yi3uhewd"

today = datetime.now()
user_params = {
    "token": USERNAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=PIXELA_ENDPOINT,json=user_params)
# data = response.json()
# print(data)
graph_config = {
    "id": "graph1",
    "name": "coding graph",
    "type": "int",
    "unit": "minute",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
Graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# response = requests.post(url=Graph_endpoint, json=graph_config, headers=headers)
# print(response.json())
pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many minutes did you code today?: ")
}
response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)
# new_pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# new_pixel_data = {
#     "quantity": "97"
# }
# response = requests.put(url=new_pixel_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)
