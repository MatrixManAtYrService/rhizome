CREATE TABLE `mlc_captured_event` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `environment` char(25) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `reseller_uuid` char(13) NOT NULL,
  `event_timestamp` datetime(6) NOT NULL,
  `mlc_event_uuid` char(13) NOT NULL,
  `event_json` text NOT NULL,
  `event_context_json` text NOT NULL,
  `processed_timestamp` datetime(6) DEFAULT NULL,
  `processed_billing_event_uuid` char(26) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `mlc_captured_event_key1` (`uuid`),
  KEY `mlc_captured_event_index1` (`merchant_uuid`),
  KEY `mlc_captured_event_index2` (`reseller_uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci