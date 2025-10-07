CREATE TABLE `combined_disbursement_tree` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `combined_disbursement_id` bigint unsigned NOT NULL,
  `charge_id` bigint unsigned NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `combined_disburtree_comb_id` (`combined_disbursement_id`,`charge_id`),
  KEY `combined_disburtree_disbur_id` (`charge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=416301 DEFAULT CHARSET=utf8mb3