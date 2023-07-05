Frontend на основе Flask для агрегатора новостей https://github.com/AlexanderVarlamov/fast_ap_lenta

В settings.ini настраиваются порты и ip для бэка и фронта.

Рекомендуется разворачивать в виртуальном окружении на Windows 10 и выше. Также необходимо иметь установленный Python версии 3.9 и выше c модулем virtualenv.

Алгоритм развёртывания:

- качаем с GitHub все файлы
- распаковываем архив и из папки проекта пишем:<i>
  - cmd(откроется консоль)
  - python -m venv venv
  - .\venv\Scripts\activate(для Windows, для Linux надо будет написать source ./venv/bin/activate)
  - pip install -r requirements.txt</i>

- далее из виртуального окружения запускаем
  - python main.py

//TODO  Поработать с CSS, реализовать динамическую подгрузку источников. Сейчас хардкодом забито 3 источника новостей. Надо реализовать дополнительное API на бэке, которое будет выдавать ключи, и сделать index.html динамическим