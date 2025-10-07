CREATE TABLE `merchant_terms_missing_acceptance` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `merchant_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) DEFAULT NULL,
  `plan_charge_type` enum('ADJUSTMENT','ADVANCE') DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `mtma_uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=347362055 DEFAULT CHARSET=utf8mb3