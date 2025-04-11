#型とは
#データの種類を表すもの
#型の種類
#数値型
 #整数型
#浮動小数点型
#文字列型
#論理型
#リスト型など
#型によってできることが違う
#同じ命令でも殻によって動作が違う

#整数型
x = 100
y = 200
z = x + y #足し算
print(z)#print(z) #300
#変数の型を調べる
print(type(x))
x_type = type(x)
print(x_type)

#文字列型
x = "100"
y = "200"
z = x + y #文字列結合 
print(z) #100200
print(type(x))
x_type = type(x)
print(x_type)