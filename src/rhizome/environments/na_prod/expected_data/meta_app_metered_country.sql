CREATE TABLE `app_metered_country` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `amount` bigint unsigned NOT NULL,
  `country` char(2) NOT NULL,
  `action` varchar(40) NOT NULL,
  `app_metered_id` bigint unsigned NOT NULL,
  `active` tinyint(1) NOT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `app_metered_id` (`app_metered_id`),
  CONSTRAINT `app_metered_country_ibfk_1` FOREIGN KEY (`app_metered_id`) REFERENCES `app_metered` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2306 DEFAULT CHARSET=utf8mb3