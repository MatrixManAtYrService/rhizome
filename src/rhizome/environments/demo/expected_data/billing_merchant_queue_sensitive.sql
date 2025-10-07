CREATE TABLE `merchant_queue_sensitive` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `mid` char(15) NOT NULL,
  `name` enum('TAX_ID','DDA') NOT NULL,
  `value` varchar(255) DEFAULT NULL,
  `value_guid` binary(16) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=218 DEFAULT CHARSET=utf8mb3