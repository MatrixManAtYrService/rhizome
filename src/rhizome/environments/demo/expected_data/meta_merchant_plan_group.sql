CREATE TABLE `merchant_plan_group` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `name` varchar(127) NOT NULL,
  `enforce_assignment` tinyint(1) DEFAULT '0',
  `linkable` tinyint(1) NOT NULL DEFAULT '0',
  `trial_days` smallint DEFAULT NULL,
  `deleted_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `merchant_plan_group_id_deleted_time_idx` (`id`,`deleted_time`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3