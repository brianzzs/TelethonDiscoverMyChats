import json
from telethon import TelegramClient


def load_config(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

base_config = load_config("config.json")
api_id = base_config['api_id']
api_hash = base_config['api_hash']

client = TelegramClient('session', api_id, api_hash)

async def list_chats():
    async with client:
        async for dialog in client.iter_dialogs():
            print(f'Chat ID: {dialog.id}, Chat Name: {dialog.name}')

if __name__ == "__main__":
    import asyncio
    asyncio.run(list_chats())
    input("Press Enter to exit...")
