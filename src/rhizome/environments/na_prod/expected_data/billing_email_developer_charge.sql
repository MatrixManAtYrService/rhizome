CREATE TABLE `email_developer_charge` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `developer_id` bigint unsigned NOT NULL,
  `charge_id` bigint unsigned NOT NULL,
  `app_uuid` char(13) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `app_name` varchar(250) NOT NULL,
  `merchant_name` varchar(127) NOT NULL,
  `charge_status` varchar(127) NOT NULL,
  `charge_amount` bigint NOT NULL,
  `currency` char(3) NOT NULL,
  `developer_portion_amount` bigint DEFAULT NULL,
  `charge_created_time` timestamp NULL DEFAULT NULL,
  `done_time` timestamp NULL DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `developer_id` (`developer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3