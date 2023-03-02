#сделать анкету задним числом #

#запустить сначала для получения параметров #
select * from ApprovalForms where ApprovalForms.FormId = 74128523;

###
select '2020-08-21 15:16:58' into @InputTime;
select '74128523' into @ContractNumber; 

update ApprovalForms
 set ApprovalForms.InputTime =@InputTime, 
 	  ApprovalForms.DateScore = @InputTime
 where ApprovalForms.FormId =  @ContractNumber;
 
