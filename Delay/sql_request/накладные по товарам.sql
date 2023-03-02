select

InvoiceData.`*`,
ListGoods.GoodsName,
Contracts.ContractId,
Contracts.ContractNumber

from 

Contracts join ListGoods on ListGoods.ContractId = Contracts.ContractId
join InvoiceData on ListGoods.Id = InvoiceData.ListGoodsId
where
Contracts.ContractNumber = 74128511