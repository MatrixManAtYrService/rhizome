CREATE TABLE `biie_file_instance` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `biie_file_def_id` bigint unsigned NOT NULL,
  `file_name` varchar(512) NOT NULL,
  `file_size` bigint unsigned NOT NULL DEFAULT '0',
  `net_file_size` bigint unsigned NOT NULL DEFAULT '0',
  `num_records` bigint unsigned NOT NULL DEFAULT '0',
  `net_num_records` bigint unsigned NOT NULL DEFAULT '0',
  `dry_run` tinyint(1) DEFAULT NULL,
  `file_status` enum('CREATED','ERROR','HOLD','IGNORED','PENDING','PROCESSED','PROCESSING','RECEIVED','THRESHOLD') NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_type_status` (`biie_file_def_id`,`file_status`,`created_time`,`id`)
) ENGINE=InnoDB AUTO_INCREMENT=580 DEFAULT CHARSET=utf8mb3