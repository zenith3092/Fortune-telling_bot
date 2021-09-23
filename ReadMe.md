#算命機器人Fortunetelling_bot

###最近事情棘手，讓你處於徬徨迷離當中嗎？

運勢、愛情、求職、事業和考試等五大方向的問題，交給易經占卜大師準沒錯！

####只要輸入所遇到的煩惱，Fortunetelling_bot 立刻就能給你占卜上的建議！
---
##操作手冊

###環境設定

本專案使用的 python 版本為3.6+
1. 安裝此專案會用到的套件
    + Pandas
	`pip install pandas`

    + Discord
	`pip install discord`

    + Requests
	`pip install requests`

2. 註冊 [卓騰語言科技](https://api.droidtown.co/login/) 帳號

	![註冊](https://imgur.com/TMq8GyE.png"markdown")

3. 登入 [卓騰語言科技](https://api.droidtown.co/login/) 網站

	![登入](https://imgur.com/Hl8YxNW.png")

---
###建立Loki專案

1. 將本資料夾 `Pull` 下來

2. 進入Loki

	![進入Loki](https://imgur.com/nIwNZLO.png")

3. 輸入專案名稱，按下建立專案

	![建立專案](https://imgur.com/MUiyEJO.png")

4. 點擊你的「專案名稱」，進入專案頁面

	![專案頁面](https://imgur.com/Vg6a9MH.png")

5. 點擊「選擇檔案」，選擇REF資料夾內的所有檔案

	![選擇檔案](https://imgur.com/FbJthRY.png")

6. 按下「讀取意圖」

	![讀取意圖](https://imgur.com/w1IXloG.png")

7. 接著可以看到五個意圖建立好了

	![意圖建好](https://imgur.com/toJRUqJ.png")

8. 點進每一個意圖，並將畫面拉到最下面，按下「生成模型」
**注意: 絕對不可按「全句分析」，否則就要重新讀取此ref檔**

	![生成模型](https://imgur.com/vgNluqx.png")

9. 將畫面往上拉，按下左上角的房子返回

	![返回](https://imgur.com/pOxpS6H.png")

10. 複製這個專案的金鑰

	![複製鑰匙](https://imgur.com/IIZEGBY.png")

11. 建立記事本檔案「account.txt」，並貼上以下內容
**注意：記得這個檔案要與「fortunetelling」及「discord_fortunetelling」在同一層資料夾**
**　　　否則程式找不到這個檔案！**
`{"username": "","loki_project_key":"","discord_token":""}`

12. 將帳號以及剛才複製的專案金鑰填入

	![填入資料](https://imgur.com/mv6z1Aa.png")

####截至目前為止就完成建立Loki專案了！

---

###在Discord上建立Fortunetelling_bot

1. 進入Discord的「[開發者頁面](https://discord.com/developers/applications/)」

2. 登入Discord帳號

	![註冊DC](https://imgur.com/49vW25R.png")

3. 點擊右上角的「New Application」

	![新APP](https://imgur.com/5tbCERs.png")

4. 輸入Application的名稱並按下「Create」

	![APP名稱](https://imgur.com/0PKDEXj.png")

5. 從左邊的SETTINGS欄位按下「Bot」後，再點擊畫面最右邊的「Add Bot」

	![建立Bot](https://imgur.com/gOZ7zbc.png")

6. 輸入Bot名稱，並「Copy」這個機器人的Token
**注意:建議名字後面可以加個「__bot」，這樣呼叫機器人的時候比較好找**

	![Bot名稱](https://imgur.com/7nBNVxT.png")

7. 將剛才複製的Token填入「account.txt」檔案

	![填入Token](https://imgur.com/H6NDjK1.png")

8. 從左邊的SETTINGS欄位按下「OAuth2」後，再從SCOPES裡面點擊「bot」，接著「Copy」連結

	![bot連結](https://imgur.com/cpcPLkQ.png")

9. 再瀏覽器貼上連結，並將機器人加入指定的伺服器

	![加入bot](https://imgur.com/FuY8CvL.png")

10. 執行「discord_fortunetelling.py」檔案

11. 開始測試機器人！

---

###測試範例

1. Tag機器人，接著輸入「hi／hello／哈囉／嗨／你好／您好／hola」來呼叫機器人

	![加入bot](https://imgur.com/6Zz5mDc.png")

2. Tag機器人，輸入自身問題讓機器人知道

	![加入bot](https://imgur.com/KS2wKGN.png")

3. Tag機器人，輸入祈禱話語後就可以將占卜結果呈現

	![加入bot](https://imgur.com/4Bl57zK.png")










