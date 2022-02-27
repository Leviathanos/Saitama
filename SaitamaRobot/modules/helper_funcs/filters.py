from SaitamaRobot import DEV_USERS, DRAGONS, DEMONS
from telegram import Message
from telegram.ext import BaseFilter


class CustomFilters(object):

    class Supporters(BaseFilter):

        def filter(self, message: Message):
            return bool(message.from_user and message.from_user.id in DEMONS)

    support_filter = Supporters()

    class Sudoers(BaseFilter):

        def filter(self, message: Message):
            return bool(message.from_user and message.from_user.id in DRAGONS)

    sudo_filter = Sudoers()

    class Developers(BaseFilter):

        def filter(self, message: Message):
            return bool(message.from_user and message.from_user.id in DEV_USERS)

    dev_filter = Developers()

    class MimeType(BaseFilter):

        def __init__(self, mimetype):
            self.mime_type = mimetype
            self.name = "CustomFilters.mime_type({})".format(self.mime_type)

        def filter(self, message: Message):
            return bool(message.document and
                        message.document.mime_type == self.mime_type)

    mime_type = MimeType

    class _HasText(BaseFilter):

        def filter(self, message: Message):
            return bool(message.text or message.sticker or message.photo or
                        message.document or message.video)

    has_text = HasText()
