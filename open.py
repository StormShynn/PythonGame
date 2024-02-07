import os 
try:
  import gspread
except:
  os.system('pip install gspread')
os.system('python Main.py' if os.name == "nt" else 'python3 Main.py') 