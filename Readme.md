### Здесь преставлены питон скрипты для распознавания речи

1. audio_devices_list.py - выводит список доступных в системе аудиоустройств. С помошью его вывода можно узнать device_index микрофона.
2. pyaudio_rec_from_mic.py - записывает звука с микрофона и сохраненяет в файл output.wav. Так можно оценить качество звука, который пишется на ваш микрофон.
3. google_recognition.py - распознавание речи с использованием библиотеки speech_recognition. Для этого используется сервис Google Speech Recognition. То есть нужен доступ в интернет.
4. vosk_recognition.py - распознавание речи с использованием библиотеки Vosk. Распознавание происходит локально на вашем устройстве.

### Требования

В файле requirements.txt указаны требования сразу для всех скриптов
