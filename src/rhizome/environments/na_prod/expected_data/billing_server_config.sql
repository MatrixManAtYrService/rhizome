CREATE TABLE `server_config` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `tag` varchar(127) NOT NULL,
  `config` varchar(2000) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `tag` (`tag`)
) ENGINE=InnoDB AUTO_INCREMENT=2586 DEFAULT CHARSET=utf8mb3