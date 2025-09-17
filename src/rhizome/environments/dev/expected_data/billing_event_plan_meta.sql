CREATE TABLE `plan_meta` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `country` char(2) DEFAULT NULL,
  `plan_type` enum('CLASSIC','PAYMENTS','PAYMENTS_PLUS','REGISTER_LITE','REGISTER','QSR','DINING','NO_HARDWARE','SERVICES','RETAIL') DEFAULT NULL,
  `plan_uuid` char(13) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `value` varchar(2048) DEFAULT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `modified_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
  `deleted_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3