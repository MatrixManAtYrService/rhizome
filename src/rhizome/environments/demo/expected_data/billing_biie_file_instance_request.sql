CREATE TABLE `biie_file_instance_request` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `biie_file_instance_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `process_name` varchar(127) NOT NULL DEFAULT 'Unknown',
  `num_attempted` bigint unsigned NOT NULL DEFAULT '0',
  `num_success` bigint unsigned NOT NULL DEFAULT '0',
  `num_errors` bigint unsigned NOT NULL DEFAULT '0',
  `num_warnings` bigint unsigned NOT NULL DEFAULT '0',
  `num_skipped` bigint unsigned NOT NULL DEFAULT '0',
  `reason_code` smallint unsigned DEFAULT NULL,
  `reason_detail` varchar(2000) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_instance_request` (`biie_file_instance_id`,`request_uuid`,`process_name`),
  UNIQUE KEY `request_file_instance` (`request_uuid`,`biie_file_instance_id`,`process_name`)
) ENGINE=InnoDB AUTO_INCREMENT=758 DEFAULT CHARSET=utf8mb3