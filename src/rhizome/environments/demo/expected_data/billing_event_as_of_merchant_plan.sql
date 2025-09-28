CREATE TABLE `as_of_merchant_plan` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `as_of_merchant_uuid` char(26) NOT NULL,
  `merchant_plan_uuid` char(13) NOT NULL,
  `trial_start_date` date DEFAULT NULL,
  `trial_days` smallint DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modifier` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `as_of_merchant_plan_key1` (`uuid`),
  UNIQUE KEY `as_of_merchant_plan_key2` (`as_of_merchant_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci