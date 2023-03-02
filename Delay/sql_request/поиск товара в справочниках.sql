#поиск товара сделки в справочнике товаров
select *
from Goods
	join good_names on Goods.Name_Id = good_names.good_name_id
	join good_names_marks on good_names.good_name_id = good_names_marks.good_name
	join marks on good_names_marks.mark = marks.mark_id
where
	Goods.GoodsId = 403624 # id из анкеты
	 and marks.mark_id = 6116 # id из анкеты