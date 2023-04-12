SELECT Id, FirstName+' ' +LastName as ClientName, Email FROM [Clients]
WHERE Id  NOT IN (SELECT ClientId FROM ClientsCigars)
ORDER BY ClientName