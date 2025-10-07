CREATE TABLE `explanation` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `request_uuid` char(13) NOT NULL,
  `merchant_id` int unsigned NOT NULL,
  `explanation_uuid` char(13) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `e_idx1` (`explanation_uuid`),
  KEY `request_merchant` (`request_uuid`,`merchant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=121792259 DEFAULT CHARSET=utf8mb3