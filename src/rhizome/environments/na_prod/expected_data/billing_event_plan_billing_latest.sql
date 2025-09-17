CREATE TABLE `plan_billing_latest` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_uuid` char(13) NOT NULL,
  `environment` varchar(25) NOT NULL,
  `last_billing_date` date NOT NULL,
  `last_billed_plan_uuid` char(13) NOT NULL,
  `last_plan_billing_method` varchar(20) NOT NULL,
  `billing_event_uuid` char(26) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `plan_billing_latest_key1` (`merchant_uuid`,`environment`)
) ENGINE=InnoDB AUTO_INCREMENT=1789 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci