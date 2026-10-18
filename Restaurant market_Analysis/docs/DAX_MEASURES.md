# DAX Measures

## Restaurants table

**Total Restaurants**
```DAX
Total Restaurants = COUNTROWS(Restaurants)
```

**Unique Brands**
```DAX
Unique Brands = DISTINCTCOUNT(Restaurants[Brand])
```

**Cities Covered**
```DAX
Cities Covered = DISTINCTCOUNT(Restaurants[City])
```

**Avg Rating**
```DAX
Avg Rating = AVERAGE(Restaurants[Rating])
```

**Highly Rated %**
```DAX
Highly Rated % = DIVIDE(CALCULATE(COUNTROWS(Restaurants), Restaurants[Rating] >= 4), CALCULATE(COUNTROWS(Restaurants), Restaurants[Rating] <> BLANK()))
```

**Avg Price for One**
```DAX
Avg Price for One = AVERAGE(Restaurants[Price for One])
```

**Avg Delivery Time (min)**
```DAX
Avg Delivery Time (min) = AVERAGE(Restaurants[Delivery Minutes])
```

**Max Safety %**
```DAX
Max Safety % = DIVIDE(CALCULATE(COUNTROWS(Restaurants), Restaurants[Safety Level] = "Max Safety"), COUNTROWS(Restaurants))
```

**Top 10 Cities**
```DAX
Top 10 Cities = VAR r = RANKX(ALLSELECTED(Restaurants[City]), [Total Restaurants], , DESC, Dense) RETURN IF(r <= 10, [Total Restaurants])
```

**Top 15 Cities**
```DAX
Top 15 Cities = VAR r = RANKX(ALLSELECTED(Restaurants[City]), [Total Restaurants], , DESC, Dense) RETURN IF(r <= 15, [Total Restaurants])
```

**Top 12 States**
```DAX
Top 12 States = VAR r = RANKX(ALLSELECTED(Restaurants[State]), [Total Restaurants], , DESC, Dense) RETURN IF(r <= 12, [Total Restaurants])
```

**Priciest Cities (Avg Price)**
```DAX
Priciest Cities (Avg Price) = VAR t = FILTER(ALLSELECTED(Restaurants[City]), [Total Restaurants] >= 300) VAR r = RANKX(t, [Avg Price for One], , DESC, Dense) RETURN IF([Total Restaurants] >= 300 && r <= 15, [Avg Price for One])
```

**Fastest Cities (Avg Min)**
```DAX
Fastest Cities (Avg Min) = VAR t = FILTER(ALLSELECTED(Restaurants[City]), [Total Restaurants] >= 300) VAR r = RANKX(t, [Avg Delivery Time (min)], , ASC, Dense) RETURN IF([Total Restaurants] >= 300 && r <= 12, [Avg Delivery Time (min)])
```

**Slowest Cities (Avg Min)**
```DAX
Slowest Cities (Avg Min) = VAR t = FILTER(ALLSELECTED(Restaurants[City]), [Total Restaurants] >= 300) VAR r = RANKX(t, [Avg Delivery Time (min)], , DESC, Dense) RETURN IF([Total Restaurants] >= 300 && r <= 12, [Avg Delivery Time (min)])
```

## Cuisines table

**Cuisine Listings**
```DAX
Cuisine Listings = COUNTROWS(Cuisines)
```

**Avg Rating by Cuisine**
```DAX
Avg Rating by Cuisine = AVERAGEX(Cuisines, RELATED(Restaurants[Rating]))
```

**Avg Price by Cuisine**
```DAX
Avg Price by Cuisine = AVERAGEX(Cuisines, RELATED(Restaurants[Price for One]))
```

**Top 15 Cuisines**
```DAX
Top 15 Cuisines = VAR r = RANKX(ALLSELECTED(Cuisines[Cuisine]), [Cuisine Listings], , DESC, Dense) RETURN IF(r <= 15, [Cuisine Listings])
```

**Top Rated Cuisines (300+ listings)**
```DAX
Top Rated Cuisines (300+ listings) = VAR t = FILTER(ALLSELECTED(Cuisines[Cuisine]), [Cuisine Listings] >= 300) VAR r = RANKX(t, [Avg Rating by Cuisine], , DESC, Dense) RETURN IF([Cuisine Listings] >= 300 && r <= 15, [Avg Rating by Cuisine])
```

**Priciest Cuisines (300+ listings)**
```DAX
Priciest Cuisines (300+ listings) = VAR t = FILTER(ALLSELECTED(Cuisines[Cuisine]), [Cuisine Listings] >= 300) VAR r = RANKX(t, [Avg Price by Cuisine], , DESC, Dense) RETURN IF([Cuisine Listings] >= 300 && r <= 15, [Avg Price by Cuisine])
```
