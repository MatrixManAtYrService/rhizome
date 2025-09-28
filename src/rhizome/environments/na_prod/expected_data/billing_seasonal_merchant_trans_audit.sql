CREATE TABLE `seasonal_merchant_trans_audit` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `merchant_id` bigint unsigned NOT NULL,
  `bill_cycle` date NOT NULL,
  `seasonal_event` enum('SWITCH_TO_SEASONAL','SWITCH_TO_NONSEASONAL','PAYMENT','SEASONAL_RE_BOARD') NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `merchant` (`merchant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=363986 DEFAULT CHARSET=utf8mb3