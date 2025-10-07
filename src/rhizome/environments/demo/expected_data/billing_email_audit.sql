CREATE TABLE `email_audit` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `email_type` varchar(127) CHARACTER SET latin1 NOT NULL,
  `recipient_id` int unsigned NOT NULL,
  `email_status` varchar(127) CHARACTER SET latin1 NOT NULL,
  `track_id` varchar(255) NOT NULL,
  `done_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  UNIQUE KEY `track_id` (`track_id`),
  KEY `email_type` (`email_type`),
  KEY `recipient_id` (`recipient_id`),
  KEY `created_time` (`created_time`)
) ENGINE=InnoDB AUTO_INCREMENT=1011 DEFAULT CHARSET=utf8mb3