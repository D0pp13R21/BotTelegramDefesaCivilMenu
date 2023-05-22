import telegram
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

bairros = [
    "Centro", "Novo Paraíso", "Ponto Novo", "Getúlio Vargas", "América", "Luzia", "Cirurgia", "Siqueira Campos",
    "Grageru", "Pereira Lobo", "Soledade", "Jardins", "Suíssa", "Lamarão", "Inácio Barbosa", "Salgado Filho",
    "Cidade Nova", "São Conrado", "13 de Julho", "Japãozinho", "Farolândia", "Dezoito do Forte", "Porto Dantas",
    "Coroa do Meio", "Palestina", "Bugio", "Aeroporto", "Santo Antônio", "Jardim Centenário", "Atalaia",
    "Industrial", "Olaria", "Santa Maria", "Santos Dumont", "Capucho", "Zona de Expansão", "José Conrado de Araújo",
    "Jabotiana", "São José"
]

ADD, REQUEST = range(2)
alagamento_counter = {}
risco_estrutural_counter = {}
risco_deslizamento_counter = {}
risco_queda_arvore_counter = {}


def start(update, context):
    keyboard = [[InlineKeyboardButton("Adicionar", callback_data='add'),
                 InlineKeyboardButton("Solicitar", callback_data='request')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Olá! Eu sou o seu bot. O que você deseja fazer?', reply_markup=reply_markup)
    return ADD


def button(update, context):
    query = update.callback_query
    if query.data == 'add':
        keyboard = []
        for bairro in bairros:
            keyboard.append([InlineKeyboardButton(bairro, callback_data=bairro)])
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text('Selecione um bairro:', reply_markup=reply_markup)
        return REQUEST
    elif query.data == 'request':
        keyboard = [[InlineKeyboardButton("Últimos 3 meses", callback_data='3_months'),
                     InlineKeyboardButton("Último mês", callback_data='1_month')],
                    [InlineKeyboardButton("Última semana", callback_data='1_week'),
                     InlineKeyboardButton("Últimas 24h", callback_data='24_hours')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.message.reply_text('Selecione o período:', reply_markup=reply_markup)
        return REQUEST


def select_bairro(update, context):
    query = update.callback_query
    bairro = query.data
    keyboard = [
        [InlineKeyboardButton("Alagamento", callback_data='alagamento'),
         InlineKeyboardButton("Risco Estrutural", callback_data='risco_estrutural')],
        [InlineKeyboardButton("Risco de Deslizamento", callback_data='risco_deslizamento'),
         InlineKeyboardButton("Risco de Queda de Árvore", callback_data='risco_queda_arvore')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.message.reply_text(f'Você selecionou o bairro {bairro}. Selecione uma modalidade:', reply_markup=reply_markup)
    return REQUEST


def count_modalidade(update, context):
    query = update.callback_query
    bairro = query.message.text.split(' ')[-1]
    modalidade = query.data
    if modalidade == 'alagamento':
        alagamento_counter[bairro] = alagamento_counter.get(bairro, 0) + 1
    elif modalidade == 'risco_estrutural':
        risco_estrutural_counter[bairro] = risco_estrutural_counter.get(bairro, 0) + 1
    elif modalidade == 'risco_deslizamento':
        risco_deslizamento_counter[bairro] = risco_deslizamento_counter.get(bairro, 0) + 1
    elif modalidade == 'risco_queda_arvore':
        risco_queda_arvore_counter[bairro] = risco_queda_arvore_counter.get(bairro, 0) + 1
    query.message.reply_text('Contabilizado com sucesso!')
    return ConversationHandler.END


def relatorio(update, context):
    message = 'Relatório de contagens:\n\n'
    for bairro in bairros:
        message += f'Bairro: {bairro}\n'
        message += f'Alagamento: {alagamento_counter.get(bairro, 0)}\n'
        message += f'Risco Estrutural: {risco_estrutural_counter.get(bairro, 0)}\n'
        message += f'Risco de Deslizamento: {risco_deslizamento_counter.get(bairro, 0)}\n'
        message += f'Risco de Queda de Árvore: {risco_queda_arvore_counter.get(bairro, 0)}\n\n'
    update.message.reply_text(message)


def main():
    updater = Updater('TOKEN')  # Substitua 'TOKEN' pelo token do seu bot

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start), CallbackQueryHandler(button)],
        states={
            ADD: [CallbackQueryHandler(select_bairro)],
            REQUEST: [CallbackQueryHandler(count_modalidade)]
        },
        fallbacks=[CommandHandler('relatorio', relatorio)]
    )

    updater.dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
