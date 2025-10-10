CREATE TABLE `app_metered` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `developer_app_id` bigint unsigned NOT NULL,
  `label` varchar(20) NOT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `developer_app_id` (`developer_app_id`),
  CONSTRAINT `app_metered_ibfk_1` FOREIGN KEY (`developer_app_id`) REFERENCES `developer_app` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=10792 DEFAULT CHARSET=utf8mb3