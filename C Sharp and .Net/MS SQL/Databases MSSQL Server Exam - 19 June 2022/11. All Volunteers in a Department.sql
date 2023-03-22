CREATE FUNCTION udf_GetVolunteersCountFromADepartment (@VolunteersDepartment VARCHAR(30))  
RETURNS INT
AS
BEGIN
	DECLARE @item INT = (
	SELECT Count(v.Id) FROM Volunteers as v LEFT JOIN VolunteersDepartments as vd ON v.DepartmentId=vd.Id WHERE vd.DepartmentName= @VolunteersDepartment
	)


	RETURN @item
END