SELECT TOP(5) CigarName, PriceForSingleCigar, ImageURL FROM Cigars
WHERE (SizeId IN (SELECT Id FROM Sizes WHERE [Length]>=12) AND [CigarName] LIKE '%ci%') OR
(SizeId IN (SELECT Id FROM Sizes WHERE [Length]>=12) AND PriceForSingleCigar>50 AND SizeId IN (SELECT Id FROM Sizes WHERE RingRange>2.55) )
ORDER BY CigarName, PriceForSingleCigar DESC