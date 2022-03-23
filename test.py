import sqlite3

# -- Conection --
conn = sqlite3.connect('datatest.db')
cur = conn.cursor()

# -- Check Access -- --
user_id = 153983953
result = cur.execute("SELECT status FROM users WHERE user_id = ?", (user_id,)).fetchone()
 
if result[0] == 0:
	print("You haven't access")
elif result[0] == 1:
	print("You have access, but only for teachers")
elif result[0] == 2:
	print("Admin, how can i help you?")

# -- Check Teacher -- 
name = 'Эмиль'
nameResult = cur.execute("SELECT * FROM employees WHERE name = ?", (name,)).fetchall()
print(nameResult)

if nameResult:
	for x in nameResult:
		print(f'''Employee: {x[0]} {x[1]} \nData: {x[2]} {x[3]} \nRole: {x[4]}\n''')
elif not nameResult:
	print("Сотрудник не найден")

# --- Full ---
if user_id in database.db and prefix == 1:
	name = input("Введите имя: ")
	result = cur.execute("SELECT * FROM employees WHERE name = ?", (name,)).fetchall()

	if result:
		for x in result:
			if x[4] == "Директор":
				print(f'''Employee: {x[0]} {x[1]} \nData: "You haven't Access" \nRole: {x[4]}\n''')

			elif [4] == "Завуч":
				print(f'''Employee: {x[0]} {x[1]} \nData: "You haven't Access" \nRole: {x[4]}\n''')

			else:
				print(f'''Employee: {x[0]} {x[1]} \nData: {x[2]} {x[3]} \nRole: {x[4]}\n''')

	elif not result:
		print("Сотрудник не найден")


elif user_id in database.db and prefix == 2:
	name = ("Введите имя: ")
	result = cur.execute("SELECT * FROM employees WHERE name = ?", (name,)).fetchall()

	if result:
		for x in result:
			print(f'''Employee: {x[0]} {x[1]} \nData: {x[2]} {x[3]} \nRole: {x[4]}\n''')

	elif not result:
		print("Сотрудник не найден")


else:
	print("You banned in bot, or you dont finish registration")