CREATE TABLE `country` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `country_code` char(2) NOT NULL,
  `default_currency` char(3) NOT NULL,
  `default_locale_id` bigint unsigned NOT NULL,
  `default_timezone_id` bigint unsigned NOT NULL,
  `state_province_required` tinyint(1) DEFAULT '0',
  `zip_postal_required` tinyint(1) DEFAULT '0',
  `county_required` tinyint(1) DEFAULT '0',
  `app_market_billing_enabled` tinyint(1) DEFAULT '0',
  `vat` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `country_code` (`country_code`),
  KEY `default_locale_id` (`default_locale_id`),
  KEY `default_timezone_id` (`default_timezone_id`),
  CONSTRAINT `country_ibfk_1` FOREIGN KEY (`default_locale_id`) REFERENCES `locale` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `country_ibfk_2` FOREIGN KEY (`default_timezone_id`) REFERENCES `timezones` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3