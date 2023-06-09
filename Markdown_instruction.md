<font color="grei">

# Инструкция по Markdown
</font>
<font color="#ADD8E6">

## Выделение текста

Чтобы выделить текст в Markdown, используйте один из следующих способов:

* Жирный текст: для выделения текста жирным шрифтом, оберните его двумя символами ** с обеих сторон. Например, **этот текст будет жирным** будет выглядеть как этот текст будет жирным.

* Курсивный текст: для выделения текста курсивом, оберните его одинарными символами _ или * с обеих сторон. Например, _этот текст будет курсивом_ или *этот текст будет курсивом* будет выглядеть как этот текст будет курсивом.

* Зачеркнутый текст: чтобы добавить зачеркивание, оберните текст двумя символами ~~. Например, ~~этот текст будет зачеркнутым~~ будет выглядеть как этот текст будет зачеркнутым.

* Заголовки: для создания заголовков используйте символ #. Чем больше знаков # вы добавляете перед текстом, тем меньше размер заголовка. Например, # Заголовок первого уровня будет выглядеть как заголовок первого уровня, а ## Заголовок второго уровня будет выглядеть как заголовок второго уровня.
## Списки
Чтобы создать список в Markdown, используйте один из двух доступных типов списков: неупорядоченный список и упорядоченный список.

Неупорядоченный список начинается с дефиса (-), знака плюса (+) или звездочки (*), за которым следует пробел и текст элемента списка:
```
- Элемент 1
- Элемент 2
- Элемент 3
```
Упорядоченный список начинается с числа, за которым следует точка и пробел, а затем текст элемента списка:
```
1. Элемент 1
2. Элемент 2
3. Элемент 3

```
Обратите внимание, что вы можете использовать любое число для начала упорядоченного списка, а Markdown автоматически нумерует оставшиеся элементы списка.

Вы также можете вкладывать списки друг в друга, добавляя четыре пробела перед началом каждого элемента вложенного списка.
```
1. Элемент 1
2. Элемент 2
   - Подэлемент 1
   - Подэлемент 2
3. Элемент 3
```

## Работа с изображениями
Работа с изображениями в Markdown происходит путем добавления ссылок на изображения. Для вставки изображения используется следующий синтаксис:
```
![альтернативный текст](адрес_изображения "заголовок")
```

![cat](cat.png)
## Ссылки
Чтобы добавить ссылку в Markdown, нужно использовать следующий синтаксис:
```
[текст ссылки](адрес ссылки)
```
Где текст ссылки - это отображаемый текст ссылки, а адрес ссылки - это URL-адрес, на который должна вести ссылка.

Например, если вы хотите создать ссылку на страницу Google, то можете написать:
```
[Google](https://www.google.com)
```
Это превратится в гиперссылку с текстом "Google", которая ведет на страницу google.com.
## Работа с таблицаи
Для добавления таблицы можем использовать разделения

```
|...|...|
```
## Цитаты 

## Заключение
</font>

1. Создали аккаунт на GIThub
2. Создать локальный репозиторий
3. используем комманды для синхронизации
```
vscod подскажет что нужно сделать
```

4. Нужна комманда для отправки на github
```
git push
```

5. Провести изменения на другом компьютере 
6. выкачать комманда 
```
git pull
```