CREATE TABLE `bi_context` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `context` enum('MERCHANT_PLAN','MERCHANT_PLAN_GROUP') DEFAULT NULL,
  `context_id` bigint unsigned NOT NULL,
  `billing_business_initiative_id` bigint unsigned NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bi_context_key` (`billing_business_initiative_id`,`context_id`,`context`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb3