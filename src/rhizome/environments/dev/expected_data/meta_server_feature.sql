CREATE TABLE `server_feature` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `name` varchar(127) NOT NULL,
  `config` mediumtext,
  `enabled` tinyint(1) NOT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `idx_sf_name_id` (`name`,`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1707 DEFAULT CHARSET=latin1