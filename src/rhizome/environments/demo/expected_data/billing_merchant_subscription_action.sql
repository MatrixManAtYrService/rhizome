CREATE TABLE `merchant_subscription_action` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `request_uuid` char(13) NOT NULL,
  `merchant_id` int unsigned NOT NULL,
  `cause` enum('OFF_BOARDED','CASH_ONLY','SEASONAL','TRIAL','UNK') DEFAULT 'UNK',
  `context` enum('CANDIDATE','OB_INTENT_EMAIL','OB_REMINDER_EMAIL','OB_CANCEL_EMAIL','OB_FINAL_EMAIL','OB_REOPEN_EMAIL','OB_FINAL_CHARGE','UNINSTALLED_APP','UNINSTALLED_APPS','DEPROVISIONED','DEPROVISIONED_DEVICE','CANCEL_INTENT','PROCESSED','INVALIDATE_ACCEPTANCE') DEFAULT 'CANDIDATE',
  `detail` varchar(31) CHARACTER SET latin1 NOT NULL,
  `dry_run` tinyint(1) DEFAULT '0',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `request_merchant` (`request_uuid`,`merchant_id`),
  KEY `merchant_id_idx` (`merchant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1609 DEFAULT CHARSET=utf8mb3