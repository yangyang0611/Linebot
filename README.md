# Line 馬來西亞GOGO

## 前言
人們都喜歡趁著假期到處旅游。在搜索國外度假勝地時，常常會根據自己的興趣偏好挑選地點。作者在台灣念書的這幾年，常常會被同學詢問關於本國的旅游推薦。因此，想設計一個lineChatBot包含本地人推薦的馬來西亞隱藏好玩景點及旅游指南。當中也包括介紹馬來西亞三大種族的重大節日，讓外國人通過這個LineBot更加深入的瞭解大馬文化！

## 構想
先藉由使用者輸入想瞭解的主題（旅游景點/節日），引導到不同的方向。旅游景點會列出幾個不同類型的度假勝地，供使用者挑選。再根據挑選地點列出景點介紹與門票規定作爲參考。節日則會列出馬來西亞主要3大種族（華人，馬來人，印度人）的慶祝節日，再根據不同種族介紹各自的節日由來，以及文化背景和對應節日時會食用的傳統食物。

## 環境
- windows
- python 3.9.0

## 使用說明
- 基本操作
    - 所有操作都是使用按鈕來進行
    - 如果使用者輸入除了按鈕以外的字，便會出現`回到Menu`的選項
    - 如果在現階段輸入上階段的指令，也會出現`回到Menu`的選項

- 架構圖
    1. 從`menu`開始使用馬來西亞gogo
    2. 輸入主題 -> `景點`/`節日`
    3. 以下分成`景點`與`節日`來加以説明
    
- `景點` 
    - `游樂園`
        - `雲頂高原`
            - 文字介紹
            - 文字説明門票與規定
            - 相關的youtube影片
        - `樂高主題樂園`
			- 文字介紹
            - 文字説明門票與規定
            - 相關的youtube影片
    - `歷史古跡`
        - `法摩沙堡`
            - 文字介紹
            - 文字説明門票與規定
            - 相關的youtube影片
        - `凱莉古堡`
			- 文字介紹
            - 文字説明門票與規定
            - 相關的youtube影片
- `節日`
    - `華人`
        - `農曆新年`
            - 文字敘述由來
            - 文字列出食物
        - `端午節`
            - 文字敘述由來
            - 文字列出食物
    - `馬來人`
        - `哈芝節`
            - 文字敘述由來
            - 文字列出食物
        - `開齋節`
            - 文字敘述由來
            - 文字列出食物
	- `印度人`
        - `屠妖節`
            - 文字敘述由來
            - 文字列出食物
        - `大寶森節`
            - 文字敘述由來
            - 文字列出食物

## 使用示範
### 輸入想瞭解的主題
![](https://i.imgur.com/RAXRooY.jpg)
![](https://i.imgur.com/3VkDy82.jpg)
![](https://i.imgur.com/JhK01qT.jpg)
![](https://i.imgur.com/OCsoSBk.jpg)
### 景點
![](https://i.imgur.com/OodsURE.jpg)
![](https://i.imgur.com/95lZAGO.jpg)
![](https://i.imgur.com/DOj8yEs.jpg)
![](https://i.imgur.com/bgeHzOf.jpg)
![](https://i.imgur.com/R2vy5FN.jpg)
![](https://i.imgur.com/TfHJx3t.jpg)
![](https://i.imgur.com/6ZEIZzI.jpg)
![](https://i.imgur.com/2iNuLe8.jpg)
### 節日
![](https://i.imgur.com/Aej3bXd.jpg)
![](https://i.imgur.com/shzYGJD.jpg)
![](https://i.imgur.com/nxUfsPP.jpg)
![](https://i.imgur.com/pvibAF1.jpg)
![](https://i.imgur.com/xqbqg5A.jpg)
![](https://i.imgur.com/hsoAJeE.jpg)
![](https://i.imgur.com/7KyAzOK.jpg)
### 隨時畫FSM
![](https://i.imgur.com/kk8b9aa.jpg)


## FSM
![](https://i.imgur.com/GMrkfDT.png)
### state說明
- user: 一開始會出現`Menu`做選擇
- Menu: 輸入`景點`或`節日`
- place: 列出不同類型的旅游景點`游樂園`和`歷史古跡`
- themepark: 輸入先瞭解的游樂園`雲頂高原`或`樂高主題樂園`
- genting: 輸入想瞭解`雲頂高原`的`介紹`，`門票及規定`或`影片`
- logoland: 輸入想瞭解`樂高主題樂園`的`介紹`或`門票及規定`或`影片`
- historical: 輸入先瞭解的歷史建築`法摩沙堡`或`凱莉古堡`
- famosa: 輸入想瞭解`雲頂高原`的`介紹`，`門票及規定`或`影片`
- Kcastle: 輸入想瞭解`雲頂高原`的`介紹`，`門票及規定`或`影片`

- festival: 列出3大種族的節日`華人`、`馬來人`、`印度人`
- chinese: 輸入想瞭解`華人`的`農曆新年`或`端午節`
- new_year：輸入想瞭解`農曆新年`的`由來`或`傳統食物`
- dragon_boat：輸入想瞭解`端午節`的`由來`或`傳統食物`
- malay: 輸入想瞭解`馬來人`的`哈芝節`或`開齋節`
- haji：輸入想瞭解`哈芝節`的`由來`或`傳統食物`
- raya：輸入想瞭解`開齋節`的`由來`或`傳統食物`
- indian: 輸入想瞭解`印度人`的`屠妖節`或`大寶森節`
- deepa：輸入想瞭解`屠妖節`的`由來`或`傳統食物`
- thai：輸入想瞭解`大寶森節`的`由來`或`傳統食物`