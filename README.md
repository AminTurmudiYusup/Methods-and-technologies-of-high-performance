# Высокопроизводительные методы и технологии
**A. Информация о моей ОС**


![overcommit_1](https://github.com/user-attachments/assets/0a407f2d-5030-44fd-b245-ce9dc7423f05)


**B. Создание программы на языке C++ для вычисления матричного выражения**


   1. Включает библиотеки

![matrix1](https://github.com/user-attachments/assets/0ea4e8e7-28c4-4219-9309-1b60c56cac4c)

    
   2. создать функцию для вычисления матрицы

![matrix2](https://github.com/user-attachments/assets/1b003d01-b2bc-49ea-b582-92edd6093e4c)


   3. определить размер матрицы

![matrix3](https://github.com/user-attachments/assets/01196161-454a-4f02-91cb-757f5b746e77)


   4.  определить размер нити


![matrix4](https://github.com/user-attachments/assets/98de0c0e-8ff7-44bf-961b-df3056d437a4)

    

**C. Создать программу python для анализа результата.**

![matrix5](https://github.com/user-attachments/assets/f8433eda-cbaa-420b-8001-13e7e9ed9da8)


**D. Создать скрипт bash для компиляции, запустить программу C++ и запустить программу python для анализа влияния программ, работающих параллельно. (используя thread open mp)**

![matrix6](https://github.com/user-attachments/assets/df64bf3d-1fa5-45b7-a67c-ef1c63882ed6)


**E. Как запустить программу**

![matrix7](https://github.com/user-attachments/assets/e13a0b72-dd91-48af-a833-b3ecab10f192)


**F. Тестирование с потоками**
   1. Размеры матриц: программа тестирует размеры матриц 500x500, 700x700 и 1000x1000.
   2. Количество потоков: программа тестирует с 1, 2, 4 и 8 потоками.
   3. Цикл повторяется по каждой комбинации размера матрицы и количества потоков.

![matrix8](https://github.com/user-attachments/assets/df0e61a6-3644-4f35-b1fa-eb0a3f9cba54)




**G. Анализ производительности и визуализация параллелизма**
 
  
  ** время выполнения против потоков **
  
  1. время_выполнения_против_потоков_500

![execution_time_vs_threads_500](https://github.com/user-attachments/assets/162520d8-67f0-4e34-95a1-c2be3704e850)


  2. execution_time_vs_threads_700
 
![execution_time_vs_threads_700](https://github.com/user-attachments/assets/05f74113-115f-4900-94a1-b7b1e94905b2)

  
  3. execution_time_vs_threads_1000
     
![execution_time_vs_threads_1000](https://github.com/user-attachments/assets/89596acc-44cd-4037-91ab-ecdd3db9cabd)


  ** ускорение против потоков **

  1. ускорение_против_потоков_500

![speedup_vs_threads_500](https://github.com/user-attachments/assets/d6644a3e-a797-4fb5-9402-6031fb1f41cb)


  2. ускорение_против_потоков_700

![speedup_vs_threads_700](https://github.com/user-attachments/assets/33af468b-58c0-48ee-93de-6ebbf7d3933b)


  3. ускорение_против_потоков_1000

![speedup_vs_threads_1000](https://github.com/user-attachments/assets/1176d571-2d62-43ed-8669-45cc86d5d47d)



**H. Заключение**

**Влияние количества потоков на время выполнения**


1 поток: время выполнения значительно увеличивается с ростом размера матрицы.


2 потока: лишь немного лучше, чем 1 поток для небольших матриц, но значительно лучше для больших матриц.


4 потока: время выполнения продолжает уменьшаться, что свидетельствует об эффективном использовании ресурсов.


8 потоков: выигрыш уменьшается из-за накладных расходов и закона Амдаля.


**Закон Амдаля**
Ограничение параллельного ускорения: даже при 8 потоках ускорение останавливается из-за:


Последовательных частей программы.


Накладных расходов на управление потоками.
