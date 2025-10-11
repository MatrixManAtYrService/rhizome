CREATE TABLE `reseller_role` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `account_id` int unsigned NOT NULL,
  `reseller_id` bigint unsigned NOT NULL,
  `permissions_id` bigint unsigned NOT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_id` (`account_id`,`reseller_id`),
  KEY `reseller_id` (`reseller_id`),
  KEY `permissions_id` (`permissions_id`),
  CONSTRAINT `reseller_role_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `reseller_role_ibfk_2` FOREIGN KEY (`reseller_id`) REFERENCES `reseller` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `reseller_role_ibfk_3` FOREIGN KEY (`permissions_id`) REFERENCES `reseller_permissions` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=1339 DEFAULT CHARSET=utf8mb3