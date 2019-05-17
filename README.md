# Sites Monitoring Utility


Checks the domains of the site. 
Has the domain been paid for at least 30 days. 
And whether the url of the site will respond with code 200.

# Description

As a parameter, a text file with the addresses of sites is transmitted. 
Each new address is written on a new line.

```text
# Example *.txt file
mail.ru
google.ru
yandex.ru
test_tt.ru
```

# Example

```bash
$ python check_sites.py urls.txt# possibly requires call of python3 executive instead of just python\

   URL: mail.ru
   Code 200: True
   Domain paid: True
   
   URL: yandex.ru
   Code 200: True
   Domain paid: True

   URL: test_tt.ru
   Code 200: False
   Domain paid: False
    
```
Running on Windows is similar.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
