import socket
import concurrent.futures
import argparse
import os
import sys

# Definindo códigos de cor ANSI
COR_PKAS = '\033[38;5;220m'  # FEB63E
COR_DNS = '\033[38;5;197m'  # F5055C
COR_ERRO = '\033[38;5;196m'  # E10406
COR_VERDE = '\033[92m'  # 00FF00
RESET = '\033[0m'  # Reset para as configurações padrão de cor

print(f'\n')
print(f'--------------------------------')
print(f'| {COR_PKAS}Pk\'s Academy{RESET} - {COR_DNS}DNS BRUTE FORCE{RESET} |')
print(f'--------------------------------')
print(f'\n')
print(f'Fazendo Brute Force')
print(f'\n')

def resolve_subdomain(subdomain, domain, user_agent=None):
    try:
        # Configuração do cabeçalho de agente do usuário, se fornecido
        headers = {'User-Agent': user_agent} if user_agent else {}
        ip_address = socket.gethostbyname(f'{subdomain}.{domain}')
        print(f'{COR_VERDE}{subdomain}.{domain} ---> {ip_address}{RESET}')
    except socket.gaierror:
        # Não faz nada se ocorrer uma exceção de resolução (NXDOMAIN)
        pass

def dns_brute_force(domain, wordlist, num_threads=10, timeout=1, user_agent=None):
    # Verifica a existência do arquivo de lista de palavras
    if not os.path.isfile(wordlist):
        print(f'{COR_ERRO}Erro: O arquivo de lista de palavras "{wordlist}" não foi encontrado.{RESET}')
        return

    # Lê as palavras do arquivo
    with open(wordlist, 'r') as file:
        words = file.read().splitlines()

    # Cria um pool de threads para consultas em paralelo
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        # Mapeia as funções para as palavras na lista
        futures = [executor.submit(resolve_subdomain, word, domain, user_agent) for word in words]

        # Aguarda a conclusão de todas as consultas
        concurrent.futures.wait(futures, timeout=timeout)

if __name__ == "__main__":
    # Verifica se há argumentos fornecidos
    if len(sys.argv) == 1:
        # Exibe a mensagem de ajuda personalizada
        print(f"""
------------------------------------------------------------------------------------------------------
{COR_PKAS}Pk's Academy{RESET} - {COR_DNS}DNS BRUTE FORCE{RESET}
------------------------------------------------------------------------------------------------------
Modo de uso: python3 dnsbrute.py <dominio> wordlist
------------------------------------------------------------------------------------------------------
Exemplo: python3 dnsbrute.py businesscorp.com.br /usr/share/dirb/wordlists/small.txt
------------------------------------------------------------------------------------------------------
Para mais informações, use a flag -h
------------------------------------------------------------------------------------------------------
""")
    elif '-h' in sys.argv or '--help' in sys.argv:
        # Exibe a mensagem de ajuda personalizada
        print(f"""
------------------------------------------------------------------------------------------------------
{COR_PKAS}Pk's Academy{RESET} - {COR_DNS}DNS BRUTE FORCE{RESET}
------------------------------------------------------------------------------------------------------
Modo de uso: python3 dnsbrute.py <dominio> wordlist
------------------------------------------------------------------------------------------------------
Exemplo: python3 dnsbrute.py businesscorp.com.br /usr/share/dirb/wordlists/small.txt
------------------------------------------------------------------------------------------------------
Options:
  -h, --help            Ajuda
  --threads THREADS     Número de threads para consultas em paralelo
  --timeout TIMEOUT     Tempo limite para cada consulta de DNS
  --user-agent USER_AGENT     Cabeçalho de Agente do Usuário para as consultas de DNS

------------------------------------------------------------------------------------------------------
""")
    else:
        # Configuração do argumento de linha de comando
        parser = argparse.ArgumentParser(description=f'{COR_PKAS}Pk\'s Academy{RESET} - {COR_DNS}DNS BRUTE FORCE{RESET}')
        parser.add_argument('domain', help='Domínio alvo')
        parser.add_argument('wordlist', help='Caminho do arquivo de lista de palavras')
        parser.add_argument('--threads', type=int, default=10, help='Número de threads para consultas em paralelo')
        parser.add_argument('--timeout', type=int, default=1, help='Tempo limite para cada consulta de DNS')
        parser.add_argument('--user-agent', help='Cabeçalho de Agente do Usuário para as consultas de DNS')

        args = parser.parse_args()

        # Executa o script com as configurações fornecidas
        dns_brute_force(args.domain, args.wordlist, args.threads, args.timeout, args.user_agent)
