# Automação CLARO NET

Este projeto automatiza o processo manual de integração das Notas Fiscais de Serviço (NFS) faturadas pela empresa para o cliente CLARO/NET no portal que o mesmo disponibiliza para esse fim. Essa automação é simplista, ela não tem interface, apenas mensagens de alerta para se comunicar com o operador, e faz a comunicação com o portal por meio da técnica de raspagem de tela.  

Em detalhes, essa automação tem como base a técnica de raspagem de tela. Por meio da biblioteca Selenium, que possibilita a execução da técnica em sites e interfaces web pois se comunica diretamente com o JavaScript da aplicação (linguagem utilizada na programação dessas interfaces), consegue-se fazer o mapeamento e a manipulação de todos os botões, inputs e campos de um formulário web, tornando possível assim o desenvolvimento de um algoritmo que emula as ações humanas para executar a tarefa.

O operador antes precisava separar a NFS e extrair dela o número do protocolo. Então ele inseria esse número de protocolo em um campo de pesquisa, o que traz à interface o processo correspondente aquele protocolo. Com o registro do processo visivel, um botão para anexar o documento (NFS) é disposto sobre ele, e, ao clicar, um modal com um pequeno formulário aparece, com campos para seleção de arquivo, um checkbox para seleção de tipo de documento (NFS ou NF), além de três campos básicos a serem preenchidos com o número da NFS, a série (sempre "2") e a data de emissão da NFS.

A automação segue esse mesmo roteiro de ação que o operador seguia.
