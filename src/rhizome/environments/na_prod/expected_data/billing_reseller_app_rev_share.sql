CREATE TABLE `reseller_app_rev_share` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 DEFAULT NULL,
  `reseller_id` bigint unsigned NOT NULL,
  `app_uuid` char(13) DEFAULT NULL,
  `app_type` enum('SECOND_PARTY','THIRD_PARTY') DEFAULT NULL,
  `rev_share` bigint NOT NULL,
  `rev_share_type` enum('TOP_LINE_PERCENT','BOTTOM_LINE_PERCENT','FLAT_RATE') NOT NULL DEFAULT 'BOTTOM_LINE_PERCENT',
  `effective_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reseller_app` (`reseller_id`,`app_uuid`,`app_type`,`effective_date`),
  KEY `reseller_id` (`reseller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=utf8mb3