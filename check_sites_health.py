from datetime import datetime, timedelta
import whois
import argparse
import requests
import os


def get_cmd_params():
    parser = argparse.ArgumentParser()
    parser.add_argument('fileurls', help='File site url')
    parser.add_argument('-d', '--delta', type=int, help='Paid period in days')
    params = parser.parse_args()

    if not params.delta or params.delta < 0:
        parser.error('The parameter must be greater than zero')

    if not os.path.isfile(params.fileurls):
        parser.error('File not found')

    return params


def load_urls4check(path):
    with open(path, 'rt') as file_urls_check:
        urls_check = file_urls_check.read().splitlines()
    return urls_check


def is_server_respond_with_ok(url):
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        return False
    return response.ok


def get_domain_expiration_date(domain_name):
    response = whois.whois(domain_name)
    return response['expiration_date']


def is_expiration_date_valid(expiration_date, delta):
    if not expiration_date or not isinstance(expiration_date, datetime):
        return False
    today = datetime.utcnow()
    return expiration_date >= today + timedelta(days=delta)


def main():
    template_print = '''
URL: {}
Server response: {}
Domain paid: {}'''
    params = get_cmd_params()

    urls = load_urls4check(params.fileurls)
    for url in urls:
        expiration_date = get_domain_expiration_date(url)
        try:
            print(template_print.format(
                url,
                is_server_respond_with_ok(url),
                is_expiration_date_valid(expiration_date, params.delta)
            ))
        except requests.exceptions.MissingSchema:
            print("\nInvalid URL '{}'".format(url))


if __name__ == '__main__':
    main()
