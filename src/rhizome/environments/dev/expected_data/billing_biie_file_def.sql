CREATE TABLE `biie_file_def` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `file_type` varchar(50) NOT NULL,
  `file_format` enum('DELIMITED','FIXED') NOT NULL,
  `num_headers` smallint unsigned NOT NULL DEFAULT '0',
  `num_footers` smallint unsigned NOT NULL DEFAULT '0',
  `key1_field` smallint unsigned NOT NULL DEFAULT '0',
  `key2_field` smallint unsigned NOT NULL DEFAULT '0',
  `error_threshold_method` enum('NONE','PERCENT','COUNT') NOT NULL DEFAULT 'NONE',
  `error_threshold` smallint unsigned NOT NULL DEFAULT '0',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_type` (`file_type`),
  UNIQUE KEY `biie_fd_uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb3