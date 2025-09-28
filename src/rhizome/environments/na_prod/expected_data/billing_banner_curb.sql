CREATE TABLE `banner_curb` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `banner_data_id` bigint unsigned NOT NULL,
  `merchant_uuid` varchar(30) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `banner_data_id` (`banner_data_id`,`merchant_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=14096 DEFAULT CHARSET=utf8mb3