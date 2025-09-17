CREATE TABLE `consumer_failure` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `environment` varchar(25) NOT NULL,
  `reference_id` char(13) NOT NULL,
  `consumer_source` enum('MLC','AGREEMENT') NOT NULL,
  `payload` text NOT NULL,
  `channel` varchar(25) NOT NULL,
  `topic` varchar(127) NOT NULL,
  `cause` varchar(100) NOT NULL,
  `message` varchar(500) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `reference_id` (`reference_id`)
) ENGINE=InnoDB AUTO_INCREMENT=121179 DEFAULT CHARSET=utf8mb3