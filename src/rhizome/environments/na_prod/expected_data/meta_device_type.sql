CREATE TABLE `device_type` (
  `id` smallint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `name` varchar(255) NOT NULL,
  `models` varchar(255) DEFAULT NULL,
  `skus` varchar(255) DEFAULT NULL,
  `sdk_version` int unsigned DEFAULT NULL,
  `prioritized_kernel_types` varchar(255) DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `name` (`name`),
  KEY `modified_time` (`modified_time`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb3