/* For testing the django.contrib.sessions.backends.db based on MySQL */
GRANT USAGE ON *.* TO 'test'@'localhost' IDENTIFIED BY PASSWORD '*94BDCEBE19083CE2A1F959FD02F964C7AF4CFC29';
GRANT ALL PRIVILEGES ON `test`.* TO 'test'@'localhost';
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_test` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;