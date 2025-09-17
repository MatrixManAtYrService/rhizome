CREATE TABLE `app_subscription_daily` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `developer_app_uuid` char(13) NOT NULL,
  `environment` varchar(25) NOT NULL,
  `event_date` date NOT NULL,
  `starting_app_subscription_uuid` char(13) DEFAULT NULL,
  `ending_app_subscription_uuid` char(13) DEFAULT NULL,
  `highest_app_subscription_uuid` char(13) NOT NULL,
  `billing_event_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_subscription_daily_key1` (`uuid`),
  UNIQUE KEY `app_subscription_daily_key2` (`merchant_uuid`,`developer_app_uuid`,`environment`,`event_date`)
) ENGINE=InnoDB AUTO_INCREMENT=895 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci