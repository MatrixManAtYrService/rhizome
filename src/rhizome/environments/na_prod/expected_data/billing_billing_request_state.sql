CREATE TABLE `billing_request_state` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `query_uuid` char(13) DEFAULT NULL,
  `state` enum('PROMOTE','PROVE') NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `query_uuid` (`query_uuid`,`state`)
) ENGINE=InnoDB AUTO_INCREMENT=20436 DEFAULT CHARSET=utf8mb3