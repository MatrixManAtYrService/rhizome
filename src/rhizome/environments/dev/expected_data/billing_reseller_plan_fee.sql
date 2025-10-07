CREATE TABLE `reseller_plan_fee` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `reseller_id` bigint unsigned NOT NULL,
  `merchant_plan_id` bigint unsigned DEFAULT NULL,
  `merchant_plan_type` varchar(20) DEFAULT NULL,
  `merchant_plan_group_id` bigint unsigned DEFAULT NULL,
  `fee_type` enum('SETUP','MONTHLY') NOT NULL,
  `currency` char(3) NOT NULL,
  `amount` bigint NOT NULL,
  `amount_type` enum('FLAT_RATE') NOT NULL,
  `effective_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `rpf_uuid` (`uuid`),
  UNIQUE KEY `rpf_reseller` (`reseller_id`,`merchant_plan_id`,`merchant_plan_type`,`fee_type`,`effective_date`)
) ENGINE=InnoDB AUTO_INCREMENT=110 DEFAULT CHARSET=utf8mb3