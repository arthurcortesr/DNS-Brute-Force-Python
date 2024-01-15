# DNS-Brute-Force-Python
O script ```dnsbrute.py``` é uma ferramenta desenvolvida em Python para realizar ataques de força bruta em subdomínios de um domínio-alvo usando consultas de DNS. Ele emprega threads para otimizar o processo, possibilitando a resolução de múltiplos subdomínios simultaneamente.

Este repositório também possui o arquivo [melhorias](https://github.com/arthurcortesr/DNS-Brute-Force-Python/blob/main/melhorias.md) que é usado para adicionar anotações de possíveis melhorias a serem implementadas no no script.

<br>

---

<br>

## **Modo de uso**

```bash
python3 dnsbrute.py <dominio> wordlist
```

## **Exemplo**

```bash
python3 dnsbrute.py businesscorp.com.br /usr/share/dirb/wordlists/small.txt
```

## **Exemplo de saída**

```bash
python3 dnsbrute.py example.com /path/to/wordlist.txt --threads 8 --timeout 2 --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
```

```bash
--------------------------------
| Pk's Academy - DNS BRUTE FORCE |
--------------------------------

subdomain1.example.com ---> 192.168.1.101
subdomain2.example.com ---> 192.168.1.102
subdomain3.example.com ---> 192.168.1.103
...
```

<br>

---

<br>


## **Funcionalidades**

1. Ataque de Força Bruta em Subdomínios: O script realiza um ataque de força bruta em subdomínios do domínio-alvo, utilizando uma lista de palavras fornecida.
2. -h, --help: Exibe a mensagem de ajuda.
3. --threads THREADS: Número de threads para consultas em paralelo (padrão: 10).
4. --timeout TIMEOUT: Tempo limite para cada consulta de DNS (padrão: 1 segundo).
5. --user-agent USER_AGENT: Cabeçalho de Agente do Usuário para as consultas de DNS.
6. A saída é colorida para facilitar a identificação de resultados bem-sucedidos (verde) e erros (vermelho).
7. Erros de resolução, como NXDOMAIN, são destacados em vermelho.
8. O script trata erros de resolução, como NXDOMAIN, e fornece informações detalhadas sobre esses erros.
9. Se nenhum argumento for fornecido, o script exibe uma mensagem personalizada com instruções de uso e um exemplo.

<br>

---

<br>

## **Avisos**

1. Possíveis Bloqueios de Consultas: Dependendo das políticas de segurança do servidor DNS do domínio-alvo, consultas excessivas podem levar a bloqueios temporários. Recomenda-se ajustar a configuração de threads e intervalos para evitar bloqueios indesejados.
2. Uso Responsável: O script é destinado a fins educacionais e deve ser usado com responsabilidade e em conformidade com as leis e regulamentações locais. O uso indevido pode resultar em consequências legais.
3. Cuidado ao Utilizar Listas de Palavras: Ao fornecer listas de palavras, certifique-se de ter permissão para realizar testes de segurança no domínio-alvo. O uso de listas não autorizadas pode violar políticas e leis de segurança cibernética.
4. Registro de Exceções: Em caso de erros ou exceções durante a execução do script, o usuário deve revisar as mensagens de erro para entender e corrigir possíveis problemas. O registro dessas exceções é fornecido para facilitar a depuração.
5. Opções de Linha de Comando: Ao utilizar opções de linha de comando, certifique-se de fornecer argumentos válidos para evitar erros na execução do script. O uso inadequado das opções pode levar a resultados inesperados.




























