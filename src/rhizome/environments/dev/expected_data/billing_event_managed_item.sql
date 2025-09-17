CREATE TABLE `managed_item` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `criteria` enum('RESELLER','MERCHANT') NOT NULL,
  `item` varchar(255) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `begin_timestamp` datetime(6) DEFAULT NULL,
  `end_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `item` (`item`)
) ENGINE=InnoDB AUTO_INCREMENT=2865 DEFAULT CHARSET=utf8mb3