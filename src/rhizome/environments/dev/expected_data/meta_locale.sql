CREATE TABLE `locale` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `language` char(2) NOT NULL,
  `country` char(2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `language` (`language`,`country`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3