#поиск сделок с выгруженными реестрами
select *
from Contracts 
	join kinds_registrations on Contracts.kind_reg_id = kinds_registrations.kind_reg_id
	 and kinds_registrations.kind_reg_bargain_id = 50 # лизинг
	join factoring_doc on Contracts.ContractId = factoring_doc.factoring_doc_contract_id
	 and factoring_doc.`Order` = 1 #первый выкуп
	join factoring on factoring.factoring_id = factoring_doc.factoring_doc_factoring_id
	 and factoring.factoring_to_file = 1 # реестр выгружен 
where
	# задание периода регистрации сделок
	Contracts.ContractDate > '2018-01-01 00:00:00'
 		and Contracts.ContractDate < '2018-04-01 00:00:00'