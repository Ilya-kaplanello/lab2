import socket

#Примечание: данный скрипт является очень простым, поэтому не поддерживает работу в браузере
#Запуск серверного сокета: python Lab_sockets.py
#Запуск клиентского сокета:
#Linux/BSD: nc localhost 1035
#Скачиваем "WireShark" или другую сетевую утилиту
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
            if 'who' in request:
                response = 'Вариант №10, Контекстный поиск в файле(ах), Илья Каплан'.encode()
            elif 'find' in request:
                response = ''
                _, string, filename = request.split()
                with open(filename) as file:
                    for line in file.readlines():
                        if string.encode() in line.encode():
                            response += line
                response.encode()
            else:
                response = 'Неизвестная команда'.encode()
            client_socket.send(response)
        #################################
#################################
