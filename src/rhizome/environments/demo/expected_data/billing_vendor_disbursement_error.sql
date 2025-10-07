CREATE TABLE `vendor_disbursement_error` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_uuid` char(13) NOT NULL,
  `vendor_code` varchar(30) NOT NULL,
  `file_instance_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vde_charge_uuid` (`charge_uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3