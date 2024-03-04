#!/usr/bin/env python3
# pip3 install python-whois
import whois
import datetime

def check_domain(domain_name):
    """
    Verifica a data de expiração de um domínio e calcula os dias restantes até a expiração.

    Args:
        domain_name (str): O nome do domínio a ser verificado.

    Returns:
        tuple: Uma tupla contendo o nome do domínio, os dias restantes até a expiração e uma mensagem de erro (se houver).
    """
    try:
        domain = whois.whois(domain_name)
        expiration_date = domain.expiration_date

        if expiration_date is not None:
            if isinstance(expiration_date, list):
                expiration_date = expiration_date[0]
            days_left = (expiration_date - datetime.datetime.now()).days
            return (domain_name, days_left, None)
        else:
            return (domain_name, None, "Data de expiração não encontrada")
    except whois.parser.PywhoisError as e:
        return (domain_name, None, str(e))

def check_domains(domain_list):
    """
    Verifica a data de expiração de uma lista de domínios.

    Args:
        domain_list (list): Uma lista de nomes de domínio a serem verificados.

    Returns:
        list: Uma lista de tuplas contendo o nome do domínio, os dias restantes até a expiração e uma mensagem de erro (se houver).
    """
    results = [check_domain(domain) for domain in domain_list]
    return results

def main():
    domain_list = [
        "google.com",
        "amazon.com",
        "twitter.com",
        "facebook.com",
        "instagram.com" 
    ]

    domain_list_sorted = sorted(domain_list)
    results = check_domains(domain_list_sorted)
    
    for domain, days_left, error in results:
        if days_left is not None:
            if days_left == 30 or days_left == 20 or days_left <= 10:
                print(f"ALERTA: O domínio {domain} expira em {days_left} dia(s).")
        else:
            print(f"Não foi possível verificar o domínio {domain}: {error}")

if __name__ == "__main__":
    main()
