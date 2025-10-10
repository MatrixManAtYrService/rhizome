CREATE TABLE `merchant_app_subscription_history` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_app_id` bigint unsigned NOT NULL,
  `old_app_subscription_id` bigint unsigned DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `merchant_app_id` (`merchant_app_id`),
  KEY `old_app_subscription_id` (`old_app_subscription_id`),
  CONSTRAINT `merchant_app_subscription_history_ibfk_1` FOREIGN KEY (`merchant_app_id`) REFERENCES `merchant_app` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `merchant_app_subscription_history_ibfk_2` FOREIGN KEY (`old_app_subscription_id`) REFERENCES `app_subscription` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE=InnoDB AUTO_INCREMENT=2791 DEFAULT CHARSET=utf8mb3