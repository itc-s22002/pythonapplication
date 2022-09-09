import random

import requests
from bs4 import BeautifulSoup

syu = []
s = []
alls = []
shiyo = []
shiyou = []
skill = []
skill_2 = []
skill_3 = []
item = []
item_2 = []
item_3 = []
atai = ["H", "A", "B", "C", "D", "S", "合計:"]
setumei = ["", "タイプ:", "分類:", "威力:", "ダイ:", "命中:", "PP:", "", "", "対象:", "効果:"]
# Webページを取得して解析する
# ポケモン一覧URL
load_url = "https://yakkun.com/swsh/stats_list.htm?mode=all"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

# 徹底攻略URL
load_url_2 = "https://swsh.pokedb.tokyo/pokemon/list"
html_2 = requests.get(load_url_2)
soup_2 = BeautifulSoup(html_2.content, "html.parser")

# 技一覧
load_url_3 = "https://yakkun.com/swsh/move_list.htm?mode=all"
html_3 = requests.get(load_url_3)
soup_3 = BeautifulSoup(html_3.content, "html.parser")
# 道具
load_url_4 = "https://game8.jp/pokemon-sword-shield/299351"
html_4 = requests.get(load_url_4)
soup_4 = BeautifulSoup(html_4.content, "html.parser")

# 特性

sk = []
sk_2 = []
sk_3 = []
load_url_5 = "https://yakkun.com/swsh/ability_list.htm"
html_5 = requests.get(load_url_5)
soup_5 = BeautifulSoup(html_5.content, "html.parser")

# 取得
chap2_3 = soup_3.find("tbody")
for sl in chap2_3.find_all("td"):
    skill.append(sl.text)
co = 0
for an in skill:
    skill_2.append(f"{setumei[co]} {an}")
    co += 1
    if co == 11:
        skill_2.append("-----------------------------")
        skill_3.append(skill_2)
        skill_2 = []
        co = 0

ids = soup.find(class_="table")
for sy in ids.find_all("td"):
    syu += sy.text.split()
co = 0
for i in range(len(syu)):
    s.append(syu[i])
    co += 1
    if co == 9:
        alls.append(s)
        co = 0
        s = []
namu = []
name = []
basic_st = []

for al in alls:
    namu.append(al[0])
    name.append(al[1])
    basic_st.append(al[2:])
for element in soup_2.find_all(class_="is-flex button is-light"):
    shiyo.append(element.text)
for i in range(150):
    a = shiyo[i].replace(" ", "").replace("\n", "")
    if i < 9:
        shiyou.append((a)[1:])
    elif i < 99:
        shiyou.append((a)[2:])
    else:
        shiyou.append((a)[3:])

for sl in soup_4.find_all("table"):
    item.append(sl.text.split())
co = 0
for i in item[2:15]:
    for n in range(len(i)):
        item_3.append(i[n])
        co += 1
        if co == 2:
            item_2.append(item_3)
            item_3 = []
            co = 0

chap2 = soup_5.find("table")
for sl in chap2.find_all("td"):
    sk_2.append(sl.text)

for i in range(0, len(sk_2), 2):
    sk_3.append([sk_2[i], sk_2[i + 1]])

# 種族値を取る


def syuzoku(n):
    ans = []
    ans_2 = []
    ans = [atai[i] + basic_st[n][i] for i in range(0, 7)]
    ans_2 = " ".join(ans)
    return ans_2


# 英語名を取る
def En_name(n):
    ans = int(n)
    url = f"https://pokeapi.co/api/v2/pokemon/{str(ans)}/"
    r = requests.get(url)
    r = r.json()
    name_2 = r["name"]
    name = name_2.split("-")
    return f"英語名: {name[0]}"


# 使用率を取る
def use_rate(N):
    cou = 0
    ans = "使用率: "
    ans_2 = []
    ans_3 = []
    for i in range(150):
        if shiyou[i] == rq or shiyou[i] == rq.split("(")[0]:
            ans_2.append(i + 1)
            cou += 1
    ans_3 = [str(an) + "位" for an in ans_2]
    if cou == 0:
        ans_3 = ["圏外"]
    ans += " ".join(ans_3)
    return ans


# 実数値を出す
def st_AL(N):
    kotai = [15, 15, 15, 15, 0]
    doryoku = [32, 32, 0, 0, 0]
    seikaku = [1.1, 1.0, 1.0, 0.9, 0.9]
    ans = ["実数値:", "最高 準高 無振 下降 最低"]
    ans_3 = f"{atai[0]} "
    for n in range(6):
        if n == 0:
            ans_3 = f"{atai[0]} "
            for i in range(5):
                ans_3 += (
                    (str((int(N[n]) + kotai[i] + doryoku[i]) + 60)).zfill(3)
                ) + " "
            ans.append(ans_3)
        else:
            ans_2 = f"{atai[n]} "
            for i_2 in range(5):
                ans_2 += (
                    str(
                        int(
                            ((int(N[n]) + kotai[i_2] +
                             doryoku[i_2]) + 5) * seikaku[i_2]
                        )
                    )
                ).zfill(3) + " "
            ans.append(ans_2)
    return ans


# 徹底攻略URL
def zukan(N, R):
    def forn(R):
        r_2 = R.split("(")
        ai = ""
        if 2 == len(r_2):
            r = r_2[1][:-1]
            ai = "f"
            if r == "れいじゅうフォルム" or r == "アローラのすがた" or r == "アッタクフォルム":
                ai = "a"
            elif r == "とくだいサイズ":
                ai = "k"
            elif r == "おおきいサイズ":
                ai = "l"
            elif r == "ちいさいサイズ" or r == "スピードフォルム" or r == "スピンフォルム" or r == "スカイフォルム":
                ai = "s"
            elif r == "ガラルのすがた" or r == "れきせんのゆうしゃ":
                ai = "g"
            elif r == "まいまいスタイル":
                ai = "m"
            elif r == "ぱちぱちスタイル":
                ai = "p"
            elif r == "カットロトム":
                ai = "c"
            elif r == "オリジンフォルム":
                ai = "o"
            elif r == "ときはなたれしフーパ":
                ai = "u"
            elif r == "れんげきのかた":
                ai = "r"
            elif r == "ヒートロトム":
                ai = "h"
            elif r == "ホワイトキュレム" or r == "はくばじょうのすがた" or r == "ウォッシュロトム":
                ai = "w"
            elif r == "ブラックキュレム" or r == "こくばじょうのすがた" or r == "ブレードフォルム":
                ai = "b"
            elif r == "たそがれのすがた" or r == "ゴミのミノ" or r == "ディフェンスフォルム":
                ai = "d"
        if 3 == len(r_2):
            r = r_2[1]
            if r == "たそがれのたてがみ":
                ai = "s"
            elif r == "あかつきのつばさ":
                ai = "m"
            else:
                ai = "h"
        if R[-1] == "X":
            ai = "x"
        elif R[-1] == "Y":
            ai = "y"
        elif R[0:2] == "メガ":
            ai = "m"
        if R[0:3] == "ゲンシ":
            ai = "p"
        return ai

    if int(N) < 808 and forn(R) != "g" and forn(R) != "h":
        nu = "sm"
    else:
        nu = "swsh"

    return f"https://yakkun.com/{nu}/zukan/n{N}{forn(R)}"


# 徹底攻略URL解析
def get_url(N, R):
    load_url = zukan(N, R)
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    ans = []
    ans_2 = []
    ids = soup.find(class_="type")
    for element in ids.find_all("img"):
        ans.append((str(element).split())[1][5:-1])
    ans_2.append(ans)
    ans = []
    for element in soup.find_all(class_="c1"):
        ans.append(element.find("a"))
    ans = ans[:39]
    ans = [x.text for x in ans if x]
    ans_2.append(ans)
    return ans_2


# タイプと特性を取る
def types(N, R):
    ans = []
    for n in range(2):
        if 0 == n:
            for i, al in enumerate(get_url(N, R)[n]):
                ans.append(f"タイプ{i + 1}: " + al)
        else:
            for i, an in enumerate(get_url(N, R)[n]):
                if an[0] == "*":
                    ans.append("夢特性: " + an)
                else:
                    ans.append("特性: " + an)
    return ans


# メインループ
while True:
    if (rq := input("名前入力:")) == "q":
        break
    # Gameのループ
    elif rq == "?":
        q = random.randint(0, len(namu))
        print(
            "\n".join(
                [
                    f"種族値:{syuzoku(q)}",
                    "\n".join(types(namu[q], name[q])),
                    "------------------------------",
                ]
            )
        )
        while True:
            if (rq := input("だーれだ？:")) == name[q]:
                print("正解")
                break
            elif rq == "ans":
                print(f"答えは {name[q]} \n -----------------------------")
                break
    # ポケモン出力
    for n in range(len(namu)):
        if rq == name[n]:
            print(
                "\n".join(
                    [
                        En_name(namu[n]),
                        f"図鑑番号: {namu[n]}",
                        use_rate(rq),
                        "\n".join(types(namu[n], name[n])),
                        f"種族値: {syuzoku(n)}",
                        "\n".join(st_AL(basic_st[n])),
                        "------------------------------",
                    ]
                )
            )
    # 技出力
    for i in range(len(skill_3)):
        if rq == skill_3[i][0].replace(" ", ""):
            print("\n".join(skill_3[i][1:]))
    # 道具出力
    for i in range(len(item_2)):
        if rq == item_2[i][0]:
            print(f"効果: {item_2[i][1]} \n -----------------------------")
    for i in range(len(sk_3)):
        if rq == sk_3[i][0]:
            print(f"効果: {sk_3[i][1]} \n -----------------------------")
