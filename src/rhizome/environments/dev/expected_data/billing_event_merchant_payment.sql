CREATE TABLE `merchant_payment` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `environment` char(25) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `requested_thru_date` date NOT NULL,
  `request_uuid` varchar(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `merchant_payment_key1` (`uuid`),
  UNIQUE KEY `merchant_payment_key2` (`merchant_uuid`,`environment`),
  UNIQUE KEY `merchant_payment_key3` (`billing_entity_uuid`,`environment`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci