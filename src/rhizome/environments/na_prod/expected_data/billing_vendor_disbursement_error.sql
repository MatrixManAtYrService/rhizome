CREATE TABLE `vendor_disbursement_error` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_uuid` char(13) NOT NULL,
  `vendor_code` varchar(30) NOT NULL,
  `file_instance_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `state` enum('CREATED','ATTEMPT','REJECT','COMPLETE','VAT') DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vde_state_charge_uuid` (`state`,`charge_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=751720 DEFAULT CHARSET=utf8mb3