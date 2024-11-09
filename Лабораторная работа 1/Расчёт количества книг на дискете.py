
disk = 1.44
k = 1024
str_ = 100
strok = 50
simv = 25
need = 4

size_strok = need * simv
size_str_ = size_strok * strok
size_book = size_str_ * str_

size_disk = disk * (k ** 2)

answer = round(size_disk / size_book)

print("Количество книг, помещающихся на дискету:", answer)
