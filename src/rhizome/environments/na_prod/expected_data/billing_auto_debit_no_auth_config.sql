CREATE TABLE `auto_debit_no_auth_config` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `description` char(200) NOT NULL,
  `hierarchy` char(255) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=utf8mb3