CREATE or ALTER FUNCTION udf_ClientWithCigars(@name NVARCHAR(30))  
RETURNS INT
AS
BEGIN
	DECLARE @item INT = (SELECT COUNT(cc.CigarId) FROM Clients as c LEFT JOIN ClientsCigars as cc
ON c.Id=cc.ClientId WHERE FirstName= @name GROUP BY c.FirstName)
RETURN @item
END