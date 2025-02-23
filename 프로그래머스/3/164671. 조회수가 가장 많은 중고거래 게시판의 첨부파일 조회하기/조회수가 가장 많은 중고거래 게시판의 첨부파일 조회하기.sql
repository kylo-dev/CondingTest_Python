select concat('/home/grep/src/', board.board_id, '/', file.file_id, file.file_name, file.file_ext) as file_path from used_goods_board board
join used_goods_file file on board.board_id = file.board_id
where board.views = (
    select max(b2.views) from used_goods_board b2
)
order by file.file_id desc