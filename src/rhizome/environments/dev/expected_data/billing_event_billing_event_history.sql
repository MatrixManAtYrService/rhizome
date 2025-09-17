CREATE TABLE `billing_event_history` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `environment` varchar(25) NOT NULL,
  `merchant_id` char(13) DEFAULT NULL,
  `input_event_uuid` varchar(26) DEFAULT NULL,
  `billing_event_uuid` char(26) DEFAULT NULL,
  `event_source` enum('MLC','PLAN_ADVANCE','CELLULAR_ARREARS','APP_SUB_DAILY','APP_METER_DAILY','APP_RATES','APP_SUB_ADVANCE','BACKBOOK_MERCHANT','BACKBOOK_MLC','BACKBOOK_APP','MISC_PAYMENT','PLAN_ARREARS','AGREEMENT') NOT NULL,
  `event_context_json` text,
  `input` text,
  `output` text,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `billing_event_history_index1` (`billing_event_uuid`),
  KEY `billing_event_history_index2` (`merchant_id`,`event_source`,`created_timestamp`),
  KEY `billing_event_history_index3` (`input_event_uuid`,`event_source`)
) ENGINE=InnoDB AUTO_INCREMENT=231243 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci