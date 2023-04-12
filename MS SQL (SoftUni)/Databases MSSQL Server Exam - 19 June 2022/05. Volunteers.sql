SELECT Name,AnimalType, FORMAT (BirthDate, 'dd.MM.yyyy') as BirthDate FROM Animals as an
LEFT JOIN AnimalTypes as aty
ON an.AnimalTypeId = aty.Id
ORDER BY Name