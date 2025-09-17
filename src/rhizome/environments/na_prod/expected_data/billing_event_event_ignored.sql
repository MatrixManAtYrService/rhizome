CREATE TABLE `event_ignored` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `reference_id` char(13) NOT NULL,
  `consumer_source` enum('MLC','AGREEMENT') NOT NULL,
  `payload` text NOT NULL,
  `channel` varchar(25) NOT NULL,
  `topic` varchar(127) NOT NULL,
  `ignore_reason` varchar(25) NOT NULL,
  `message` varchar(500) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `event_ignored_key1` (`uuid`),
  UNIQUE KEY `event_ignored_key2` (`reference_id`,`id` DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci