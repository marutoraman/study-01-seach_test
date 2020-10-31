import pandas as pd

### プログラミング初級講座１

# 検索対象
df=pd.read_csv("./source.csv")
source=list(df["name"])

while True:
    # ユーザー入力
    word=input("鬼滅の登場人物を入力　＞＞　")

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
    else:
        print("『{}』はありません".format(word))
        # 追加
        add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        if add_flg=="1":
            source.append(word)
    
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./source.csv",encoding="utf_8-sig")
    print(source)


#for s in source:
#    if "ねずこ"==s:
#        print("『ねずこ』はあります")