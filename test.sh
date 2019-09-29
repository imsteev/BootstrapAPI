#/bin/bash
/usr/local/bin/python3 bootstrap_api.py
/usr/local/bin/python3 app.py &
pid=$!
echo $pid
sleep 1
/usr/local/bin/python3 test_bootstrap_api.py
kill -9 $pid