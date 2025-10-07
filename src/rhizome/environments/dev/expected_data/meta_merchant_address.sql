CREATE TABLE `merchant_address` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `address_1` varchar(255) DEFAULT NULL,
  `address_2` varchar(255) DEFAULT NULL,
  `address_3` varchar(255) DEFAULT NULL,
  `city` varchar(127) DEFAULT NULL,
  `state` varchar(127) DEFAULT NULL,
  `zip` varchar(127) DEFAULT NULL,
  `country` varchar(127) DEFAULT NULL,
  `phone_number` varchar(21) DEFAULT NULL,
  `latitude` bigint DEFAULT NULL,
  `longitude` bigint DEFAULT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `modified_time` (`modified_time`),
  KEY `country` (`country`)
) ENGINE=InnoDB AUTO_INCREMENT=2075581 DEFAULT CHARSET=utf8mb3