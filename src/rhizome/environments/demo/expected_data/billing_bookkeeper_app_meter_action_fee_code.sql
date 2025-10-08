CREATE TABLE `app_meter_action_fee_code` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `developer_app_uuid` char(13) NOT NULL,
  `app_metered_uuid` char(13) NOT NULL,
  `merchant_plan_uuid` varchar(13) DEFAULT NULL,
  `app_meter_action_type` varchar(25) NOT NULL,
  `effective_date` date NOT NULL,
  `fee_category` varchar(25) NOT NULL,
  `fee_code` varchar(25) NOT NULL,
  `deleted_date` date DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `audit_id` varchar(26) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_meter_action_fee_code_key1` (`uuid`),
  UNIQUE KEY `app_meter_action_fee_code_key2` (`developer_app_uuid`,`app_metered_uuid`,`merchant_plan_uuid`,`app_meter_action_type`,`effective_date`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci