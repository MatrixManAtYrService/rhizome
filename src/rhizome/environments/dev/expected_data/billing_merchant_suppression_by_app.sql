CREATE TABLE `merchant_suppression_by_app` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `reference_id` bigint unsigned NOT NULL,
  `plan_billable` tinyint(1) DEFAULT '1',
  `app_billable` tinyint(1) DEFAULT '1',
  `plan_exportable` tinyint(1) DEFAULT '1',
  `app_exportable` tinyint(1) DEFAULT '1',
  `context` enum('OVERRIDE','NO_PLAN','NO_CLOVER_APPS','FIELD_TEST') DEFAULT NULL,
  `detail` varchar(511) CHARACTER SET latin1 DEFAULT NULL,
  `start_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `finalization_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `country` (`reference_id`,`context`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3