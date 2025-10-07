CREATE TABLE `promo_control` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `code` varchar(32) NOT NULL,
  `reseller_id` bigint unsigned DEFAULT NULL,
  `agent` varchar(32) DEFAULT NULL,
  `bank` varchar(32) DEFAULT NULL,
  `business` varchar(32) DEFAULT NULL,
  `chain` varchar(32) DEFAULT NULL,
  `corp` varchar(7) DEFAULT NULL,
  `marker` varchar(10) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3