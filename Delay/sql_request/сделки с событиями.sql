#поиск сделки с событием
select 
 `Events`.*
from
Contracts 
	join Accounts on Contracts.ContractId = Accounts.ContractId
	join `Events` on Accounts.Account = `Events`.Account
 		and `Events`.`Type` = 4 #код события ЧА
 		and `Events`.DateAnnul is null