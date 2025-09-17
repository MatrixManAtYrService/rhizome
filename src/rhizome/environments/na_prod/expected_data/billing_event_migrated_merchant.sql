CREATE TABLE `migrated_merchant` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `reseller_uuid` char(13) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `backbook_merchant` tinyint(1) NOT NULL,
  `added_to_ebb_group` tinyint(1) NOT NULL,
  `plan_trials_migrated` tinyint(1) NOT NULL,
  `apps_migrated` tinyint(1) NOT NULL,
  `app_sub_events_caught_up` tinyint(1) NOT NULL,
  `app_meter_events_caught_up` tinyint(1) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `migrated_merchant_key1` (`reseller_uuid`,`merchant_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=1774 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci