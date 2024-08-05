team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score1 + score2
time_avg = (team1_time + team1_time) / tasks_total
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды \033[31m"Мастера кода"\033[32m!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды \033[31m"Волшебники данных"\033[32m!'
else:
    result = '\033[31mНичья'
print('\033[32m\nВ команде "Мастера кода" участников: \033[31m%s\033[32m!' % team1_num +
      '\nВ команде "Волшебники данных" участников: \033[31m%s\033[32m!' % team2_num +
      '\nИтого сегодня в командах участников: \033[31m%s \033[32mи \033[31m%s\033[32m!' % (team1_num, team2_num) +
      '\nКоманда "Волшебники данных" решила задач: \033[31m{}\033[32m!'.format(score2) +
      '\n"Волшебники данных" решили задачи за \033[31m{} с\033[32m!'.format(team2_time) +
      '\nКоманда "Мастера кода" решила задач: \033[31m{}\033[32m!'.format(score1) +
      '\n"Мастера кода" решили задачи за \033[31m{} с\033[32m!'.format(team1_time) +
      f'\nКоманды решили \033[31m{score1} \033[32mи \033[31m{score2} \033[32mзадач.' +
      f'\nВсего на соревнованиях было решено \033[31m{tasks_total} \033[32mзадач!' +
      f'\nСреднее время затраченое на решение одной задачи составило: \033[31m{time_avg:.2f} с\033[32m!' +
      f'\n\033[32m{result}')
