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
  KEY `account_id` (`account_id`),
  KEY `internal_account_id` (`internal_account_id`),
  KEY `serial_number` (`serial_number`),
  KEY `timestamp_idx` (`timestamp`),
  CONSTRAINT `device_events_ibfk_1` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `device_events_ibfk_2` FOREIGN KEY (`internal_account_id`) REFERENCES `internal_account` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=27781 DEFAULT CHARSET=utf8mb3