CREATE TABLE `fee_exception` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `reference_id` bigint unsigned NOT NULL,
  `reference_type` enum('MERCHANT') NOT NULL,
  `fee_type` enum('SETUP','MONTHLY') NOT NULL,
  `context` enum('CHARITY','ENTERPRISE','GOVT','WAIVER') NOT NULL,
  `detail` varchar(511) NOT NULL,
  `start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `finalization_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fe_uuid` (`uuid`),
  KEY `fe_reference` (`reference_id`,`reference_type`,`fee_type`,`start_time`)
) ENGINE=InnoDB AUTO_INCREMENT=1768302 DEFAULT CHARSET=utf8mb3