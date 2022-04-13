t3:
	cat setup_mysql_dev.sql | sudo mysql -h localhost -u root -p
	echo "SHOW DATABASES;" | mysql -u hbnb_dev -p | grep hbnb_dev_db
	echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | sudo mysql -u root -p

t4:
	cat setup_mysql_test.sql | sudo mysql -h localhost -u root -p
	echo "SHOW DATABASES;" | mysql -u hbnb_test -p | grep hbnb_test_db
	echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | sudo mysql -u root -p
