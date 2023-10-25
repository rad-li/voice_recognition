""" Выводит список доступных в системе аудиоустройств """

import sounddevice as sd


print(sd.query_devices())
