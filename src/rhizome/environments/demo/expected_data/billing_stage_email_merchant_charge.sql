CREATE TABLE `stage_email_merchant_charge` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `type` enum('CHARGES','ACH_REJECT','DEV_DISBMT','ACH_NO_AUTH','ACH_NSF','CREDIT_NOTE') DEFAULT 'CHARGES',
  `payment_type` varchar(10) DEFAULT NULL,
  `payload` text,
  `recipient_id` int unsigned DEFAULT NULL,
  `charge_id` bigint unsigned NOT NULL,
  `done_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `request_uuid` char(13) NOT NULL,
  `promoted_time` timestamp NULL DEFAULT NULL,
  `promoted_id` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `request_and_uuid` (`request_uuid`,`uuid`),
  KEY `charge_id` (`charge_id`),
  KEY `recipient_type_done_time` (`done_time`,`recipient_id`,`type`)
) ENGINE=InnoDB AUTO_INCREMENT=257 DEFAULT CHARSET=utf8mb3