# Принадлежность сделки лизингу факторингу
select 
	Contracts.ContractNumber,
	Contracts.ContractDate
from 
	Contracts join kinds_registrations on Contracts.kind_reg_id = kinds_registrations.kind_reg_id
 		and kinds_registrations.kind_reg_bargain_id = 50 
	join KindsSettingReg on kinds_registrations.kind_reg_id = KindsSettingReg.KindReg
	 and KindsSettingReg.Code = 1 # Настройка "Признак принадлежности к открытому факторингу"
	 and KindsSettingReg.DataInt = 1 # у вида установлен признак факторинга
