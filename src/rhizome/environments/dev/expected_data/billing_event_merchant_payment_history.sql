CREATE TABLE `merchant_payment_history` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `environment` char(25) NOT NULL,
  `billing_entity_uuid` char(26) NOT NULL,
  `payment_date` date NOT NULL,
  `currency` varchar(3) DEFAULT NULL,
  `total_amount` decimal(12,3) NOT NULL DEFAULT '0.000',
  `num_payments` int NOT NULL DEFAULT '0',
  `billing_event_uuid` varchar(26) NOT NULL,
  `request_uuid` varchar(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `merchant_payment_history_key1` (`uuid`),
  UNIQUE KEY `merchant_payment_history_key4` (`billing_event_uuid`,`payment_date`,`currency`),
  UNIQUE KEY `merchant_payment_history_key2` (`merchant_uuid`,`payment_date`,`currency`,`billing_event_uuid`,`environment`),
  UNIQUE KEY `merchant_payment_history_key3` (`billing_entity_uuid`,`payment_date`,`currency`,`billing_event_uuid`,`environment`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci