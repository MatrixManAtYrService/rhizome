CREATE TABLE `merchant_odessa_mapping` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mid` varchar(31) NOT NULL,
  `odessa_id` varchar(24) DEFAULT NULL,
  `stop_ach` tinyint(1) NOT NULL DEFAULT '0',
  `stop_ach_date` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mid_odessa_id` (`mid`,`odessa_id`),
  KEY `mid_idx` (`mid`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3