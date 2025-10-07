CREATE TABLE `vendor_disbursement_state_attempt` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_id` bigint unsigned NOT NULL,
  `state` enum('CREATED','ATTEMPT','REJECT','COMPLETE','VAT') DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `charge_id` (`charge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=322 DEFAULT CHARSET=utf8mb3