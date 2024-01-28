# [IMPORT]
import os
import sys
import random
import string
import System
import gspread
import secrets
import datetime
from time import sleep
from threading import Thread
from Menu import Smenu, Sregister, Slogin, Sbanner, SchangePwd, SchangeCoin, Scoinmining, Scharts, SXs, SchangeCoin1, SchangeCoin2, SXs1, SXs2
# [CODE]
print(" Vui Lòng Đợi Đang Tải Dữ Liệu Từ Sever !!")
def Exit():
	os.sys.exit()
def Enter():
	a = input(" Enter để tiếp tục")
def Clear():
	os.system("cls" if os.name == "nt" else "clear")
def Crossbar():
	for i in range(13):
		sys.stdout.write("▂▂▂▂")
	sys.stdout.write("\n")
def Loading(I):
	frames = ["\r[-->     ]", "\r[ -->    ]",
	"\r[  -->   ]", "\r[   -->  ]",
	"\r[    --> ]", "\r[     -->]"]
	for i in range(I, 0, -1):
		for frame in frames:
			sys.stdout.write(frame + str(i))
			sleep(0.125)
	sys.stdout.write(frames[-1])
	Clear()
def Space(Number):
	Space = ""
	for i in range(Number):
		Space += " " * i
	return Space

def MENU():
	Clear()
	Smenu()
	select = input("CHỌN CHẾ ĐỘ: ")
	if select.isdigit():
		option = int(select)
		actions = {
		0: os.sys.exit,
		1: lambda: Register(),
		2: lambda: Login(),
		3: lambda: BXH(0),
		9: lambda: ChangeCoin()
		}
		if option in actions:
			actions[option]()
		else:
			print(f" Lựa Chọn Không Hợp Lệ !")
			sleep(2); MENU()
	else:
		print(f" Vui Lòng Nhập Số !")
		sleep(2); MENU()
		
def Login():
	Clear()
	Slogin()
	username = input("Account: ")
	if username.strip() == "":
		print(f"{Space(2)}Error !")
		print(f"{Space(2)}Auto exit enabled")
		Loading()
		Clear()
		os.sys.exit()
	password = input("Password: ")
	id = System.CheckLogin(username, password)
	if (id == 0):
		print(" Đăng Nhập Thất Bại !")
		sleep(2); MENU()
	print(" Login Success !")
	id -= 1
	MenuMain(id)
		
def Register():
	def User():
		Sregister()
		user = input("Account Name: ")
		if (len(user) < 3):
			print(" Tên Quá Ngắn !")
			Loading(3)
			User()
		elif (len(user) > 10):
			print(" Tên Quá Dài !")
			Loading(3)
			User()
		ID = System.CheckUser(user)
		if (ID == 0):
			print(" Tên đã được sử dụng !")
			Loading(3)
			User()
		if (ID == 1):
			return user
	def Password(user):
		Sregister()
		print(f"Account Name: {user}")
		pwd = input("Enter Password: ")
		if (len(pwd) < 3):
			print("Pass Quá Ngắn !")
			Loading(3)
			Password(user)
		elif (len(pwd) > 10):
			print("Pass Quá Dài !")
			Loading(3)
			Password(user)
		return pwd
	Clear()
	user = User()
	pwd = Password(user)
	System.SaveData(user, pwd)
	
def ChangeCoin():
	def Coin():
		Clear()
		SchangeCoin2()
		pwd = input(" Nhập Mật Khẩu: ")
		if (pwd != '12345'):
			MENU()
		id = input(" ID: ")
		Check = System.CheckID(id)
		if (Check == 0):
			print(" User not exists !!")
			Loading(3)
			ChangeCoin()
		print(f" User: {Check}")
		Continue = input(" Continue(y/n): ")
		if (Continue.lower() == 'y'):
			coin = input(" Coin: ")
			System.CoinRepair(coin, id)
		else:
			Loading(2)
			ChangeCoin()
	def List():
		Clear()
		SchangeCoin1()
		System.ListOfAccount()
		Continue = input("\n Continue: ")
		Loading(3)
		ChangeCoin()
	Clear()
	SchangeCoin()
	select = input("CHỌN CHẾ ĐỘ: ")
	if select.isdigit():
		option = int(select)
		actions = {
		0: lambda: MENU(),
		1: lambda: List(),
		2: lambda: Coin(),
		}
		if option in actions:
			actions[option]()
		else:
			print(f" Lựa Chọn Không Hợp Lệ !")
			sleep(2); ChangeCoin()
	else:
		print(f" Vui Lòng Nhập Số !")
		sleep(2); ChangeCoin()
		
def MenuMain(id):
	Clear()
	Sbanner()
	user, coin = System.LoadDataUser(id)
	print(f" User: {user}          Coin: {coin} Xu")
	select = input("CHỌN CHẾ ĐỘ: ")
	if select.isdigit():
		option = int(select)
		actions = {
		0: lambda: Exit(),
		1: lambda: XS(id),
		2: lambda: CoinMining(id),
		3: lambda: BXH(id),
		4: lambda: Exit()
		}
		if option in actions:
			actions[option]()
		else:
			print(f" Lựa Chọn Không Hợp Lệ !")
			sleep(2); MenuMain(id)
	else:
		print(f" Vui Lòng Nhập Số !")
		sleep(2); MenuMain(id)
def XS(id):
	Clear()
	def Check(id):
		SXs1()
		user, coin = System.LoadDataUser(id)
		coin = System.LoadDataCoin(id)
		if (coin < 0 or coin == 0):
			print(" Không đủ xu !")
			Loading(3)
			MenuMain(id)
		print(f" User: {user}          Coin: {coin} Xu")
		select = input("CHỌN: ")
		if select.isdigit():
			select = int(select)
			if (select == 1):
				return 1 #Chan
			elif (select == 2):
				return 2 #Le
			else:
				print(f" Lựa Chọn Không Hợp Lệ !")
				sleep(2); XS(id)
		else:
			print(f" Vui Lòng Nhập Số !")
			sleep(2); XS(id)
	def Function(i):
		#i = 1 70chan 30le
		#i = 2 70le 30chan
		percentage_even = 0.7
		total_elements=100
		if i == 1:
			even_count = int(total_elements * percentage_even)
			odd_count = total_elements - even_count
		elif i == 2:
			odd_count = int(total_elements * percentage_even)
			even_count = total_elements - odd_count
		odd_numbers = [random.randrange(1, 99, 2) for _ in range(odd_count)]
		even_numbers = [random.randrange(2, 99, 2) for _ in range(even_count)]
		result_list = odd_numbers + even_numbers
		random.shuffle(result_list)
		return random.choice(result_list)
	def CoinBet(id, select):
		Clear()
		SXs2()
		select = int(select)
		user, coin = System.LoadDataUser(id)
		print(f" User: {user}          Coin: {coin} Xu")
		if (select == 1):
			title = f"Chẳn"
		else:
			title = f"Lẻ"
		print(f" Chọn : {title}")
		Bet = input(" Bet: ")
		if Bet.isdigit():
			Bet = int(Bet)
			coin = System.LoadDataCoin(id)
			if (Bet > coin or Bet < 0 or Bet == 0):
				print(" Cược Sai !!")
				Loading(2)
				CoinBet(id, select)
			else:
				return Bet
		else:
			print(f" Vui Lòng Nhập Số !")
			Loading(2); CoinBet(id, select)
	def Spin(id, num):
		crossbar1 = "\n    ╔══════════╗"
		crossbar2 = "\n    ╚══════════╝\n"
		delay = 0.002
		print(crossbar1)
		while delay < 0.1:
			num = (num % 98) + 1 
			sys.stdout.write(f"\r    ║ -> {num:02d} <- ║")
			sys.stdout.flush()  
			sleep(delay)
			delay += 0.001
		print(crossbar2)
	def Reward(id, Se, Be, Nu):
		TitleWin = f" Chúc mừng chiến thắng !"
		TitleLose = f" Chúc may mắn lần sau !"
		if (Se == 1 and Nu % 2 == 0):
			print(TitleWin)
			System.CoinRepair(Be, id)
			print(f"Coin: +{Be} Xu\n")
		elif (Se == 0 and Nu % 2 != 0):
			print(TitleWin)
			System.CoinRepair(Be, id)
			print(f"Coin: +{Be} Xu\n")
		elif (Se == 1 and Nu % 2 != 0):
			print(TitleLose)
			System.CoinRepair(-Be, id)
			print(f"Coin: -{Be} Xu\n")
		elif (Se == 0 and Nu % 2 == 0):
			print(TitleLose)
			System.CoinRepair(-Be, id)
			print(f"Coin: -{Be} Xu\n")
	select = Check(id)
	Bet = CoinBet(id, select)
	num = Function(select)
	Spin(id, num)
	Reward(id, select, Bet, num)
	input("Cotinue;")
	MenuMain(id)

def CoinMining(id):
	Clear()
	Scoinmining()
	user, coin = System.LoadDataUser(id)
	print(f" User: {user}          Coin: {coin} Xu")
	blocks = input(f" Nhập Số Block Đào: ")
	coinlist = [200, 400, 600,
							800, 1000, 1200,
							1400, 1600, 1800,
							2000, 2200, 2400]
	if blocks.isdigit():
		for i in range(int(blocks)):
			blockchain = random.randint(10, 50)
			nimed = 0
			difficulty = random.randint(3000, 3500)
			A = blockchain * difficulty
			for _ in range(A):
				nimed += 1 
				sys.stdout.write(f"\r[{i}] Mine: {nimed:07d}")
				sleep(0)
			mined_coin = random.choice(coinlist)
			System.CoinRepair(mined_coin, id)
			user, coin = System.LoadDataUser(id)
			unit = "Xu" if mined_coin >= 1000 else " Xu"
			print(f"\n[{i}] +{mined_coin} {unit} | Tổng: {coin} Xu\n")
		Loading(5)
		MenuMain(id)
	elif blocks.lower() == 'n':
		MenuMain(id)
	else:
		print(f" Vui Lòng Nhập Số !!")
		Loading(3)
		CoinMining(id)

def BXH(id):
	User, user, Coin, coin = System.Charts(id)
	Scharts(1, User, Coin)
	Scharts(2, user, coin)
	Enter()
	if (id == 0):
		MENU()
	else:
		MenuMain(id)

Clear()
MENU()
