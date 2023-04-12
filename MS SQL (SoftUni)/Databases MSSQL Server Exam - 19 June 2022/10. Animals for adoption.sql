SELECT a.Name, DATEPART(year,a.BirthDate) as BirthDate, att.AnimalType FROM Animals as a
LEFT JOIN AnimalTypes as att
ON a.AnimalTypeId=att.Id
WHERE a.OwnerId IS NULL AND a.AnimalTypeId !=3 AND DATEPART(year,a.BirthDate)+5>2022
ORDER BY a.Name