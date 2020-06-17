# bhunter
Инструмент для получения доступа к узлам бот-сетей
## Зависимости:
python3-paramiko <br/>
python3-libtmux <br/>
tmux <br/>
## Установка:
sudo make install <br/>
sudo make keygen <br/>
## Запуск:
Перед запуском необходимо убедиться, что 22/TCP порт свободен. Если он занят ssh-сервером, то перенесите ssh сервер на другой порт.
### просто командой:
sudo bhunter<br/>
### через tmux:
sudo bhunter-ts<br/>
sudo tmux attach -t bhunter<br/>
### as a service:
systemctl enable bhunter<br/>
systemctl start bhunter<br/>
