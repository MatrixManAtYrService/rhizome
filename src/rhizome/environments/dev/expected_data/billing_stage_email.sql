CREATE TABLE `stage_email` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `request_uuid` char(13) NOT NULL,
  `reference_type` enum('MERCHANT','DEVELOPER') DEFAULT 'MERCHANT',
  `reference_id` int unsigned DEFAULT NULL,
  `type` enum('MERCHANT_APP_PLAN_CHARGES','MERCHANT_ACH_REJECT_CHARGE','APP_BILL_INTERNAL','APP_BILL_EXCEPTION','INTERNAL','DEVELOPER_DIST','INFOLEASE','DEVELOPER_EXPORT','GOLEO','ODESSA') DEFAULT NULL,
  `to` varchar(127) NOT NULL,
  `from` varchar(127) DEFAULT NULL,
  `from_name` varchar(127) DEFAULT NULL,
  `replyTo` varchar(127) DEFAULT NULL,
  `bcc` varchar(127) DEFAULT NULL,
  `subject` varchar(511) NOT NULL,
  `body` varchar(8191) CHARACTER SET latin1 DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sent_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `request_uuid` (`request_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=1788 DEFAULT CHARSET=utf8mb3