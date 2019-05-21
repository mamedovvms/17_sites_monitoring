# Sites Monitoring Utility

Checks the domains of the site.
Whether the domain has been paid for the transferred number of days, default 30 days.
And shows the server's response to the request .

# Description

As a parameter, a text file with the addresses of sites is transmitted. 
Each new address is written on a new line.
The second parameter is the number of days for which you want to check payment.
```text
# Example *.txt file
http://mail.ru
http://google.ru
http://yandex.ru
http://test_tt.ru
```

# Example

```bash
$ python check_sites.py urls.txt -d 30# possibly requires call of python3 executive instead of just python\

   URL: http://mail.ru
Server response: True
Domain paid: True

URL: http://google.ru
Server response: True
Domain paid: True

Invalid URL yandex.ru

URL: http://test_tt.ru
Server response: False
Domain paid: False

       
```
Running on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
