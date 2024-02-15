from pyrogram import Client
from apps.basics import welcome
from moduls.utils.utils import get_postdata, send_postdata

@Client.on_callback_query()
async def controler(cliente, data_response):
    data = data_response.data
    function_name, postdata = data.split("-")[0], data.split("-")[1]

    if function_name == "start":
        send_postdata(function_name, postdata)
        await welcome.start(cliente, data_response.message)

#    if data_response.message.from_user.id == data_response.from_user.id: