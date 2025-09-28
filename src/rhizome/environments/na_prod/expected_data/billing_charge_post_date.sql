CREATE TABLE `charge_post_date` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_id` bigint unsigned NOT NULL,
  `post_date` date DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `charge_id` (`charge_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41302596 DEFAULT CHARSET=utf8mb3