CREATE TABLE `stage_app_metered_event` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `app_metered_event_id` bigint unsigned NOT NULL,
  `stage_charge_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `merchant_id` int unsigned NOT NULL,
  `promoted_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `request_uuid` (`request_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=662 DEFAULT CHARSET=utf8mb3