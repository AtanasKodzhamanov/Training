SELECT c.Id, CigarName,PriceForSingleCigar,TasteType,TasteStrength FROM [Cigars] as c
LEFT JOIN [Tastes] as t
ON c.TastId=t.Id
WHERE t.TasteType IN ('Earthy','Woody')
ORDER BY PriceForSingleCigar DESC