class product: 
id = -1 
name = "" 
price = -1 
count = -1 

def __init__(self, id, name, price, count): 
self.id = id 
self.name = name 
self.price = int(price) 
self.count = int(count) 

def add(self, count): 
self.count += count 
return 

def buy(self, count): 
if self.count < count : 
return "0" 
else: 
self.count -= count 
return "1" 

def toString(self): 
return self.id + " " + self.name + " " + str(self.price) + " " + str(self.count) 


class shop: 
count = -1 
goodsID = {} 
goodsNAME = {} 
sales = [] 
sale = {} 

def __init__(self, gid = {}, gname = {}): 
self.goodsID = gid 
self.goodsNAME = gname 
self.count = len(self.goodsID) 

def addGood(self, pr): 
self.goodsID[pr.id] = pr 
self.goodsNAME[pr.name] = pr 
return 

def insert(self, key, how): 
if key in self.goodsNAME: 
self.goodsNAME[key].add(how) 
return "1" 
elif key in self.goodsID: 
self.goodsID[key].add(how) 
return "1" 
else: 
return "товар не найден" 

def buy(self, key, how): 
if key in self.goodsNAME: 
pr = self.goodsNAME[key] 
ans = pr.buy(how) 
if ans == "1": 
self.sale[key] = product(pr.id, pr.name, pr.price, how) 
return ans 
else: 
return ans 
elif key in self.goodsID: 
pr = self.goodsID[key] 
ans = pr.buy(how) 
if ans == "1": 
self.sale[key] = product(pr.id, pr.name, pr.price, how) 
return ans 
else: 
return ans 
else: 
return "товар не найден" 

def finishSale(self): 
self.sales.append(self.sale.copy()) 
self.sale.clear() 

def cancelSale(self): 
for el in self.sale.keys(): 
self.insert(el, self.sale[el].count) 

self.sale.clear() 


def printTable(): 
print("\n") 
for el in sh.goodsID.keys(): 
print(sh.goodsID[el].toString()) 
print("\n") 

def printSales(): 
print("\n") 
pos = 1 
for el in sh.sales: 
print(pos) 
pos += 1 
for k in el.keys(): 
print(el[k].toString()) 
print("\n") 

fin = open("in.txt") 
finSale = open("sale.txt") 

gID = {} 
gNAME = {} 


for l in fin: 
info = l.split(";") 
gID[info[0]] = product(info[0], info[1], info[2], info[3]) 
gNAME[info[1]] = product(info[0], info[1], info[2], info[3]) 

sh = shop(gID, gNAME) 

pos = 0 
sale = {} 

for line in finSale: 
if line == "-\n": 
if len(sale) > 0: 
sh.sales.append(sale.copy()) 
sale.clear() 
elif line == "-": 
if len(sale): 
sh.sales.append(sale.copy()) 
sale.clear() 
else: 
points = line.split(";") 
sale[points[0]] = product(points[0], points[1], int(points[2]), int(points[3])) 

flag = True 

while flag: 
print("1.Покупка") 
print("2.Продажа") 
print("3.Данные по продажам") 
print("0.Выход") 

ans = input("Ваш запрос : ") 
if ans == "1": 
f = True 
while f: 

printTable() 

print("0. Вернуться в главное меню") 
print("1. Сформировать продажу") 
print("2. Отменить продажу") 
print("Введите id|имя и количество через пробел") 
ans = input("Ваш запрос : ") 

if ans == "0": 
f = not(f) 
elif ans == "1": 
sh.finishSale() 
elif ans == "2": 
sh.cancelSale() 
else: 
lines = ans.split(" ") 
if len(lines) >= 2: 
ans = sh.buy(lines[0], int(lines[1])) 
if ans == "0": 
print("не хватает товара на складе") 
elif not(ans == "1"): 
print(ans) 

ans = "-1" 

elif ans == "2": 
f = True 
while f: 
print("0. Вернуться в главное меню") 
print("Введите через пробел id и количество добавляемого товара : ") 

ans = input() 
if ans == "0": 
f = not(f) 
else: 
line = ans.split(" ") 
if len(line) >= 2: 
ans = sh.insert(line[0], int(line[1])) 
if not(ans == "1"): 
ans = input("хотите ли добавить товар (да/нет) : ") 
if ans == "да": 
name = input("Имя товара : ") 
price = int(input("Цена товара : ")) 
sh.addGood(product(line[0], name, price, line[1])) 
ans = "-1" 
elif ans == "3": 
f = True 
while f: 
printSales() 
print("0. Вернуться в главное меню") 
ans = input("Введите id интересующей продажи или запрос : ") 

if ans == "0": 
f = not(f) 
elif

len(sh.sales) > int(ans) - 1: 
for el in sh.sales[int(ans) - 1].keys(): 
print(sh.sales[int(ans) - 1][el].toString()) 

elif ans == "0": 
flag = not(flag) 

fout = open("in.txt", "w") 
foutSale = open("sale.txt", "w") 

for k in sh.goodsID.keys(): 
pr = sh.goodsID[k]; 
fout.write(pr.id + ";" + pr.name + ";" + str(pr.price) + ";" + str(pr.count) + "\n") 

for el in sh.sales: 
for k in el.keys(): 
pr = el[k] 
foutSale.write(pr.id + ";" + pr.name + ";" + str(pr.price) + ";" + str(pr.count) + "\n") 
foutSale.write("-\n")