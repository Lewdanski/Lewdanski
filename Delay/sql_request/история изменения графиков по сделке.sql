#история изменения графика платежей, графика начислений
SELECT '5924740' INTO @ContractId;

select * from GraphsValidity where GraphsValidity.ContractId = @ContractId;

select * from Graphs where Graphs.ContractId = @ContractId;

select * from graphs_h where graphs_h.ContractId = @ContractId;

select * from GraphsAccrualValidity where GraphsAccrualValidity.ContractId = @ContractId;

select * from GraphsAccrualAddData where GraphsAccrualAddData.ContractId = @ContractId;

select * from GraphsAccrual where GraphsAccrual.ContractId = @ContractId;

select * from GraphsAccrualH where GraphsAccrualH.ContractId = @ContractId;

