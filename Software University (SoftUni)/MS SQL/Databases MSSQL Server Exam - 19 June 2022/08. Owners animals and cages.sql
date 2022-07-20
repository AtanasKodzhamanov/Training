SELECT v.Name,v.PhoneNumber,TRIM(REPLACE(REPLACE(v.Address,'Sofia , ',''),'Sofia, ','')) as Address FROM Volunteers as v
LEFT JOIN 
VolunteersDepartments as vd
ON v.DepartmentId=vd.Id
WHERE vd.DepartmentName='Education program assistant' AND v.Address like '%Sofia%'
ORDER BY v.Name