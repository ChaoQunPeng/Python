import requests
import re
import datetime
import os

from bs4 import BeautifulSoup

import collectWebUrlClass
import parseUrl

# requests.adapters.DEFAULT_RETRIES = 5

# 收集页面上的URL
collectWebUrlClass.collectUrl()

# 解析URL
d = parseUrl.parseUrlFunc()


