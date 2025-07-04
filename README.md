# Network Scanner

Network Scanner — это простой инструмент для сканирования локальной сети и проверки доступности устройств. Программа пингует все устройства в сети и выводит их статус (доступен/недоступен) и имя хоста, если оно доступно.

## Описание

Этот проект сканирует все IP-адреса в заданной подсети и проверяет их доступность с помощью команды `ping`. Если устройство отвечает на пинг, программа пытается получить имя хоста через `socket.gethostbyaddr`. Результаты сохраняются в CSV-файл для дальнейшего анализа.
- Сканирует все устройства в сети (например, `192.168.3.0/24`).
- Проверяет доступность каждого устройства с помощью пинга.
- Получает имя хоста для доступных устройств.
- Сохраняет результаты сканирования в CSV-файл.

## Установка

1. Клонируйте репозиторий:
   git clone https://github.com/definitis/network-scanner.git

Перейдите в папку с проектом:
cd network-scanner

Установите необходимые зависимости:
pip install -r requirements.txt

Использование
Для того чтобы запустить сканирование сети, выполните следующую команду:
python main.py
Программа будет сканировать все IP-адреса в сети и выводить их статус в консоль. Результаты будут сохранены в CSV файл в той же папке, где находится скрипт, с именем, основанным на текущей дате и времени (например, network_scan_2025-06-25_14-30-00.csv).