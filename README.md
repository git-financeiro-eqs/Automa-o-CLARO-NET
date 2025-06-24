# Automação CLARO NET

Este projeto automatiza o processo manual de integração das Notas Fiscais de Serviço (NFS) faturadas pela empresa para o cliente CLARO/NET no portal que o mesmo disponibiliza para esse fim. Essa automação é simplista, ela não tem interface, apenas mensagens de alerta para se comunicar com o operador, e faz a comunicação com o portal por meio da técnica de raspagem de tela.  

Em detalhes, essa automação tem como base a técnica de raspagem de tela. Por meio da biblioteca Selenium, que possibilita a execução da técnica em sites e interfaces web pois se comunica diretamente com o JavaScript da aplicação (linguagem utilizada na programação dessas interfaces), consegue-se fazer o mapeamento e a manipulação de todos os botões, inputs e campos de um formulário web, tornando possível assim o desenvolvimento de um algoritmo que emula as ações humanas para executar a tarefa.

O operador antes precisava separar a NFS e extrair dela o número do protocolo. Então ele inseria esse número de protocolo em um campo de pesquisa, o que traz à interface o processo correspondente aquele protocolo. Com o registro do processo visível, um botão para anexar o documento (NFS) é disposto sobre ele, e, ao clicar, um modal com um pequeno formulário aparece, com campos para seleção de arquivo, um checkbox para seleção de tipo de documento (NFS ou NF), além de três campos básicos a serem preenchidos com o número da NFS, a série (sempre "2") e a data de emissão da NFS.

A automação segue esse mesmo roteiro de ação que o operador seguia.
<br/>
<br/>
## Tecnologias Utilizadas

- Python e suas bibliotecas nativas;
- Selenium – Raspagem de tela para automação de interações no portal da Vale;
- Webdriver Manager – Gerenciamento automático do ChromeDriver para o Selenium;
- keyboard – Simulação de teclas e atalhos do teclado;
- Pyperclip – Manipulação da área de transferência (copiar e colar);
- PyPDF2 – Leitura e manipulação de arquivos PDF;
- Pygetwindow – Verificar abertura de uma janela do sistema operacional;


<br/>

## Instalação

1. Clone o repositório ou baixe o arquivo ZIP do programa:
```bash
   https://github.com/git-financeiro-eqs/Automacao_CLARO_NET.git
```
2. Instale as dependências:
```bash
    pip install -r requirements.txt
```
3. Execute o programa:
```bash
    python main.py
```
<br/>

## Como Usar<br/>

1. Na pasta onde está o programa será necessário criar um pasta com o nome "NFS". Se não criar a pasta e tentar executar a automação ela te alertará quanto a inexistência dessa pasta, então crie-a.  
2. Você deve salvar os arquivos NFS que serão enviados à plataforma nessa pasta. Se não salvar, a automação te alertará quanto a inexistência desses arquivos.  
3. Após as primeiras duas etapas estarem concluídas, execute a automação. Ela irá abrir o link da plataforma e inserir as credenciais, contudo, ela não lê o captcha, então é você quem insere o dado nesse campo e efetua o logon. Ela aguarda até que você finalize essa etapa.  
4. Após as etapas anteriores terem sido concluídas, a automação irá executar o processo para todas as NFS salvas na pasta. Ao concluir, ela emitirá um alerta de finalização e solicitando que você, operador, exclua as NFS salvas na pasta para dar lugar a outras NFS que virão no futuro. Isso é dessa forma devido a necessidade que os operadores do time de Faturamento tem de utilizar esses arquivos para outras demandas.  
  
