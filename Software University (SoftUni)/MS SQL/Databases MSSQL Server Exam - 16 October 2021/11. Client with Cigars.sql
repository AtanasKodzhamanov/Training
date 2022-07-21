CREATE OR ALTER PROCEDURE usp_SearchByTaste @taste VARCHAR(30)
AS
BEGIN

SELECT CigarName, CONCAT('$',PriceForSingleCigar) as Price, @taste as TasteType, BrandName,Concat([Length],' cm') as CigarLength, Concat([RingRange],' cm') as CigarRingRange FROM Cigars as c
LEFT JOIN Sizes as s
ON c.SizeId=s.Id
LEFT JOIN Brands as b
ON c.BrandId = b.Id
WHERE TastID in (SELECT Id FROM Tastes WHERE TasteType= @taste)
ORDER BY CigarLength, CigarRingRange DESC

END