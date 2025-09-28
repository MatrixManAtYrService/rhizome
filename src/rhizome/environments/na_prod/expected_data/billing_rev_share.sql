CREATE TABLE `rev_share` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `charge_uuid` char(13) CHARACTER SET latin1 NOT NULL,
  `developer` int DEFAULT NULL,
  `partner` int DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `charge_uuid` (`charge_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=125678628 DEFAULT CHARSET=utf8mb3