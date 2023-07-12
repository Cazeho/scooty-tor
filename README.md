# scooty-tor

```
apt install tor privoxy -y

nano /etc/privoxy/config

--> forward-socks5t   / 127.0.0.1:9050 . 

systemctl restart privoxy

curl --proxy 127.0.0.1:8118 https://check.torproject.org | grep "Congratulations"



tor --hash-password "pass"




```
