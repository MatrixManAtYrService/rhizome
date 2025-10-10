CREATE TABLE `merchant_creation_details` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_id` int unsigned NOT NULL,
  `creation_source` enum('FDPOS','IPG','CC','GOR_INTERNAL','FDPOS_INTERNAL','IPG_INTERNAL','SELF_BOARDING','DASHBOARD','MERCHANT_CLAIM','DEVELOPER_CLAIM','FISERV_SBA','PARTNER_SBA','SBA_HIPAA_EXEMPT','OCEAN','IPP','SHELL','TMS','BOARDING_UI') NOT NULL,
  `source_identifier` varchar(255) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `pre_create` enum('SHELL') DEFAULT NULL,
  `pre_source` enum('SELF_BOARDING') DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `merchant_id` (`merchant_id`),
  KEY `source_identifier` (`source_identifier`),
  CONSTRAINT `merchant_creation_details_ibfk_1` FOREIGN KEY (`merchant_id`) REFERENCES `merchant` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=404737 DEFAULT CHARSET=utf8mb3