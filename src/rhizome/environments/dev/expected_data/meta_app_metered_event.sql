CREATE TABLE `app_metered_event` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `merchant_app_id` bigint unsigned NOT NULL,
  `app_metered_id` bigint unsigned NOT NULL,
  `count` bigint unsigned NOT NULL,
  `charge_id` bigint unsigned DEFAULT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `merchant_app_id` (`merchant_app_id`),
  KEY `app_metered_id` (`app_metered_id`),
  KEY `app_line_item_id` (`charge_id`),
  CONSTRAINT `app_metered_event_ibfk_1` FOREIGN KEY (`merchant_app_id`) REFERENCES `merchant_app` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app_metered_event_ibfk_2` FOREIGN KEY (`app_metered_id`) REFERENCES `app_metered` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `app_metered_event_ibfk_3` FOREIGN KEY (`charge_id`) REFERENCES `charge` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=4419 DEFAULT CHARSET=utf8mb3