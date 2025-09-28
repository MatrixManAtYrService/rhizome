CREATE TABLE `stage_merchant_app_charge` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_app_id` bigint unsigned NOT NULL,
  `app_subscription_id` bigint unsigned DEFAULT NULL,
  `charge_id` bigint unsigned NOT NULL,
  `created_time` timestamp NULL DEFAULT NULL,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `merchant_id` int unsigned NOT NULL,
  `developer_id` bigint unsigned NOT NULL,
  `app_id` bigint unsigned NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `promoted_time` timestamp NULL DEFAULT NULL,
  `promoted_id` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `merchant_app_id` (`merchant_app_id`),
  KEY `charge_id` (`charge_id`),
  KEY `request_uuid` (`request_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=1106467762 DEFAULT CHARSET=utf8mb3