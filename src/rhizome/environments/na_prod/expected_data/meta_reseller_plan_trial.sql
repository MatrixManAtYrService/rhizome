CREATE TABLE `reseller_plan_trial` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(13) NOT NULL,
  `reseller_id` bigint unsigned NOT NULL,
  `merchant_plan_id` bigint unsigned NOT NULL,
  `trial_days` smallint NOT NULL,
  `finalize_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=112 DEFAULT CHARSET=utf8mb3