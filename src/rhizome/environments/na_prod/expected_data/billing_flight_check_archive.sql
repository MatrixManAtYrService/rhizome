CREATE TABLE `flight_check_archive` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `executor_id` bigint NOT NULL,
  `status` enum('PASS','FAIL') NOT NULL,
  `output` text,
  `payload` text,
  `completed_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3