# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 12:18:47 2023

@author: Pena + GPT-4

Cria uma versão com sample rate de 44100 Hz de cada arquivo de audio da pasta
"""

import os
from pydub import AudioSegment
from pydub.utils import mediainfo

def conform_audio_files(folder_path):
    # Caminho para a pasta onde os arquivos conformados serão salvos
    conformed_folder = os.path.join(folder_path, "conformed files")
    if not os.path.exists(conformed_folder):
        os.makedirs(conformed_folder)

    # Extensões de arquivo suportadas
    supported_extensions = ['aiff', 'm4a', 'flac', 'mp3', 'ogg', 'wav']

    for file in os.listdir(folder_path):
        if file.split('.')[-1].lower() in supported_extensions:
            file_path = os.path.join(folder_path, file)

            # Obtendo informações do arquivo de áudio
            info = mediainfo(file_path)
            sample_rate = int(info['sample_rate'])

            if sample_rate != 44100:
                # Conformar arquivo para 44100Hz
                audio = AudioSegment.from_file(file_path)
                conformed_audio = audio.set_frame_rate(44100)

                # Adicionando "_44100" ao nome do arquivo
                file_name, file_extension = os.path.splitext(file)
                ##conformed_file_name = f"{file_name}_44100"
                conformed_file_name = f"{file_name}"

                # Se o arquivo original for m4a, mudar o formato de saída para wav
                if file_extension.lower() == '.m4a':
                    conformed_file_name += '.wav'
                else:
                    conformed_file_name += file_extension

                conformed_file_path = os.path.join(conformed_folder, conformed_file_name)

                # Salvar arquivo conformado
                conformed_audio.export(conformed_file_path, format=conformed_file_name.split('.')[-1])

    return f"Arquivos conformados salvos em: {conformed_folder}"

folder_path = "D:/Code/AudioResampler/audioFiles/"
conform_audio_files(folder_path)
# Nota: Substitua "folder_path" pelo caminho da pasta com seus arquivos de áudio.
