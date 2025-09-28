CREATE TABLE `flight_check_execution` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `executor_id` bigint NOT NULL,
  `status` enum('IN_PROGRESS','PASS','FAIL') NOT NULL,
  `output` mediumtext,
  `payload` text,
  `completed_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1686 DEFAULT CHARSET=utf8mb3