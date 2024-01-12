Aqui irei deixar anotações de possíveis melhorias para o script que serão analisadas antes de serem de fato feitas as atualizações no scripts. Também será escrito os códigos e/ou partes da melhoria.

<br>

---

<br>

## **Suporte a IPV6**

Atualmente, o script usa socket.gethostbyname para resolver os subdomínios. Considere adicionar suporte a IPv6 para garantir uma cobertura mais ampla

<br>

---

<br>

## **Opção de Saída para Arquivo**

Adicionar uma opção de linha de comando que permita ao usuário salvar os resultados em um arquivo em vez de apenas imprimir no console. Isso pode ser útil para análise posterior ou documentação.

<br>

---

<br>

## **Opção de Modo Silencioso**

Adicionar uma opção de linha de comando para desativar a saída padrão, tornando o script mais silencioso. Isso pode ser útil ao executar em segundo plano.

<br>

---

<br>

## **Exclusão de Subdomínios Repetidos**

Se a lista de palavras contiver duplicatas, considerar adicionar uma verificação para evitar consultas redundantes aos mesmos subdomínios.

<br>

---

<br>

## **Tratamento de Redirecionamentos**

Se o domínio-alvo usar redirecionamento para www, considerar adicionar uma opção para seguir automaticamente redirecionamentos.

<br>

---

<br>

## **Relatório de Estatísticas** 

No final da execução, pode adicionar um relatório estatístico, mostrando o número total de consultas bem-sucedidas, falhas, etc.

<br>

---

<br>























