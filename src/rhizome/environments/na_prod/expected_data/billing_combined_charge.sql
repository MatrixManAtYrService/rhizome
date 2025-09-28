CREATE TABLE `combined_charge` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `combined_chrg_uuid` (`uuid`),
  UNIQUE KEY `combined_chrg_req_uuid` (`request_uuid`,`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70234578 DEFAULT CHARSET=utf8mb3