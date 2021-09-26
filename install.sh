sudo apt install python3-pip -y
git clone https://github.com/xiaozhan-sb/MHDDoS&&cd MHDDoS
chmod 777 pre.sh
bash pre.sh
rm -rf start.build
rm -rf start.py
cd files/proxys
python3 -m nuitka --show-progress --show-memory socker.py
rm -rf socker.build
rm -rf socker.py
chmod 777 httptest
cd ../..
echo "put proxies in MHDDoS/files/proxys,named it as socks5.txt or http.txt"
echo "and enter MHDDos dir to start"
echo "note: use start.bin to start"
