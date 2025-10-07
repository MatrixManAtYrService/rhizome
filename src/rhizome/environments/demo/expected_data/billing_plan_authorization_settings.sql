CREATE TABLE `plan_authorization_settings` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_id` int unsigned DEFAULT NULL,
  `partner_control_id` int unsigned DEFAULT NULL,
  `reseller_id` bigint unsigned DEFAULT NULL,
  `country_code` char(2) NOT NULL,
  `plan_group_id` bigint DEFAULT NULL,
  `device_name` varchar(255) DEFAULT NULL,
  `rules` varchar(16383) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `merchant_id` (`merchant_id`),
  UNIQUE KEY `partner_control_id` (`partner_control_id`),
  UNIQUE KEY `unique_reseller_country` (`reseller_id`,`country_code`),
  KEY `merchant` (`merchant_id`),
  KEY `partner_control` (`partner_control_id`),
  KEY `reseller` (`reseller_id`),
  KEY `country` (`country_code`),
  KEY `plan_group_id` (`plan_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb3