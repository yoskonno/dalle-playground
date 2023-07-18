import requests
import json
from datetime import datetime

num_requests = 100 # B
i = 1

# "a real skull on black background"
# "a human skull on black background","num_images"

CLOUDFLARE_URL = 'https://offense-southampton-addresses-suppliers.trycloudflare.com/' # B

while i <= num_requests:
    data = {"text":"skull on a black background","num_images":8}
    headers = {'Content-Type': 'application/json'}

    # human skull image on a black background # some of them were pretty good

    response = requests.post(CLOUDFLARE_URL + '/dalle', data=json.dumps(data), headers=headers)

    # parse the response and check if you need to continue making requests
    print(f"{response.json()} {i}/{num_requests} - {datetime.now().strftime('%H:%M:%S %d-%m-%Y')}")

    i += 1