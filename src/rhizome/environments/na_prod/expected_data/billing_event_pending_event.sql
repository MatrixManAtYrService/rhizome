CREATE TABLE `pending_event` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `environment` varchar(25) NOT NULL,
  `reference_id` char(13) NOT NULL,
  `consumer_source` enum('MLC','AGREEMENT') NOT NULL,
  `payload` text NOT NULL,
  `channel` varchar(25) NOT NULL,
  `topic` varchar(127) NOT NULL,
  `processor_uuid` varchar(26) DEFAULT NULL,
  `processing_start_timestamp` datetime(6) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `pending_event_key1` (`reference_id`,`processor_uuid`,`id`),
  KEY `pending_event_key2` (`processing_start_timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=1050555 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci