# DAX Measures

Table: `ev battery_failure prediction Dataset`

```DAX
Total Vehicles =
DISTINCTCOUNT ( 'ev battery_failure prediction Dataset'[vehicle_id] )

Battery Failures =
CALCULATE (
    COUNTROWS ( 'ev battery_failure prediction Dataset' ),
    'ev battery_failure prediction Dataset'[battery_failure] = 1
)

Failure Rate =
DIVIDE ( [Battery Failures], [Total Vehicles], 0 )

Average Battery Health =
AVERAGE ( 'ev battery_failure prediction Dataset'[battery_health_percent] )

Average State of Health =
AVERAGE ( 'ev battery_failure prediction Dataset'[state_of_health] )

Average Capacity Loss =
AVERAGE ( 'ev battery_failure prediction Dataset'[capacity_loss_percent] )
```

## Calculated column

`Failure Status Label` maps `battery_failure` (1 / 0) to "Failure" / "No Failure" for readable chart labels and slicers.

## Suggested next measures

```DAX
Failure Rate vs Fleet Avg =
VAR FleetRate =
    CALCULATE ( [Failure Rate], ALL ( 'ev battery_failure prediction Dataset' ) )
RETURN
    [Failure Rate] - FleetRate

Failures per 1,000 Vehicles = [Failure Rate] * 1000

High Risk Vehicles % =
DIVIDE (
    CALCULATE (
        COUNTROWS ( 'ev battery_failure prediction Dataset' ),
        'ev battery_failure prediction Dataset'[thermal_runaway_risk] > 50
    ),
    [Total Vehicles]
)
```
