CREATE TABLE `cellular_billing_arrears_info` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `request_uuid` varchar(30) NOT NULL,
  `merchant_uuid` varchar(13) DEFAULT NULL,
  `billing_date` date NOT NULL,
  `merchant_plan_uuid` varchar(13) DEFAULT NULL,
  `billing_event_uuid` varchar(26) DEFAULT NULL,
  `total_units` int DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_merchant_request_uuid` (`merchant_uuid`,`request_uuid`),
  KEY `cellular_billing_arrears_info` (`merchant_uuid`,`billing_date`)
) ENGINE=InnoDB AUTO_INCREMENT=455 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci