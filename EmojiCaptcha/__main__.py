#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
from typing import Dict
from PIL import Image
import uuid
import logging
from EmojiCaptcha.emojis_map import emojis_index


DATA_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'emojis')
try:
    os.mkdir("cache")
except OSError:
    pass

class Captcha:
    def __init__(self, file_name=None, background=None):
        """
        Optional **args

        file_name[str]: custom file name for generating.

        background[str]: background image file path for captcha.

        ---------------------------------------------------------

        Return type -----> dict
        """

        self.file_name = file_name if file_name else str(uuid.uuid4().hex)
        self.background = background if background else os.path.join(DATA_DIR, 'background.png')


    def generate(self) -> dict():
        "Main function to Generate Captcha"
        try:
            background = Image.open(self.background)
            paste_image_list = list()
            emoji_names = list()
            supported_emojis = ['🃏', '🎤', '🎥', '🎨', '🎩', '🎬', '🎭', '🎮', '🎯', '🎱', '🎲', '🎷', '🎸', '🎹', '🎾', '🏀', '🏆', '🏈', '🏉', '🏐', '🏓', '💠', '💡', '💣', '💨', '💸', '💻', '💾', '💿', '📈', '📉', '📊', '📌', '📍', '📎', '📏', '📐', '📞', '📟', '📠', '📡', '📢', '📣', '📦', '📹', '📺', '📻', '📼', '📽', '🖥', '🖨', '🖲', '🗂', '🗃', '🗄', '🗜', '🗝', '🗡', '🚧', '🚨', '🛒', '🛠', '🛢', '🧀', '🌭', '🌮', '🌯', '🌺', '🌻', '🌼', '🌽', '🌾', '🌿', '🍊', '🍋', '🍌', '🍍', '🍎', '🍏', '🍚', '🍛', '🍜', '🍝', '🍞', '🍟', '🍪', '🍫', '🍬', '🍭', '🍮', '🍯', '🍺', '🍻', '🍼', '🍽', '🍾', '🍿', '🎊', '🎋', '🎍', '🎏', '🎚', '🎛', '🎞', '🐌', '🐍', '🐎', '🐚', '🐛', '🐝', '🐞', '🐟', '🐬', '🐭', '🐮', '🐯', '🐻', '🐼', '🐿', '👛', '👜', '👝', '👞', '👟', '💊', '💋', '💍', '💎', '🔋', '🔌', '🔪', '🔫', '🔬', '🔭', '🔮', '🕯', '🖊', '🖋', '🖌', '🖍', '🥚', '🥛', '🥜', '🥝', '🥞', '🦊', '🦋', '🦌', '🦍', '🦎', '🦏', '🌀', '🌂', '🌑', '🌕', '🌡', '🌤', '⛅️', '🌦', '🌧', '🌨', '🌩', '🌰', '🌱', '🌲', '🌳', '🌴', '🌵', '🌶', '🌷', '🌸', '🌹', '🍀', '🍁', '🍂', '🍃', '🍄', '🍅', '🍆', '🍇', '🍈', '🍉', '🍐', '🍑', '🍒', '🍓', '🍔', '🍕', '🍖', '🍗', '🍘', '🍙', '🍠', '🍡', '🍢', '🍣', '🍤', '🍥', '🍦', '🍧', '🍨', '🍩', '🍰', '🍱', '🍲', '🍴', '🍵', '🍶', '🍷', '🍸', '🍹', '🎀', '🎁', '🎂', '🎃', '🎄', '🎈', '🎉', '🎒', '🎓', '🎙', '🐀', '🐁', '🐂', '🐃', '🐄', '🐅', '🐆', '🐇', '🐕', '🐉', '🐓', '🐖', '🐗', '🐘', '🐙', '🐠', '🐡', '🐢', '🐣', '🐤', '🐥', '🐦', '🐧', '🐨', '🐩', '🐰', '🐱', '🐴', '🐵', '🐶', '🐷', '🐸', '🐹', '👁\u200d🗨', '👑', '👒', '👠', '👡', '👢', '💄', '💈', '🔗', '🔥', '🔦', '🔧', '🔨', '🔩', '🔰', '🔱', '🕰', '🕶', '🕹', '🖇', '🚀', '🤖', '🥀', '🥁', '🥂', '🥃', '🥐', '🥑', '🥒', '🥓', '🥔', '🥕', '🥖', '🥗', '🥘', '🥙', '🦀', '🦁', '🦂', '🦃', '🦄', '🦅', '🦆', '🦇', '🦈', '🦉', '🦐', '🦑', '⭐️', '⏰', '⏲', '⚠️', '⚡️', '⚰️', '⚽️', '⚾️', '⛄️', '⛅️', '⛈', '⛏', '⛓', '⌚️', '☎️', '⚜️', '✏️', '⌨️', '☁️', '☃️', '☄️', '☕️', '☘️', '☠️', '♨️', '⚒', '⚔️', '⚙️', '✈️', '✉️', '✒️']
            r = random.random()
            random.shuffle(supported_emojis, lambda: r)
            r = random.random()
            random.shuffle(supported_emojis, lambda: r)

            for i in range(6):
                emoji_names.append(supported_emojis[i])
                paste_image_list.append((os.path.join(DATA_DIR, emojis_index.get(supported_emojis[i]) + ".png")))

            position = [(20, 20), (180, 20), (310, 20), (20, 160), (180, 160), (310, 160)]

            for i in range(len(paste_image_list)):
                img = Image.open(paste_image_list[i]).rotate(random.randint(0, 360), resample=Image.BICUBIC, expand=True)
                img.thumbnail((200, 200), Image.ANTIALIAS)
                background.paste(img, (position[i]), img)
                
            emoji_captcha_path = os.path.join("cache", f"{self.file_name}.png")
            background.save(emoji_captcha_path, "PNG", quality=100)
            return {"answer": emoji_names, "captcha": emoji_captcha_path, "is_error": False}
        except Exception as e:
            logging.exception(e)
            return {"is_error": True}

