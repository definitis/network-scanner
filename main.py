import ipaddress
import subprocess
import socket
import csv
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def savecsv(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"network_scan_{timestamp}.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['IP', 'Status', 'Hostname']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for result in results:
            writer.writerow(result)

network = ipaddress.ip_network("192.168.3.0/24", strict=False)

def ping(ip):
    response = subprocess.call(
        ["ping", "-n", "1", "-w", "100", str(ip)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return response == 0

def name(ip):
    try:
        hostname = socket.gethostbyaddr(str(ip))[0]
        return hostname
    except (socket.herror, socket.gaierror):
        return None

def scan(ip):
    if ping(ip):
        hostname = name(ip)
        print('\n'f'{ip} OK - {hostname if hostname else "Имя неизвестно"}')
        return {
            'IP': str(ip),
            'Status': 'OK',
            'Hostname': hostname if hostname else 'Имя неизвестно'
        }
    else:
        return {
            'IP': str(ip),
            'Status': 'NO',
            'Hostname': 'Не найдено'
        }

with ThreadPoolExecutor(max_workers=50) as executor:
    results = list(executor.map(scan, network.hosts()))

savecsv(results)