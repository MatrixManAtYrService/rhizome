CREATE TABLE `device_events` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `device_event` enum('REGISTERED','PROVISIONED','ACTIVATED','REACTIVATED','DEACTIVATED','DISASSOCIATED','POS_MODE','CFD_MODE') DEFAULT NULL,
  `serial_number` varchar(32) CHARACTER SET latin1 DEFAULT NULL,
  `device_type_id` smallint unsigned DEFAULT NULL,
  `merchant_id` int unsigned DEFAULT NULL,
  `account_id` int unsigned DEFAULT NULL,
  `internal_account_id` bigint unsigned DEFAULT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `merchant_id` (`merchant_id`),
  KEY `serial_number` (`serial_number`),
  KEY `timestamp_idx` (`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=45061474 DEFAULT CHARSET=utf8mb3