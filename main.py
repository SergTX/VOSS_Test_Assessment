import OpenSSL
import requests

# s = requests.Session()
#
# s.verify = 'CApath: /etc/ssl/certs'

r = requests.get('https://ultimateqa.com/', verify='/etc/ssl/certs/ca-certificates.crt')

