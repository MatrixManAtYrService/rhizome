CREATE TABLE `server_feature` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `name` varchar(127) NOT NULL,
  `config` text,
  `enabled` tinyint(1) NOT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=1435 DEFAULT CHARSET=latin1