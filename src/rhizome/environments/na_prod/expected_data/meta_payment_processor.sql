CREATE TABLE `payment_processor` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `name` varchar(127) DEFAULT NULL,
  `payment_gateway_api` varchar(31) CHARACTER SET latin1 NOT NULL,
  `production` tinyint(1) NOT NULL,
  `config` text,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `modified_time` (`modified_time`)
) ENGINE=InnoDB AUTO_INCREMENT=807 DEFAULT CHARSET=utf8mb3