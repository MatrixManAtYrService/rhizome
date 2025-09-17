CREATE TABLE `app_subscription_current` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `developer_app_uuid` char(13) NOT NULL,
  `environment` varchar(25) NOT NULL,
  `app_subscription_uuid` char(13) NOT NULL,
  `app_subscription_cost` decimal(12,3) NOT NULL,
  `bundled_with_plan` tinyint(1) NOT NULL DEFAULT '0',
  `trial_end_date` date DEFAULT NULL,
  `last_advance_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_subscription_current_key1` (`uuid`),
  UNIQUE KEY `app_subscription_current_key2` (`merchant_uuid`,`developer_app_uuid`,`environment`)
) ENGINE=InnoDB AUTO_INCREMENT=613 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci