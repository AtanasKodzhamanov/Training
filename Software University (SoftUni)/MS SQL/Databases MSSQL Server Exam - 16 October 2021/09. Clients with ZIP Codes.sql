SELECT LastName,AVG(s.[Length]) as CiagrLenght, FLOOR(AVG(s.[RingRange]))+1 as CiagrRingRange FROM CLIENTS as c
INNER JOIN ClientsCigars as cc
ON c.Id=cc.ClientId
LEFT JOIN Cigars as cig
ON cc.CigarId=cig.Id
LEFT JOIN Sizes as s
ON cig.SizeId = s.Id 
GROUP BY LastName
ORDER BY CiagrLenght DESC