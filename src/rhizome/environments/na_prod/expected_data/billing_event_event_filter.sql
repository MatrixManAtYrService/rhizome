CREATE TABLE `event_filter` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `criteria` enum('RESELLER','MERCHANT','DEVELOPER_APP','APP','OFFBOARDING_RESELLER') NOT NULL,
  `action` enum('INCLUDE','EXCLUDE','CAPTURE') NOT NULL,
  `value` varchar(255) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `begin_timestamp` datetime(6) DEFAULT NULL,
  `end_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `merchant_id` (`value`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb3