CREATE TABLE `charge_capture_error` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_uuid` char(13) NOT NULL,
  `mid` varchar(32) NOT NULL,
  `file_instance_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8mb3