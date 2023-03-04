from telethon.sync import TelegramClient
from telethon.tl.types import PeerChannel
from telethon import events
from config import tg_user, from_channel, to_channel, forum_topic
from loguru import logger

logger.remove()
logger.add("mirror.log", rotation="1 week", level="INFO",
           format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message: <8}</white>")

def telegram_client_authorise():
    client = TelegramClient(tg_user['name'], tg_user['api_id'], tg_user['api_hash']).start()
    client.connect()
    receiver = client.get_entity(PeerChannel(to_channel))
    return receiver, client

receiver, client = telegram_client_authorise()

@client.on(events.NewMessage(chats=list(from_channel.keys())))
async def handler(event):
    try:
        event.message.message += '\n\n' + from_channel[event.peer_id.channel_id]
        await client.send_message(receiver, event.message, reply_to=forum_topic)
        logger.info(f'''Mirrored  message: "{event.message}" to {to_channel}''')
    except KeyError:
        logger.warning(f'Channel ID {event.peer_id.channel_id} not found in from_channel')
    except Exception as e:
        print(e)
        logger.error(f"Error mirroring message: {e}")

client.run_until_disconnected()
