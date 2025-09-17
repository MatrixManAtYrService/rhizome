CREATE TABLE `as_of_merchant_device` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `as_of_merchant_uuid` char(26) NOT NULL,
  `serial_number` varchar(32) NOT NULL,
  `device_type` varchar(25) DEFAULT NULL,
  `bundle_indicator` varchar(32) DEFAULT NULL,
  `modifier_1` varchar(25) DEFAULT NULL,
  `modifier_2` varchar(25) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `as_of_merchant_device_key1` (`uuid`),
  UNIQUE KEY `as_of_merchant_device_key3` (`serial_number`,`id` DESC),
  UNIQUE KEY `as_of_merchant_device_key2` (`as_of_merchant_uuid`,`device_type`,`serial_number`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci