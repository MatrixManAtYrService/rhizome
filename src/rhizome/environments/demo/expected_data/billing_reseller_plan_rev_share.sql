CREATE TABLE `reseller_plan_rev_share` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 DEFAULT NULL,
  `reseller_id` bigint unsigned NOT NULL,
  `plan_uuid` char(13) DEFAULT NULL,
  `rev_share` bigint NOT NULL,
  `rev_share_type` enum('PERCENT','FLAT_RATE') NOT NULL DEFAULT 'PERCENT',
  `effective_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reseller_plan` (`reseller_id`,`plan_uuid`,`effective_date`),
  KEY `reseller_id` (`reseller_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb3