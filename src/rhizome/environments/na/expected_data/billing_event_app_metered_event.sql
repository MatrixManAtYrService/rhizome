CREATE TABLE `app_metered_event` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `developer_app_uuid` char(13) NOT NULL,
  `environment` varchar(25) NOT NULL,
  `app_metered_uuid` char(13) NOT NULL,
  `count` smallint DEFAULT NULL,
  `basis_amount` decimal(12,3) DEFAULT NULL,
  `basis_currency` char(3) DEFAULT NULL,
  `action_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `credit_for_trial` tinyint(1) NOT NULL DEFAULT '0',
  `cos_event_uuid` varchar(26) DEFAULT NULL,
  `processed_timestamp` datetime(6) DEFAULT NULL,
  `billing_event_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_metered_event_key1` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=6834 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci