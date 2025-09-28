CREATE TABLE `combined_charge_tree` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `combined_charge_id` bigint unsigned NOT NULL,
  `charge_id` bigint unsigned NOT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `combined_chrgtree_comb_id` (`combined_charge_id`,`charge_id`),
  KEY `combined_chrgtree_chrg_id` (`charge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=173169670 DEFAULT CHARSET=utf8mb3