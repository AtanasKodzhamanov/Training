SELECT a.FullName, Country,ZIP, CONCAT('$',Max(PriceForSingleCigar)) as PriceForSingleCigar FROM (SELECT FirstName + ' ' +LastName as FullName, Country,ZIP, PriceForSingleCigar FROM Clients as c
LEFT JOIN Addresses as a
ON c.AddressId=a.Id
LEFT JOIN ClientsCigars as cc
ON a.Id=cc.ClientId
LEFT JOIN Cigars as cig
ON cc.CigarId = cig.Id
WHERE ISNUMERIC(ZIP)>0) as a
GROUP BY a.FullName, Country,ZIP