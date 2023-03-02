#сделки с кол-вом товаров более 1 шт (без проверки актуальности)
select 
	Contracts.ContractNumber,
	Contracts.ContractDate,
	sum(ListGoods.Number) as shtuki,
	count(ListGoods.Id) as pozicii
from 
	Contracts join kinds_registrations on Contracts.kind_reg_id = kinds_registrations.kind_reg_id
	 and kinds_registrations.kind_reg_bargain_id = 50
	 join ListGoods on Contracts.ContractId = ListGoods.ContractId
	 join Accounts on Contracts.ContractId = Accounts.ContractId
	  and Accounts.`Condition` = 0

where Contracts.ContractDate > '2019-01-01 00:00:00'
  
group by 
	 Contracts.ContractId
having shtuki > 2
	 and shtuki<>pozicii