CREATE TABLE `deserializable_failure` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `topic` varchar(127) DEFAULT NULL,
  `channel` varchar(127) DEFAULT NULL,
  `environment` char(25) NOT NULL,
  `consumer_source` enum('MLC','AGREEMENT') NOT NULL,
  `b64` text NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `uuid` (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3