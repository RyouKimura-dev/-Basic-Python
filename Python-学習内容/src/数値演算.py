#数値演算
#丸括弧を付けて計算の優先順位を変えることができる
print(1 + 2 * 3) #7 
print((1 + 2) * 3) #9
print(1 + 2 * 3 - 4) #3
#割り算の場合は、0で割るとエラーになる
#print(1 / 0) #エラーになる
#割り算の結果は浮動小数点型になる

x = 10
y = 30
z = x + y
print(z)
#変数の値を変更することができる

math = 82
japanese = 74
english =60
avg_score = ( math + japanese + english ) / 3
print(avg_score)
avg_score_tyoe = type(avg_score)
print(avg_score_tyoe) #<class 'float'>
#変数の型を確認することができる