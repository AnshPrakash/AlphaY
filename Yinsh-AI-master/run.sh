python2 server.py 10000 -n 5 -s 5 -NC 2 -TL 120 -LOG server.log &
python2 client.py 0.0.0.0 10000 third.py &
#python2 client.py 0.0.0.0 10000 third.py -mode GUI
python2 client.py 0.0.0.0 10000 training.py -mode GUI
