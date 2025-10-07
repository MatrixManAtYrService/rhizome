CREATE TABLE `corollary_data` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `request_uuid` char(13) NOT NULL,
  `calling_class` varchar(127) CHARACTER SET latin1 NOT NULL,
  `path` varchar(511) CHARACTER SET latin1 NOT NULL,
  `output` varchar(4095) CHARACTER SET latin1 DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `request_uuid` (`request_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=21538085 DEFAULT CHARSET=utf8mb3