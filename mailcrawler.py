#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pip3 install requests, urllib3
# cat ~/sites.txt | while read line; do python3 mailcrawler.py $line; done
import re
import sys
import urllib3
import requests
import urllib.parse
import csv

def extract_emails_from_url(url, user_agent, timeout=10):
    try:
        url_parts = urllib.parse.urlparse(url)
        if not url_parts.scheme:
            url = "https://" + url  # Adiciona "https" como protocolo padrão se não estiver especificado

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)  # Desativa erros de certificado SSL

        headers = {"User-Agent": user_agent}

        response = requests.get(url, headers=headers, verify=False, timeout=timeout)  # Adiciona o timeout aqui
        response.raise_for_status()  # Verifica se a solicitação teve êxito

        email_pattern = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9]*\\.[a-zA-Z.]+[a-zA-Z])"
        emails = set()

        for email in re.findall(email_pattern, response.text):
            email = email.lower()
            emails.add(email)

        return emails

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a solicitação HTTP para {url}.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def save_emails_to_csv(site, emails):
    with open("emails.csv", "a", newline="") as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Site", "Email"])

        for email in emails:
            writer.writerow([site, email])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Lista de sites não informada!\nUse: {sys.argv[0]} site1 site2 site3")
        sys.exit(1)

    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
    sites = sys.argv[1:]

    for site in sites:
        emails = extract_emails_from_url(site, user_agent, timeout=3)  # Especifique o timeout desejado (em segundos)
        if emails:
            print(f"Emails encontrados em {site}:")
            for email in emails:
                print(email)
            save_emails_to_csv(site, emails)
