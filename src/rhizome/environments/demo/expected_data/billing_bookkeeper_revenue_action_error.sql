CREATE TABLE `revenue_action_error` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `revenue_action_uuid` char(26) NOT NULL,
  `request_uuid` char(26) NOT NULL,
  `posting_date` date NOT NULL,
  `original_request_uuid` char(26) NOT NULL,
  `original_posting_date` date NOT NULL,
  `posting_attempts` smallint DEFAULT '1',
  `error_code` varchar(25) NOT NULL,
  `error_details` text,
  `resolved` smallint DEFAULT '0',
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `revenue_action_error_key1` (`uuid`),
  UNIQUE KEY `revenue_action_error_key2` (`revenue_action_uuid`,`id`),
  UNIQUE KEY `revenue_action_error_key3` (`request_uuid`,`posting_date`,`revenue_action_uuid`,`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci