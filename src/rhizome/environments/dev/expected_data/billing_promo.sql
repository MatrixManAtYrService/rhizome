CREATE TABLE `promo` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `code` varchar(32) NOT NULL,
  `description` varchar(511) CHARACTER SET latin1 DEFAULT NULL,
  `plan_trial_days` smallint DEFAULT NULL,
  `plan_type` enum('PAYMENTS_PLUS','REGISTER_LITE','REGISTER','QSR','DINING','NO_HARDWARE','PAYMENTS','SERVICES','RETAIL') DEFAULT NULL,
  `app_trial_days` smallint DEFAULT NULL,
  `developer_app_id` bigint unsigned DEFAULT NULL,
  `activation_time` timestamp NULL DEFAULT NULL,
  `deactivation_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3