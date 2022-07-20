CREATE OR ALTER PROCEDURE usp_AnimalsWithOwnersOrNot(@AnimalName VARCHAR(30))
AS
BEGIN
	SELECT a.Name, CASE WHEN o.Name IS NULL THEN 'For adoption' ELSE o.Name END as Name FROM Owners as o
	 Right JOIN Animals as a 
	ON o.Id=a.OwnerId
	WHERE a.Name=@AnimalName
END