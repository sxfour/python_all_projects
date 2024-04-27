from warnings import filterwarnings
from telegram.warnings import PTBUserWarning
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters
)

import logging

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

START_ROUTES, END_ROUTES = range(2)
ZERO, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE = range(10)

keyboards = [
    [
        InlineKeyboardButton("ПРИЕМ ДОКУМЕНТОВ", callback_data=str(ONE)),
        InlineKeyboardButton("ВСТУПИТЕЛЬНЫЕ, ЕГЭ", callback_data=str(TWO)),
    ], [
        InlineKeyboardButton("3", callback_data=str(THREE)),
        InlineKeyboardButton("4", callback_data=str(FOUR)),
    ], [
        InlineKeyboardButton("5", callback_data=str(FIVE)),
        InlineKeyboardButton("6", callback_data=str(SIX)),
    ], [
        InlineKeyboardButton("7", callback_data=str(SEVEN)),
        InlineKeyboardButton("8", callback_data=str(EIGHT)),
    ], [
        InlineKeyboardButton("9", callback_data=str(NINE))
    ]
]


async def error_msg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    logger.info("Message from %s not found on this server, please check commands!", user.full_name)
    await update.message.reply_text("Я вас не понял!\nНапишите: /start")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    reply_markup = InlineKeyboardMarkup(keyboards)
    await update.message.reply_text("Привет Абитуриент! \U0001F4A9", reply_markup=reply_markup)

    return START_ROUTES


async def one(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Перейдите по ссылке: https://telegra.ph/12-02-05-19", reply_markup=reply_markup
    )

    return START_ROUTES


async def two(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Second CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return START_ROUTES


async def three(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Three CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )

    return START_ROUTES


async def four(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Fourth CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return START_ROUTES


async def five(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Five CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )

    return START_ROUTES


async def six(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Six CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )

    return START_ROUTES


async def seven(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Seven CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )

    return START_ROUTES


async def eight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Eight CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )

    return START_ROUTES


async def nine(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    keyboard = [
        [
            InlineKeyboardButton("НАЗАД", callback_data=str(ZERO)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(
        text="Nine CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )

    return START_ROUTES


async def start_over(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    reply_markup = InlineKeyboardMarkup(keyboards)
    await query.edit_message_text(
        text="Привет Абитуриент! \U0001F4A9", reply_markup=reply_markup
    )

    return START_ROUTES


def main() -> None:
    application = Application.builder().token("You token").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            START_ROUTES: [
                CallbackQueryHandler(one, pattern="^" + str(ONE) + "$"),
                CallbackQueryHandler(two, pattern="^" + str(TWO) + "$"),
                CallbackQueryHandler(three, pattern="^" + str(THREE) + "$"),
                CallbackQueryHandler(four, pattern="^" + str(FOUR) + "$"),
                CallbackQueryHandler(five, pattern="^" + str(FIVE) + "$"),
                CallbackQueryHandler(six, pattern="^" + str(SIX) + "$"),
                CallbackQueryHandler(seven, pattern="^" + str(SEVEN) + "$"),
                CallbackQueryHandler(eight, pattern="^" + str(EIGHT) + "$"),
                CallbackQueryHandler(nine, pattern="^" + str(NINE) + "$"),
                CallbackQueryHandler(start_over, pattern="^" + str(ZERO) + "$"),
            ]
        },
        fallbacks=[CommandHandler("start", start)],
    )

    application.add_handler(conv_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, error_msg))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
