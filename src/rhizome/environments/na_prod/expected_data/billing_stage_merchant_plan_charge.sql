CREATE TABLE `stage_merchant_plan_charge` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_id` int unsigned NOT NULL,
  `charge_id` bigint unsigned NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `num_of_devices` smallint unsigned NOT NULL,
  `merchant_plan_id` bigint unsigned NOT NULL,
  `plan_charge_type` enum('ADVANCE','ADJUSTMENT') NOT NULL,
  `request_uuid` char(13) NOT NULL,
  `promoted_time` timestamp NULL DEFAULT NULL,
  `promoted_id` bigint unsigned DEFAULT NULL,
  `device_type_id` smallint unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `charge_id` (`charge_id`),
  KEY `merchant_plan_charge_ibfk_1` (`merchant_id`),
  KEY `merchant_plan_id` (`merchant_plan_id`),
  KEY `request_uuid` (`request_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=1290635030 DEFAULT CHARSET=utf8mb3