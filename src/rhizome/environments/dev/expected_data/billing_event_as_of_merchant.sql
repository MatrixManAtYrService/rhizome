CREATE TABLE `as_of_merchant` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `as_of_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `event_datetime` datetime DEFAULT NULL,
  `billing_event_uuid` varchar(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `request_uuid` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `as_of_merchant_key1` (`uuid`),
  UNIQUE KEY `as_of_merchant_key2` (`merchant_uuid`,`as_of_timestamp` DESC),
  UNIQUE KEY `as_of_merchant_key3` (`as_of_timestamp` DESC,`id` DESC)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci