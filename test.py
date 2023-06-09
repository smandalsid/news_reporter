# import logging

# # logging.debug("Debug message")
# # logging.info("Info message")
# # logging.warning("Warning message")
# # logging.error("Error message")
# # logging.fatal("Fatal message")

# logging.basicConfig(level=logging.DEBUG,
#                     format="[%(asctime)s] %(name)s %(levelname)s : %(message)s",
#                     datefmt='%Y-%m-%d %H:%M:%S'
#                     )

# # logger=logging.getLogger(__file__)
# logger=logging.getLogger("news")

# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.fatal("Fatal message")

import requests
import json

# response=requests.put("http://127.0.0.1:8000/api/google/14/", {'batch': '2', 'title': 'apicall2', 'link': 'test', 'ago': '2023-06-07', 'time': '2023-06-07T06:40:18Z'})
response=requests.get("http://127.0.0.1:8000/api/google/")
print(response.json())
