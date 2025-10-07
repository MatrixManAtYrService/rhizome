CREATE TABLE `producer_failure` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `environment` char(25) DEFAULT NULL,
  `reference_id` bigint unsigned DEFAULT NULL,
  `kafka_event_type` enum('AUDIT','INTERNAL_AUDIT') NOT NULL,
  `payload` text NOT NULL,
  `processed` tinyint(1) NOT NULL DEFAULT '0',
  `topic` varchar(25) NOT NULL,
  `offset` bigint unsigned DEFAULT NULL,
  `cause` varchar(100) DEFAULT NULL,
  `failure_message` varchar(500) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3