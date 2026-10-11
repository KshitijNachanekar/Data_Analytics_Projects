# EV Battery Failure Analysis — Power BI Dashboard

An interactive Power BI report that explores **what separates failing EV batteries from healthy ones** across a fleet of **20,000 vehicles** (70 attributes each: health, thermal, charging, driving, environment and maintenance).

> **Headline:** 6.9% of vehicles (1,384) are flagged as battery failures. Failures are driven by **age, thermal condition and degradation**, not by brand, chemistry or charging habits.

![Executive Overview](screenshots/01-executive-overview.png)

## Key findings

| Finding | Evidence |
|---|---|
| Age is the strongest visible driver | Failure rate rises from **1.0%** (0–3 yrs) to **15.8%** (9–12 yrs); 2015 models fail at 18.4% vs 1.0% for 2023 |
| Thermal risk is a near-perfect warning sign | Vehicles with thermal runaway risk > 50 fail at **42.7%** vs **0.7%** when risk ≤ 10 |
| Failed batteries are measurably degraded | Battery health 71.5% vs 82.7%; capacity loss 28.5% vs 17.4%; aging score 80 vs 60 |
| Failed batteries are stressed | Stress index 58.5 vs 46.5 (+26%); internal resistance 0.63 vs 0.43 (+46%); ~2,000 fewer remaining cycles |
| Charging/driving habits barely matter | Charge efficiency 95.2% vs 96.3%; fast-charge ratio 0.35 vs 0.33 |
| Brand, chemistry, vehicle type, terrain are nearly flat | Segment failure rates all sit between ~6% and ~8% |

## Report pages

1. **Executive Overview** – total vehicles, failures, failure rate, failure distribution, health and thermal risk by status, status slicer
2. **Battery Health & Risk** – average battery health, state of health, capacity loss, battery stress by failure status
3. **Failure Drivers** – failure rate by chemistry, vehicle type, drive type, terrain, fleet vs private, manufacturing year, brand and battery manufacturer
4. **Failure Investigation** – battery stress, internal resistance and predicted remaining life cycles
5. **Charging & Driving** – charging and discharging efficiency
6. **Environment & Maintenance** – ambient temperature and maintenance score

## Data model

A single flat table (`ev battery_failure prediction Dataset`, 20,000 rows × 71 columns) with a calculated label column `Failure Status Label` ("Failure" / "No Failure"). See [docs/DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) and [docs/DAX_MEASURES.md](docs/DAX_MEASURES.md).

## How to open

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free, Windows).
2. Download `powerbi/EV_Battery_Failure_Analysis.pbix`.
3. Open it. The data is embedded, so no refresh or credentials are needed.

## Dataset

**EV Battery Health Prediction Dataset (20K)** on Kaggle, uploaded by `srisyra02`: <https://www.kaggle.com/datasets/srisyra02/ev-battery-health-prediction-dataset-20k>

The Kaggle page tags the data as *synthetic* and does not state a licence, so the raw CSV is **not** included in this repository. Download it from the link above to reproduce the analysis; all rights to the data remain with its original author.

## Limitations

- The dataset is tagged *synthetic* on Kaggle (and many fields are near-uniform), so findings describe this dataset, not real-world fleets.
- About 3–5% of values are blank in most numeric columns, and about 3% of text fields (vehicle type, chemistry, drive type) are empty.
- The report compares averages of failed vs healthy vehicles; it does not include a predictive model.

## Roadmap

- Replace blanks with "Unknown" in Power Query and add data-quality notes
- Risk and age bands (Low / Medium / High) as calculated columns
- Measures: failure rate vs fleet average, high-risk %, failures per 1,000 vehicles
- Drill-through to a vehicle detail page; top-N highest-risk vehicles table
- Train a failure-prediction model (Python/Fabric) and surface predicted probability

## Tools

Power BI Desktop · DAX · Power BI report theme "EV Battery Analytics – Midnight Teal"

## Licence

MIT — see [LICENSE](LICENSE).
