CREATE TABLE `producer_failure` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(26) NOT NULL,
  `environment` varchar(25) NOT NULL,
  `reference_id` char(13) NOT NULL,
  `event_source` enum('MLC','PLAN_ADVANCE','CELLULAR_ARREARS','APP_SUB_DAILY','APP_METER_DAILY','APP_RATES','APP_SUB_ADVANCE','BACKBOOK_MERCHANT','BACKBOOK_MLC','BACKBOOK_APP','MISC_PAYMENT','PLAN_ARREARS','AGREEMENT') NOT NULL,
  `event_context_json` text,
  `input_event_uuid` varchar(26) DEFAULT NULL,
  `input` text,
  `output` text NOT NULL,
  `channel` varchar(25) NOT NULL,
  `topic` varchar(127) NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  KEY `reference_id` (`reference_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb3