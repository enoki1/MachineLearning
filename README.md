# MachineLearning
-------

# Алгоритм Нидлмана-Вунша.
    
    Есть две последовательности, надо провести выравнивание. Для этого динамикой заполняется таблица n x m, где n,m - длины последовательностей. 
    Таблица заполняется таким образом что на каждой итерации выбирается минимум из предложенных действий(удаление, вставка, замена).
    В ячейке (n+1)(m+1) хранится ответ - Расстояние Левенштейна. Для поиска действий для выравнивания я прошелся обратно запоминая какие действия выбирал во время минимизирования
    
    Для последовательностей длиной >10^5 я получал ответ в течении 16-17 минут(скрин не сохранил), что очень долго. Скорее всего не стоило запоминать всю таблицу
    размером 10^5 на 10^5, это слишком много, но тогда я не смогу определить какие действия для выравнивания совершал.
    Вот как выглядит вывод для произвольных последовательностей(V - вставка, Z - замена, U - удаление)
![Image alt](images/Nidl.png)    