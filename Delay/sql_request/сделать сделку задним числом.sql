#сделать сделку задним числом #
#запустить сначала для получения параметров #
#после запускать по блокам по необходимости#
select * from Contracts where Contracts.ContractNumber = 74128447;

# задать необходимую дату договора #
select '2020-05-23 14:00:07' into @ContractDate;
select '74128447' into @ContractNumber; 

update Contracts 
 set Contracts.ContractDate = @ContractDate where Contracts.ContractNumber = @ContractNumber;
 
update Accounts 
 set Accounts.CreateDate = @ContractDate where Accounts.Account = @ContractNumber;
 
update ApprovalForms
 set ApprovalForms.InputTime =@ContractDate, 
 	  ApprovalForms.DateScore = @ContractDate
 where ApprovalForms.FormId =  @ContractNumber;
 
update Operations
 set Operations.OperationDate = @ContractDate
 where Operations.Account = @ContractNumber;

#сдвиг графика платежей на 1 месяц назад #
SELECT '5924858' INTO @ContractId;

update Graphs set 
 Graphs.Date = DATE_ADD(Graphs.Date,INTERVAL -1 MONTH)  
where Graphs.ContractId = @ContractId; 

update Contracts set 
 Contracts.DateLastPayment = DATE_ADD(Contracts.DateLastPayment,INTERVAL -1 MONTH),
 Contracts.DateLastPaymentNew = DATE_ADD(Contracts.DateLastPaymentNew,INTERVAL -1 MONTH)
where Contracts.ContractId = @ContractId;
#####