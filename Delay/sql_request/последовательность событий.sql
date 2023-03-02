#последовательность событий. В примере поиск сделок с событием ЧА после ДП
select * from `Events` join
(

	select 
	`Events`.Account,
	`Events`.Date
	from `Events` where `Events`.`Type` = 6 # код события ДП
	and `Events`.DateAnnul is null
)
 as s on `Events`.Account = s.Account
 
where
	`Events`.`Type` = 4 # код события ЧА
	and `Events`.Date > s.Date
	and `Events`.DateAnnul is null