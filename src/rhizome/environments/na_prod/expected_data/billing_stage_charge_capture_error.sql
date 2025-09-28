CREATE TABLE `stage_charge_capture_error` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_uuid` char(13) NOT NULL,
  `mid` varchar(32) NOT NULL,
  `file_instance_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `promoted_time` timestamp NULL DEFAULT NULL,
  `promoted_id` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1524998 DEFAULT CHARSET=utf8mb3