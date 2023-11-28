# import time
#
# import requests
#
#
# def check_status():
#     response = requests.get('http://127.0.0.1:8000')
#     if response.status_code == 200:
#         return 'ok'
#     else:
#         return 'not ok'
#
#
# def schedule_request():
#     while True:
#         check_status()
#         time.sleep(5)
