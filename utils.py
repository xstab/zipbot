from pony.orm import *
from pyrogram.types import Message
from os import listdir

# ========= DB build =========
db = Database()


class User(db.Entity):
    uid = PrimaryKey(int, auto=True)
    status = Required(int)  # status-user: "INSERT"/"NOT-INSERT"


db.bind(provider='sqlite', filename='zipbot.sqlite', create_db=True)
db.generate_mapping(create_tables=True)


# ========= helping func =========
def dir_work(uid: int) -> str:
    """ static-user folder """
    return f"static/{uid}/"


def zip_work(uid: int) -> str:
    """ zip-archive file """
    return f'static/{uid}.zip'


def list_dir(uid: int) -> list:
    """ items in static-user folder """
    return listdir(dir_work(uid))


def up_progress(current, total, msg: Message):
    """ edit status-msg with progress of the uploading """
    msg.edit(f"**Upload progress: {current * 100 / total:.1f}%**")


# ========= MSG class =========
class Msg:

    def start(msg: Message) -> str:
        """ return start-message text """
        txt = f"Hey {msg.from_user.mention}!\n" \
              "\nI can compress files in to an archive." \
              "\nJust send /zip, and follow the instructions."
        return txt

    zip = "Send the files you want to compress, and at the end send /stopzip after all the files have been downloaded."
    too_big = "הקובץ גדול מידי ):"
    too_much = "ניתן לדחוס עד 20 קבצים בלבד."
    send_zip = "use /zip command to compress the files"
    zipping = "start compressing {} files..."
    uploading = "uploading archive..."
    unknow_error = "An unknown error occurred"
    downloading = "downloading..."
    zero_files = "No files were sent"
