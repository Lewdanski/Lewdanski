#поиск сделок по номеру реестра
select 
	Contracts.ContractNumber
from 
Contracts 
	join kinds_registrations on Contracts.kind_reg_id = kinds_registrations.kind_reg_id
 		and kinds_registrations.kind_reg_bargain_id in (40,50) #продажа, лизинг
	join factoring_doc on Contracts.ContractId = factoring_doc.factoring_doc_contract_id
		and factoring_doc.`Order` = 1	
	join factoring on factoring.factoring_id = factoring_doc.factoring_doc_factoring_id
where
 factoring.factoring_doc = 47612 #номер реестра 