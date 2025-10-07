CREATE TABLE `banner_data` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `banner_uuid` varchar(30) NOT NULL,
  `banner_lookup_name` enum('COUNTRY','RESELLER','PLAN','MERCHANT','MERCHANT_GROUP') DEFAULT NULL,
  `banner_lookup_value` varchar(30) NOT NULL,
  `start_date` timestamp NULL DEFAULT NULL,
  `end_date` timestamp NULL DEFAULT NULL,
  `contentful_template_id` varchar(30) NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '0',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `owner` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `banner_lookup_value` (`banner_lookup_value`)
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8mb3