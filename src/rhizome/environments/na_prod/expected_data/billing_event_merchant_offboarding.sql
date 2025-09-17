CREATE TABLE `merchant_offboarding` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `uuid` char(36) NOT NULL,
  `merchant_uuid` char(13) NOT NULL,
  `environment` char(25) NOT NULL,
  `step` enum('INITIATE','REMINDER','OFFBOARD','IMMEDIATE','PROCESSING','PROCESSED','CANCELED','REOPENED','BLOCKED') NOT NULL,
  `due_date` date NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  `offboard_timestamp` datetime(6) NOT NULL,
  `deleted_timestamp` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci