# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OYo0V2eNpx79YY4Y_dY-iQPpLxqcPJND

первая нейросеть по чтению тз
"""

import tensorflow as tf
from tensorflow.keras.layers import Input, Embedding, LSTM, Dense, Dropout, Flatten
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical

import numpy as np
import zipfile
# Размер словаря
vocab_size = 10000

# Максимальная длина текста
max_text_len = 50

# Размер изображения
image_size = (224, 224, 3)

# Размер скрытого слоя
latent_dim = 128

# Количество эпох
epochs = 100





# Токенизация текста
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=vocab_size)
tokenizer.fit_on_texts

# Преобразование текста в последовательности токенов
text_sequences = tokenizer.texts_to_sequences

# Входные данные
text_input = Input(shape=(max_text_len,))
image_input = Input(shape=image_size)

# Текстовое эмбеддинг
text_embedding = Embedding(vocab_size, latent_dim)(text_input)

# LSTM для обработки текста
lstm_output = LSTM(latent_dim)(text_embedding)

pip install gradio_client

"""загрузка файлов для нейросети по созданию 3д моделей"""

!git clone https://github.com/isl-org/ZoeDepth.git

!python sanity.py

pip install timm==0.6.7

cd ZoeDepth

"""написание нейросети"""

import torch
from zoedepth.utils.misc import get_image_from_url, colorize
from PIL import Image
import matplotlib.pyplot as plt


zoe = torch.hub.load(".", "ZoeD_N", source="local", pretrained=True)

pip install git+https://github.com/tatsy/torchmcubes.git

pip uninstall torchmcubes

# Commented out IPython magic to ensure Python compatibility.
# %cd /content
!git clone -b dev https://github.com/camenduru/TripoSR-hf
# %cd /content/TripoSR-hf

!pip install -q trimesh omegaconf einops rembg gradio
!pip install -q https://github.com/camenduru/wheels/releases/download/colab/torchmcubes-0.1.0-cp310-cp310-linux_x86_64.whl

# !apt -y install -qq aria2
# !aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/stabilityai/TripoSR/resolve/main/model.ckpt -d /content/model -o model.ckpt

# %cd /content/TripoSR-hf
!python app.py