""" Запись аудио с помощью микрофона и распознавание речи с использованием библиотеки Vosk """

# Импортируем необходимые модули
from vosk import Model, KaldiRecognizer
import pyaudio
import os
import json

# проверка наличия модели на нужном языке в каталоге приложения
if not os.path.exists("models/vosk-model-small-ru"):
    print("Загрузите модель с сайта:\n"
          "https://alphacephei.com/vosk/models и распакауйте в папку model")
    exit(1)

# Инициализируем модель для распознавания речи с помощью модели "vosk-model-small-ru"
model = Model("models/vosk-model-small-ru")

# Инициализируем объект KaldiRecognizer с использованием модели и частотой дискретизации аудио 44100 Гц
rec = KaldiRecognizer(model, 44100)

# Инициализируем объект PyAudio для работы с аудио
p = pyaudio.PyAudio()

# Открываем аудио поток для записи звука с параметрами:
# формат Int16 (16-битное целое число), 1 канал, частота дискретизации 44100 Гц,
# включен режим записи и указываем размер буфера в 8000 фреймов
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=44100,
    input=True,
    frames_per_buffer=8000
)

# Запускаем поток записи звука
stream.start_stream()

# Бесконечный цикл, в котором читаем аудио данные из потока записи звука с помощью stream.read(44100)
while True:
    data = stream.read(44100)

    # Затем передаем данные в rec.AcceptWaveform(data), чтобы распознать речь
    if rec.AcceptWaveform(data):

        # Если распознавание прошло успешно, получаем результат в формате JSON
        text = json.loads(rec.Result())["text"]

        # Преобразуем его с помощью json.loads() и извлекаем распознанную информацию из поля "text"
        if text != "":
            print(text)
