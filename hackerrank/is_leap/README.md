# Desafio: Ano Bissexto (is_leap)

## Enunciado
[write-a-function-English.pdf](https://github.com/user-attachments/files/28325986/write-a-function-English.pdf)

## Minha Explicação
Para identificar um ano bissexto, segui a lógica do calendário gregoriano. O ano é bissexto se for divisível por 4, exceto se for divisível por 100 (a menos que também seja divisível por 400).

## Código
```python
def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap
