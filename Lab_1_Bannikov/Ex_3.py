# TODO Найдите количество книг, которое можно разместить на дискете
volume_of_disk = 1.44
pages_of_book = 100
strings_on_page = 50
symbols_of_string = 25
one_symbol = 4

one_book = one_symbol * symbols_of_string * strings_on_page * pages_of_book
volume_of_disk_bite = volume_of_disk * 1024 * 1024
books = int(volume_of_disk_bite // one_book)

print("Количество книг, помещающихся на дискету:", books)
