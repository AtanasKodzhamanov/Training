SELECT o.Name+'-'+a.Name as OwnersAnimals,o.PhoneNumber,ac.CageId FROM Owners as o
INNER JOIN Animals as a
ON o.Id=a.OwnerId
INNER JOIN AnimalsCages as ac
ON a.Id=ac.AnimalId
WHERE a.AnimalTypeId IN ( SELECT Id FROM AnimalTypes WHERE AnimalType='Mammals')
ORDER BY o.Name, a.Name DESC