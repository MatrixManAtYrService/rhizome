CREATE TABLE `plan_meta_history` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `action` enum('INSERT','UPDATE','DELETE') NOT NULL,
  `plan_meta_id` bigint unsigned DEFAULT NULL,
  `ref_type` enum('COUNTRY','PROVINCE') DEFAULT NULL,
  `ref_id` varchar(64) DEFAULT NULL,
  `plan_type` enum('UNKNOWN','CLASSIC','PAYMENTS_PLUS','REGISTER_LITE','REGISTER','QSR','DINING','VT','NO_HARDWARE','PAYMENTS','SERVICES','RETAIL') DEFAULT NULL,
  `plan_uuid` char(13) DEFAULT NULL,
  `prop_name` varchar(255) NOT NULL,
  `prop_value` varchar(2048) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `plan_meta_id` (`plan_meta_id`),
  KEY `plan_type` (`plan_type`),
  KEY `plan_uuid` (`plan_uuid`),
  KEY `prop_name` (`prop_name`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=utf8mb3