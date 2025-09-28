CREATE TABLE `flight_check` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `executor` varchar(255) CHARACTER SET latin1 NOT NULL,
  `enabled` tinyint(1) NOT NULL DEFAULT '0',
  `cycle_minutes` smallint NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `executor` (`executor`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8mb3