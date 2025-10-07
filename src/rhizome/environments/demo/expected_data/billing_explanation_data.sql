CREATE TABLE `explanation_data` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `explanation_uuid` char(13) NOT NULL,
  `index` smallint NOT NULL,
  `json_class` varchar(255) CHARACTER SET latin1 NOT NULL,
  `json_data` varchar(2047) CHARACTER SET latin1 NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `explanation_uuid` (`explanation_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=84619 DEFAULT CHARSET=utf8mb3