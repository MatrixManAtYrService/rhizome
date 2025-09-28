CREATE TABLE `stop_ach_history` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_odessa_mapping_id` bigint unsigned DEFAULT NULL,
  `old_stop_ach` tinyint(1) NOT NULL DEFAULT '0',
  `old_modified_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3