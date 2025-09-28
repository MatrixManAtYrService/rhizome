CREATE TABLE `app_app_bundle` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `app_bundle_id` bigint unsigned NOT NULL,
  `developer_app_id` bigint unsigned NOT NULL,
  `allow_uninstall` tinyint(1) DEFAULT '0',
  `charge` tinyint(1) DEFAULT '1',
  `app_subscription_id` bigint unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app_bundle_id` (`app_bundle_id`),
  KEY `developer_app_id` (`developer_app_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30660 DEFAULT CHARSET=latin1