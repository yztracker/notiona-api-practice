import requests
from bs4 import BeautifulSoup
from notion_client import Client

# 抓取網頁資料
def fetch_data_from_url(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        return soup
    except requests.RequestException as e:
        print(f"網頁載入失敗：{e}")
        return None

# 將資料儲存到 Notion
def send_data_to_notion(data, token, notion_page_id):
    if not data:
        print("無資料可儲存到 Notion")
        return
    
    try:
        notion = Client(auth=token)
        
        # 抓取網頁的標題和內容
        title = data.title.string
        content = data.body.get_text()

        # 更新 Notion 頁面標題
        notion.pages.update(page_id=notion_page_id, properties={"title": [{"text": {"content": title}}]})
        
        # 將內容分割成多個小於 2000 個字符的段落
        chunks = [content[i:i+1998] for i in range(0, len(content), 1998)]

        # 為每個段落新增一個區塊
        for chunk in chunks:
            notion.blocks.children.append(notion_page_id, children=[{
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": chunk}}]
                }
            }])
    except Exception as e:
        print(f"儲存到 Notion 失敗：{e}")

def main():
    url = input("請輸入網址：")
    data = fetch_data_from_url(url)

    # 替換以下的值
    token = "secret_6n2vtiHqRLMkP6QR5M2tjWivNZubroCDhnaPjq1uGQy"
    notion_page_url = "57b9b1d53abc42eda2133eb335a04a3f"
    
    send_data_to_notion(data, token, notion_page_url)

# 執行
if __name__ == "__main__":
    main()
