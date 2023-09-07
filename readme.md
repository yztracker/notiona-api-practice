# Notion 自動整理文件工具

這是一個使用 Python 開發的工具，能夠從指定的網址抓取內容，並自動將其儲存到 Notion。

## 功能

- 從指定網址抓取網頁標題和內容。
- 使用 Notion API 自動將這些資訊儲存到指定的 Notion 頁面。
- 提供基本的錯誤處理功能。

## 使用方法

1. 替換 `YOUR_NOTION_API_TOKEN` 和 `YOUR_NOTION_PAGE_ID` 為你的實際資料。
2. 執行主程式：
   ```
   python main.py
   ```

3. 根據提示輸入網址，然後程式會自動抓取內容並儲存到你的 Notion 頁面。

## 如何獲得 Notion API Token 與 URL：

### 獲得 API Token：
1. 登入 Notion。
2. 點擊右上角的設定圖示（Settings & Members），選擇「整合」或「Integrations」。
3. 點擊「+ New Integration」。
4. 選擇你想要與 API 互動的 Notion 資料庫。
5. 複製界面上的 `Internal Integration Token` 作為你的 API Token。
6. 在相同的頁面下方設定整合的權限。

### 獲得 Notion 頁面 URL：
1. 打開你想要與 API 互動的 Notion 頁面或資料庫。
2. 複製網址列中的 ID 作為 Notion 頁面 ID，例如 `https://www.notion.so/Some-Page-Name-12a34b56c78d4e5e9f2g3h45j6k7l8m9` 中的 `12a34b56c78d4e5e9f2g3h45j6k7l8m9`。

## 注意事項

- 請確保你的 Notion API Token 有足夠的權限來訪問和修改指定的頁面或資料庫。
- 不要在公開場合分享你的 API Token。
- 此工具是基於 Notion 的公開 API 開發的，如果 Notion 的 API 有任何更改，可能會影響此工具的功能。
