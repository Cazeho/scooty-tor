# scooty-tor


## set up proxy

```
apt install tor privoxy -y

nano /etc/privoxy/config

--> forward-socks5t   / 127.0.0.1:9050 . 

systemctl restart privoxy

curl --proxy 127.0.0.1:8118 https://check.torproject.org | grep "Congratulations"



```



## set up your website on dark net

```
nano /etc/tor/torrc

-->

HiddenServiceDir /var/lib/tor/hidden_service/
HiddenServicePort 80 127.0.0.1:80


cat /var/lib/tor/hidden_service/hostname

```
