CREATE TABLE `combined_disbursement` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `vendor_code` varchar(30) DEFAULT NULL,
  `base_currency` char(3) DEFAULT NULL,
  `base_amount` bigint DEFAULT NULL,
  `state_date` date DEFAULT NULL,
  `pay_out_currency` char(3) DEFAULT NULL,
  `pay_out_amount` bigint DEFAULT NULL,
  `pay_out_exchange_rate` bigint DEFAULT NULL,
  `state` enum('CREATED','ATTEMPT','REJECT','COMPLETE') DEFAULT NULL,
  `reject_code` varchar(32) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `combined_disbur_uuid` (`uuid`),
  UNIQUE KEY `combined_disbur_req_uuid` (`request_uuid`,`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10587 DEFAULT CHARSET=utf8mb3