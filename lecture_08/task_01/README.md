### Task
Read data from cvs files in asset folder and import into SQLite database.

### CVS structure 'catalog.csv':
 1. Id number
 2. Product name
 3. Product color/colors
 4. Group of product
 5. Sports, for which the article is intended
 6. Category
 7. Sub Category
 8. Gender and Age Group (Men, Women, Unisex, Infant)
 
Example of row of file:

```
"538352","TYGUN II","BLACK/RUNNINWHT","FOOTWEAR","BOXING","SHOES","SHOES (LOW)","Men"
"42259","M TEAM TEE","WHITE/DARKNAVY","TEXTILES","TENNIS","T-SHIRTS","T-SHIRT (SHORT SLEEVE)","Men"
"562319","NOVA WALK 06","DARONX/METSIL/DSHALE","FOOTWEAR","WALKING","SHOES","SHOES (LOW)","Men"
"G13130","COMPOUND","BLACK1/BLACK1/LGTIPD","FOOTWEAR","GOLF","SHOES","SHOES (LOW)","Men"
"396559","+TG SWERVE DBMI","WHITE/BLACK","HARDWARE","FOOTBALL/SOCCER","BALLS","BALL (MACHINE-STITCHED)","Men"
"34549","LTA SS2G C","RUNWHI/SHABLU/VAPOUR","FOOTWEAR","BASKETBALL","SHOES","SHOES (LOW)","Kid"
```

### CVS structure 'sale-10K.csv':
 1. Id number
 2. Country was carried sale (ISO code)
 3. Town was carried sale
 4. Date/hour on sale with timezone (ISO8601)
 5. Sale price (the price of the same item in different countries are different)

Example of row of file:

```
"561712","ES","Murcia","2015-12-11T17:14:05+01:00",43.21
"K81938","FR","Nantes","2016-01-14T20:58:38+01:00",36.57
"41975","IT","Catania","2016-01-12T10:57:50+01:00",409.58
"538352","DE","Düsseldorf","2015-12-18T20:50:21+01:00",95.03
```
