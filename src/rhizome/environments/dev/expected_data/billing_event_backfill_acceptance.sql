CREATE TABLE `backfill_acceptance` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `acceptance_id` char(36) NOT NULL,
  `merchant_id` char(13) NOT NULL,
  `account_id` char(13) NOT NULL,
  `type` enum('BILLING','CELLULAR_ARREARS','CELLULAR_ADVANCE') NOT NULL,
  `comment` varchar(500) NOT NULL,
  `serial_number` varchar(32) DEFAULT NULL,
  `iccid` varchar(22) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=505 DEFAULT CHARSET=utf8mb3