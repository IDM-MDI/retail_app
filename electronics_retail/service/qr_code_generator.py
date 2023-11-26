import requests


def generate_qr_code(data):
    qr_api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={data}"
    response = requests.get(qr_api_url)
    return response.content if response.status_code == 200 else None
