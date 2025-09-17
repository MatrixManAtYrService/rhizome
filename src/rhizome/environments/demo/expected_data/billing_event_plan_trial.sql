CREATE TABLE `plan_trial` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `environment` char(25) NOT NULL,
  `effective_datetime` datetime(6) NOT NULL,
  `merchant_plan_uuid` char(13) NOT NULL,
  `trial_start_date` date NOT NULL,
  `trial_days` smallint NOT NULL,
  `billing_event_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `plan_trial_key1` (`uuid`),
  KEY `plan_trial_index1` (`merchant_uuid`,`environment`,`effective_datetime`)
) ENGINE=InnoDB AUTO_INCREMENT=59 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci