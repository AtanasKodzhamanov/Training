SELECT TOP(5) o.Name, COUNT(o.Id) as CountOfAnimals	 FROM [Owners] as o
LEFT JOIN Animals as a
ON o.Id=a.OwnerId
GROUP BY o.Id , o.Name
ORDER BY CountOfAnimals DESC, o.Name