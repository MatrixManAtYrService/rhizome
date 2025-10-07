CREATE TABLE `disbursement_invoice_number` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `combined_disbursement_id` bigint unsigned NOT NULL,
  `invoice_number` varchar(30) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `combined_disbursement_id` (`combined_disbursement_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3