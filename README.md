# Bot do Telegram para Contagem de Dados

Este é um bot do Telegram desenvolvido em Python usando a biblioteca python-telegram-bot. O bot permite que os usuários adicionem contagens de dados relacionados a diferentes modalidades em bairros específicos de Aracaju. Além disso, também é possível solicitar relatórios com base nas contagens realizadas.

## Funcionalidades

- Apresentação inicial do bot com opções de adicionar ou solicitar dados.
- Opção de adicionar contagens por bairro e modalidade.
- Opção de solicitar relatórios com base nas contagens realizadas.
- Relatório exibindo as contagens de todas as modalidades por bairro.

## Pré-requisitos

- Python 3.6 ou superior
- Biblioteca python-telegram-bot

## Instalação

1. Clone o repositório ou faça o download do código-fonte.

    git clone https://github.com/seu-usuario/nome-do-repositorio.git


2. Instale as dependências utilizando o pip:

    pip install python-telegram-bot

## Utilização

1. Crie um novo bot no BotFather e obtenha o token do bot.

2. Substitua `'TOKEN'` pelo token do seu bot no código-fonte (`main()` função).

    updater = Updater('TOKEN')

3. Execute o programa Python.

    python bot.py

4. Inicie uma conversa com o bot no Telegram.

5. Utilize os comandos disponíveis para adicionar contagens, solicitar relatórios e interagir com o bot.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, melhorias ou correções de bugs, sinta-se à vontade para abrir uma issue ou enviar um pull request.
