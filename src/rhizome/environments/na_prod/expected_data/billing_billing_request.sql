CREATE TABLE `billing_request` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `query_uuid` char(13) DEFAULT NULL,
  `name` varchar(127) CHARACTER SET latin1 NOT NULL,
  `status` enum('PENDING','SUCCEEDED','KILLED','FAILED','HAS_ERRORS','DELETED','UNAUTHORIZED','QUEUED') DEFAULT 'PENDING',
  `input_class` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `entry_point` varchar(255) CHARACTER SET latin1 NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `completed_time` timestamp NULL DEFAULT NULL,
  `server_id` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=80456 DEFAULT CHARSET=utf8mb3