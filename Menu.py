# [IMPORT]
import sys
# [CODE]
def Crossbar():
	for i in range(12):
		sys.stdout.write("▂▂▂▂")
# [MENU CODE]
def Smenu():
	menu = """
	╔═══════════════════╗
	║1.Register   3.BXH ║
	║2.Login      0.EXIT║
	╚═══════════════════╝
	"""
	print(menu)
	Crossbar()
	
def Sregister():
	register= """
	╔═══════════════════╗
	║      Register     ║
	║                   ║
	╚═══════════════════╝
	"""
	print(register)
	Crossbar()
	
def Slogin():
	login= """
	╔═══════════════════╗
	║       Login       ║
	║                   ║
	╚═══════════════════╝
	"""
	print(login)
	Crossbar()
	
def SchangePwd():
	change_password= """
	╔═══════════════════╗
	║  Change Password  ║
	║                   ║
	╚═══════════════════╝
	"""
	print(change_password)
	Crossbar()

def SchangeCoin():
	change_coin= """
	╔═══════════════════╗
	║    Change Coin    ║
	║ 1.List     2.Coin ║
	╚═══════════════════╝
	"""
	print(change_coin)
	Crossbar()

def SchangeCoin1():
	change_coin= """
	╔═══════════════════╗
	║       List        ║
	║                   ║
	╚═══════════════════╝
	"""
	print(change_coin)
	Crossbar()
	
def SchangeCoin2():
	change_coin= """
	╔═══════════════════╗
	║       Coin        ║
	║                   ║
	╚═══════════════════╝
	"""
	print(change_coin)
	Crossbar()
def Sbanner():
	banner= """
	╔════════════════════════════════════════╗
	║               Mini Game                ║
	║ 1.XỔ SỐ            3.BXH             ║
	║ 2.COIN MINING        4.Change Password ║
	║                      0.EXIT            ║
	╚════════════════════════════════════════╝
	"""
	print(banner)
	Crossbar()
	
def SXs():
	xs= """
	╔═══════════════════╗
	║      Xổ Số      ║
	║                   ║
	╚═══════════════════╝
	"""
	print(xs)
	Crossbar()
	
def SXs1():
	xs= """
	╔═══════════════════╗
	║ 1.Chẵn           ║
	║             2.Lẻ ║
	╚═══════════════════╝
	"""
	print(xs)
	Crossbar()

def SXs2():
	xs= """
	╔═══════════════════╗
	║        Bet        ║
	║                   ║
	╚═══════════════════╝
	"""
	print(xs)
	Crossbar()
	
def Scoinmining():
	coin= """
	╔═════════════════════════╗
	║       Coin Mining       ║
	║     Have a nice day !!  ║ 
	╚═════════════════════════╝
	"""
	print(coin)
	Crossbar()
	
def Scharts(top, user, coin):
	charts = f"""
	╔════════════════════════╗
	║			 Top {top}         ║
	║ User: {user}
	║ Coin: {coin} Xu
	╚════════════════════════╝
	"""
	print(charts)
