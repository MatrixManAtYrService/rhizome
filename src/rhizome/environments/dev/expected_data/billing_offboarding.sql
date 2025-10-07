CREATE TABLE `offboarding` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `request_uuid` char(13) NOT NULL,
  `merchant_id` int unsigned NOT NULL,
  `step` enum('INITIATE','REMINDER','OFFBOARD','PROCESSING','PROCESSED','CANCELED','REOPENED','BLOCKED','IMMEDIATE') DEFAULT NULL,
  `dry_run` tinyint(1) DEFAULT '0',
  `due_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `merchant_id_idx` (`merchant_id`),
  KEY `request_uuid_idx` (`request_uuid`),
  KEY `step_idx` (`step`)
) ENGINE=InnoDB AUTO_INCREMENT=5685 DEFAULT CHARSET=utf8mb3