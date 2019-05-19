from datetime import datetime, timedelta
import whois
import argparse
import requests


TIME_DELTA = 30


def get_cmd_params():
    parser = argparse.ArgumentParser()
    parser.add_argument('fileurls', type=argparse.FileType('rt'), help='File site url')
    return parser.parse_args()


def load_urls4check(path):
    with open(path, 'rt') as file_urls_check:
        urls_check = file_urls_check.read().splitlines()
    return urls_check


def get_valid_url(url):
    if 'http://' in url or 'https://' in url:
        return url
    else:
        return 'https://{}'.format(url)


def is_server_respond_with_200(url):
    try:
        response = requests.get(get_valid_url(url))
    except requests.exceptions.ConnectionError:
        return False
    return response.ok


def get_domain_expiration_date(domain_name):
    response = whois.whois(domain_name)
    return response['expiration_date']


def is_expiration_date_valid(expiration_date):
    if not expiration_date:
        return False
    today = datetime.utcnow()
    return expiration_date >= today + timedelta(days=TIME_DELTA)


def main():
    template_print = '''
    URL: {}
    Code 200: {}
    Domain paid: {}'''
    params = get_cmd_params()

    urls = load_urls4check(params.fileurls.name)
    for url in urls:
        expiration_date = get_domain_expiration_date(url)
        print(template_print.format(url,
                                    is_server_respond_with_200(url),
                                    is_expiration_date_valid(expiration_date)))


if __name__ == '__main__':
    main()
