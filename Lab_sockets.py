import socket

#Примечание: данный скрипт является очень простым, поэтому не поддерживает работу в браузере
#Запуск серверного сокета: python Lab_sockets.py
#Запуск клиентского сокета:
#Linux/BSD/MacOS: nc localhost 1035
#Windows: Скачиваем "WireShark" или другую сетевую утилиту
#Команда "who" возвращает информацию о варианте и студенте и не принимает никаких параметров
#Команда "find" принимает два параметра: искомую часть строки и имя файла, в которм строка будет искаться


#init
#################################
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#################################

#server_socket
#################################
server_socket.bind(('localhost', 1035))
server_socket.listen()
#################################

#client_socket
#################################
while True:
    print('Waiting for connection')
    client_socket, addr = server_socket.accept() #Инициальзация клиентского сокета
    print('Connection form', addr)

    while True:
        print('Waiting for request')
        request = client_socket.recv(255) #Получаем запрос

        #Команды из терминала и отправка ответа пользователю
        #################################
        if not request:
            break
        else:
            if 'who'.encode() in request:
                response = 'Вариант №10, Контекстный поиск в файле(ах), Илья Каплан\n'.encode()
            elif 'find'.encode() in request:
                response = ''.encode()
                _, string, filename = request.split()
                with open(filename.decode('utf-8')) as file:
                    for line in file.readlines():
                        if string in line.encode():
                            response += f'{line}\n'.encode()
            else:
                response = 'Неизвестная команда\n'.encode()
            client_socket.send(response)
        #################################
#################################
