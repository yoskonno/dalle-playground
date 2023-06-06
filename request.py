import requests
import json

num_requests = 100
i = 1

# "a real skull on black background"
# "a human skull on black background","num_images"

CLOUDFLARE_URL = 'https://cooking-impaired-sand-failures.trycloudflare.com/'

while i <= num_requests:
    data = {"text":"skull on a black background","num_images":10}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(CLOUDFLARE_URL + 'dalle', data=json.dumps(data), headers=headers)

    # parse the response and check if you need to continue making requests
    print(f"{response.json()} {i}/{num_requests}")

    i += 1