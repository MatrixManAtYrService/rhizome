CREATE TABLE `merchant_merchant_plan_history` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `merchant_id` int unsigned NOT NULL,
  `old_merchant_plan_id` int unsigned DEFAULT NULL,
  `new_merchant_plan_id` int unsigned DEFAULT NULL,
  `changed_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `merchant_id` (`merchant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=397215 DEFAULT CHARSET=utf8mb3