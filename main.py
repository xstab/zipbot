import os
from pyrogram import Client
from os import mkdir

app_id = int(os.environ.get("6798455", 6798455))
app_key = os.environ.get('50e975d09902b74b371d0e8acef83f61')
token = os.environ.get('1800364091:AAHgoROxRe06PQ7lOekXisfyrlsf_ZiDgKc')

app = Client("zipBot", app_id, app_key, bot_token=token)


if __name__ == '__main__':

    try:
        mkdir("static")  # create static files folder
    except FileExistsError:
        pass

    app.run()
