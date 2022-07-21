DELETE FROM[ClientsCigars]
WHERE [ClientId] in (SELECT Id FROM [Addresses] WHERE LEFT([Country],1)='C')

DELETE FROM[Clients]
WHERE [Id] in (SELECT Id FROM [Addresses] WHERE LEFT([Country],1)='C')

DELETE FROM [Addresses]
WHERE LEFT([Country],1)='C'