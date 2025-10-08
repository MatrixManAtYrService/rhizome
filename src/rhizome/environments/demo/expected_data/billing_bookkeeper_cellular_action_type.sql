CREATE TABLE `cellular_action_type` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `cellular_action_type` varchar(25) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `cellular_action_type_key1` (`uuid`),
  UNIQUE KEY `cellular_action_type_key2` (`cellular_action_type`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci