import os
import pygame
import logging
import tempfile
from time import sleep
from gtts import gTTS

logging.getLogger(__name__)


def play(text: str) -> None:
    """
    Sintetiza o texto em voz e o reproduz utilizando a biblioteca gtts.

    Args:
        text (str): O texto em inglês a ser sintetizado e reproduzido.
    """
    try:
        pygame.mixer.init()
    except pygame.error as e:
        logging.error(f'Erro ao inicializar o pygame.mixer: {e}')
        raise

    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
        filename = temp_file.name

    tts = gTTS(text=text, lang='en')
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        sleep(0.1)

    try:
        pygame.mixer.music.unload()
        os.remove(filename)
    except PermissionError as e:
        logging.error(f'Erro ao remover arquivo: {e}')
        pass
