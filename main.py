import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='TheBakerCat/2chan_ruGPT3_small')

set_seed(42)

vk_session = vk_api.VkApi(token="ТОКЕН")
longpoll = VkBotLongPoll(vk_session, '215377650')
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.obj.text:
        message = event.obj.text
        if message.startswith("schizo"):  
            banwords = ['.com', '.ru', '.net', '.org', '.info', '.biz', '.io', '.co', "https://", "http://", "@", "tg", "телега", "telega", "телеграм", "телеграмм", "telegram", "telegramm"] # банворды
            banword_matches = [b for b in banwords if(b in message)]
            if banword_matches:
                vk.messages.send(
                    peer_id=event.obj.peer_id,
                    message='аааа бля нельзя такие сообщения чел',
                    random_id=get_random_id()
                )
            vk.messages.send(
                peer_id=event.obj.peer_id,
                message=generator(event.obj.text[7:], max_length=30, num_return_sequences=1)[0]["generated_text"],
                random_id=get_random_id()
            )
