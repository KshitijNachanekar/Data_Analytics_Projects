# Data Dictionary

20,000 rows (one per vehicle) × 70 source columns + 1 calculated column. Descriptions are inferred from column names; confirm against the original dataset documentation.

| Group | Columns |
|---|---|
| Vehicle | vehicle_id, vehicle_brand, vehicle_model, vehicle_type, manufacturing_year, drive_type, fleet_or_private, odometer_km, vehicle_age_years |
| Battery | battery_manufacturer, battery_chemistry, battery_capacity_kwh, battery_serial, cycle_count, remaining_capacity, predicted_remaining_life_cycles |
| Health | battery_health_percent, state_of_health, capacity_loss_percent, aging_score, thermal_health_score, cooling_system_health |
| Electrical | state_of_charge, depth_of_discharge, cell_voltage_avg, cell_voltage_std, pack_voltage, internal_resistance, voltage_imbalance, abnormal_voltage_events |
| Thermal | cell_temperature_avg, cell_temperature_max, temperature_variance, thermal_runaway_risk |
| Charging | charge_efficiency, discharge_efficiency, charging_cycles_last_month, fast_charge_ratio, slow_charge_ratio, average_charge_power_kw, average_charging_time, overnight_charging_ratio, home_charging_ratio, charging_interruptions, overcharge_events, charging_quality_score |
| Driving | average_speed, average_trip_distance, aggressive_acceleration_score, hard_braking_score, regenerative_braking_usage, highway_driving_ratio, city_driving_ratio, daily_distance, driving_stress_score |
| Environment | average_ambient_temperature, maximum_temperature, minimum_temperature, humidity, altitude, terrain_type, dust_exposure |
| Maintenance / BMS | last_service_days, firmware_updates, previous_faults, maintenance_score, sensor_fault_count, BMS_warning_count |
| Composite scores | battery_stress_index |
| Target | battery_failure (1 = failure, 0 = no failure) |
| Calculated | Failure Status Label ("Failure" / "No Failure") |

## Data quality notes

- ~600–1,000 blank values (3–5%) in most numeric columns
- ~640–730 empty strings each in vehicle_type, battery_chemistry and drive_type
- Class balance: 18,616 No Failure (93.1%) vs 1,384 Failure (6.9%)
