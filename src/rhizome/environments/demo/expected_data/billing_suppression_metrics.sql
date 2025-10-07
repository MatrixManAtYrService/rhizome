CREATE TABLE `suppression_metrics` (
  `supp_month` date NOT NULL,
  `supp_type` enum('MERCHANT','APP','RESELLER','COUNTRY','MERCHANT_BY_APP') NOT NULL,
  `supp_context` enum('SYSTEM','SUNSET','PROMO','FINANCE_EXCEPTION','OFFER','OFF_BOARDED','TRIAL','PILOT','OVERRIDE','NO_PLAN','NO_CLOVER_APPS','FIELD_TEST','DEBIT_NO_AUTH','DEMO','ACH_HOLD','SEASONAL','ALL') NOT NULL,
  `plan_charges` bigint NOT NULL,
  `app_charges` bigint NOT NULL,
  `wm_charges` bigint NOT NULL,
  `total_charges` bigint NOT NULL,
  `num_suppressions` bigint NOT NULL,
  `num_merchants` bigint NOT NULL,
  PRIMARY KEY (`supp_month`,`supp_type`,`supp_context`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3