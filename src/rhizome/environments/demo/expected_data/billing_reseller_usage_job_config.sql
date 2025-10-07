CREATE TABLE `reseller_usage_job_config` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `reseller_id` bigint unsigned NOT NULL,
  `report_type` enum('csv','excel') NOT NULL DEFAULT 'excel',
  PRIMARY KEY (`id`),
  UNIQUE KEY `reseller_id` (`reseller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3