watch -n1 rsync  . -av pi@192.168.1.200:/home/pi/django/curie/ --exclude env --exclude db.sqlite3
