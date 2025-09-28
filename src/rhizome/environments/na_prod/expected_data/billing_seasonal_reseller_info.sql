CREATE TABLE `seasonal_reseller_info` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `reseller_uuid_parent` char(13) CHARACTER SET latin1 NOT NULL,
  `reseller_uuid_child` char(13) CHARACTER SET latin1 NOT NULL,
  `seasonal_automation_supported` tinyint(1) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `reseller` (`reseller_uuid_child`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3