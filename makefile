install:
	-mkdir "/var/log/bhunter"
	-mkdir "/etc/bhunter"
	-install ./src/bhunter /usr/bin/
	-install ./src/bhunter-ts /usr/bin/
	-install ./src/bhunter.service /etc/systemd/system/
	-install ./default/defLogins.txt /etc/bhunter/defLogins.txt
keygen:
	# -ssh-keygen -t rsa -f server.key
	-ssh-keygen -m PEM -f server.key
	-mv ./server.key.pub /etc/bhunter/server.pub
	-mv ./server.key /etc/bhunter/server.key
# debian:
# 	mkdir -p ./build_deb/usr/
# 	mkdir -p ./build_deb/var/log/bhunter/
# 	mkdir -p ./build_deb/DEBIAN
# 	cp ./for_debian/* ./build_deb/DEBIAN
#
# 	cp ./src/honeypot.py ./build_deb/usr/bin/
# 	cp ./src/contrSSH ./build_deb/usr/bin/
# 	cp ./src/hydracall.py ./build_deb/usr/bin/
# # 	mkdir /var/log/contrSSH/
# 	cp ./defLogins.txt /var/log/contrSSH/defLogins.txt
#
# 	fakeroot dpkg-deb --build ./build_deb
# 	rm -r ./build_deb
