CREATE TABLE `merchant_terms_acceptance_events` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `merchant_id` bigint unsigned NOT NULL,
  `acceptance_id` varchar(100) NOT NULL,
  `agreement_type` varchar(128) DEFAULT NULL,
  `account_id` char(13) NOT NULL,
  `acceptance_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `acceptance_modified` timestamp NULL DEFAULT NULL,
  `acceptance_deleted` timestamp NULL DEFAULT NULL,
  `action` varchar(100) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mta_uuid` (`uuid`),
  UNIQUE KEY `mta_merchantid` (`merchant_id`,`acceptance_created`,`acceptance_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3