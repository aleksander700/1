"""Все шестибуквенные слова, составленные из букв Ц, В, Е, Т, О, К, записаны в алфавитном порядке и пронумерованы.
Вот начало списка:
1. BBBBBB
2. ВВВВВЕ
3. ВВВВВК
4. ВВВВВО
5. ВВВВВТ
6. ВВВВВЦ
Определите в этом списке количество слов с нечётными номерами, в записи которых не содержится ни одной из букв В, Е или К и при этом имеется ровно две буквы Т и ровно одна буква Ц.
Примечание. Слово - последовательность идущих подряд букв, не обязательно осмысленная."""
# all(word.count(x) == 0 for x in "век")
# git-scm.com/download/win
# git config --global user.name "Ваше Имя"
# git config --global user.email "ваш_email@example.com"
# word.count("в")==0 and word.count("е")== 0 and word.count("к") == 0
# Set-Service -Name ssh-agent -StartupType Automatic
# Start-Service ssh-agent
# ssh-keygen -t ed25519 -C "your_email@example.com"
# Get-Content ~/.ssh/id_ed25519.pub | clip
# ssh -T git@github.com
from itertools import *
i = 0
c = 0
for el in product(sorted('цветок'),repeat = 6):
    word =''.join(el)
    i += 1
    if i % 2 != 0 and all(word.count(x) == 0 for x in "век") and word.count('т')== 2 and word.count('ц') == 1:
        c += 1
print(c)
