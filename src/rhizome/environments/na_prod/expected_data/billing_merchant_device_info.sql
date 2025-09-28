CREATE TABLE `merchant_device_info` (
  `merchant_id` bigint unsigned NOT NULL,
  `device_id` bigint unsigned NOT NULL,
  `terminal_id` varchar(16) NOT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  UNIQUE KEY `merchant_id` (`merchant_id`,`device_id`,`terminal_id`),
  KEY `modified_idx` (`modified_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3