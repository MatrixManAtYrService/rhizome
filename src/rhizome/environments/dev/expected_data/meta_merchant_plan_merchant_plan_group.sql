CREATE TABLE `merchant_plan_merchant_plan_group` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `merchant_plan_id` bigint unsigned NOT NULL,
  `merchant_plan_group_id` bigint unsigned NOT NULL,
  `default_plan` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `merchant_plan_id` (`merchant_plan_id`),
  KEY `merchant_plan_group_id` (`merchant_plan_group_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4678 DEFAULT CHARSET=utf8mb3