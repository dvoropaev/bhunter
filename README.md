# bhunter
## Зависимости:
python3-paramiko <br/>
python3-libtmux <br/>
tmux <br/>
## Установка:
sudo make install <br/>
sudo make keygen <br/>
## Запуск:
### просто командой:
sudo bhunter<br/>
### через tmux:
sudo bhunter-ts<br/>
sudo tmux attach -t bhunter<br/>
### as a service:
systemctl enable bhunter<br/>
systemctl start bhunter<br/>
