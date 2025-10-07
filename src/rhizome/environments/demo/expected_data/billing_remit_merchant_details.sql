CREATE TABLE `remit_merchant_details` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `remit_uuid` varchar(30) NOT NULL,
  `hierarchy_id` varchar(250) NOT NULL,
  `remit_type` enum('AMAZON','BANA','CARDCONNECT','RSA') DEFAULT NULL,
  `hierarchy_name` enum('agent','bank','corp','business','customer','maps','associationNumber','chain','merchant') DEFAULT NULL,
  `deleted_time` date DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3