'''Tapşırıq 2 (Dövrlər - For Loop): 
1-dən 20-yə qədər olan bütün ədədləri ekrana çap edən bir for dövrü yaz.
 Amma kiçik bir oyun qat: Əgər ədəd 5-ə tam bölünürsə, ədədin özünü yox, ekrana "BİNGO!" sözünü yazdırsın.'''

for i in range (1,21):
    if i % 5 == 0:
        print("Bingo")
        
    else:
        print(i)