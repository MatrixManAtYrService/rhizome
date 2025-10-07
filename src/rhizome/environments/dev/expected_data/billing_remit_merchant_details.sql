CREATE TABLE `remit_merchant_details` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `remit_uuid` varchar(30) NOT NULL,
  `hierarchy_id` varchar(250) NOT NULL,
  `remit_type` varchar(30) DEFAULT NULL,
  `hierarchy_name` varchar(255) DEFAULT NULL,
  `status_owner` varchar(30) DEFAULT NULL,
  `entity_name` varchar(50) DEFAULT NULL,
  `relm_code` varchar(30) DEFAULT NULL,
  `deleted_time` date DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8mb3