CREATE TABLE `vat_vendor_disbursement` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `combined_disbursement_id` bigint unsigned NOT NULL,
  `vat_base_currency` char(3) DEFAULT NULL,
  `vat_base_amount` bigint DEFAULT NULL,
  `state_date` date DEFAULT NULL,
  `vat_pay_out_currency` char(3) DEFAULT NULL,
  `vat_pay_out_amount` bigint DEFAULT NULL,
  `vat_pay_out_exchange_rate` varchar(10) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `combined_disbur_id` (`combined_disbursement_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3