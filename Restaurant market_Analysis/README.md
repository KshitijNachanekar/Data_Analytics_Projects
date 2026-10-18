# Restaurant Market Analysis - Power BI Dashboard (India)

An interactive, multi-page Power BI report analysing **44,751 restaurant listings across 97 Indian cities** (24 states, 124 cuisines) from Zomato's public listings: ratings, pricing, delivery speed, cuisines, cities and safety measures.

![Executive Dashboard](screenshots/01-executive-dashboard.png)

> Independent portfolio project. Not affiliated with Zomato.

## Key findings

| Finding | Evidence |
|---|---|
| Market is concentrated in the North | North India holds 40% of listings; Delhi NCR (1,439) and Kolkata (1,296) lead |
| Ratings are high and tightly bunched | Average 3.92; 56% of rated restaurants score 4.0+; 16% of listings are unrated |
| Price does not buy ratings | Every price band averages about 3.92 (correlation with rating about -0.01); premium (above Rs 400) is only 1.7% of listings |
| Faster delivery goes with better ratings | Under 25 min: 4.00 vs 40+ min: 3.89 (correlation about -0.10) |
| Dessert cuisines rate highest | Mithai and Ice Cream 4.09 vs Pizza 3.86, Momos 3.87, Rolls 3.88 |
| Big speed gaps between cities | Guntur 22.5 min vs Kolkata 44.7 min (cities with 300+ listings) |
| Safety | 57% of restaurants follow the full "Max Safety" protocol |

## Report pages
1. **Executive Dashboard** - 8 KPI cards with "vs India" notes, top cities vs rating, price mix, state map and table, region and cuisine mix, key insights, strategic focus areas
2. **City & Regional Analysis** - top cities and states, rating by region, city performance table
3. **Cuisine Analysis** - most listed, highest rated and priciest cuisines
4. **Pricing & Ratings** - price band mix, rating by price band, rating distribution, priciest cities
5. **Delivery & Safety** - availability, speed bands, rating vs speed, fastest and slowest cities

Every page has Region and State dropdown filters and sidebar navigation.

## Tech
Power BI Desktop (PBIP project format with TMDL + PBIR, so every file is plain text and Git-friendly) - DAX - Power Query (M) - Python (pandas) for cleaning.

## Data cleaning (`scripts/clean_data.py`)
- Removed 140 exact duplicate rows (44,891 to 44,751). The source has no outlet address, so some may be genuine separate outlets.
- Rating: text to number; "New" and "-" kept as unrated (6,978 listings).
- Price: parsed "Rs X for one" text to numbers (23 blanks) and added price bands.
- Delivery time: extracted minutes; non-numeric statuses (opens later, closed, closing soon, hours unavailable) moved to a Delivery Status column; 1 implausible value (under 5 min) set blank; added speed bands.
- City: merged "NCR" into "Delhi NCR"; added State and Region (North / South / East / West / Central, a grouping chosen for this project).
- Brand: derived from the name before " - " to count chain outlets.
- Cuisine: split the multi-value column into a separate `Cuisines` table (158,526 rows).

## Data model
`Restaurants` (1) -> `Cuisines` (many) on Restaurant ID. 24 measures on Restaurants and 8 on Cuisines, including RANKX-based Top-N measures that respond to slicers. See [docs/DAX_MEASURES.md](docs/DAX_MEASURES.md).

## Repository structure
```
.
|-- Zomato_Restaurant_Analysis.pbip          # open this in Power BI Desktop
|-- Zomato_Restaurant_Analysis.Report/       # report pages and visuals (PBIR)
|-- Zomato_Restaurant_Analysis.SemanticModel/# tables, measures, relationships (TMDL)
|-- scripts/clean_data.py                    # raw CSV -> cleaned CSVs
|-- docs/DAX_MEASURES.md
|-- raw/        # put the Kaggle file here (not tracked)
|-- data/       # cleaned CSVs are generated here (not tracked)
|-- screenshots/
`-- requirements.txt
```

## Run it yourself
1. Download the dataset from Kaggle (link below) and save it as `raw/zomato_dataset.csv`.
2. `pip install -r requirements.txt` then `python scripts/clean_data.py` - creates `data/restaurants.csv` and `data/cuisines.csv`.
3. Open `Zomato_Restaurant_Analysis.pbip` in Power BI Desktop (turn on the Power BI Project / TMDL / enhanced report format preview features if asked, then restart).
4. Home > Transform data > Edit parameters > set **DataFolder** to the full path of your `data` folder, ending with a backslash (for example `C:\projects\restaurant-market-analysis-powerbi\data\`).
5. Click **Refresh**.

## Limitations
- The dataset has no dates, votes or revenue, so there is no time trend or sales analysis.
- It is a snapshot; ratings and delivery times reflect the moment of collection.
- Key Insights and Strategic Focus text on the Executive Dashboard is static.
- The state map needs internet access and Power BI's map visuals enabled.

## Data source
Kaggle: *Zomato Top 100 Cities Restaurant Data* by rrkcoder - https://www.kaggle.com/datasets/rrkcoder/zomato-data-40k-restaurants-of-indias-100-cities
The Kaggle page does not state a licence, so the data files are not included in this repository. All rights to the data remain with its original author.

## Author
Kshitij Nachanekar - Computer Engineering student, Data Analysis | Power BI | SQL | Python

## Licence
Code, report and documentation: MIT (see [LICENSE](LICENSE)). The dataset is not covered.
