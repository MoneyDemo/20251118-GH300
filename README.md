# TODO Website - Python with In-Memory Database

一個使用 Python Flask 框架建立的待辦事項網站，使用 In-Memory 資料庫儲存資料。

## 功能特點

- ✅ 新增待辦事項（含標題和描述）
- ✅ 顯示所有待辦事項
- ✅ 標記待辦事項為完成/未完成
- ✅ 編輯待辦事項
- ✅ 刪除待辦事項
- ✅ 統計顯示（總數、待完成、已完成）
- ✅ RESTful API 設計
- ✅ 響應式設計，支援手機和桌面

## 技術架構

- **後端**: Python 3.x + Flask
- **前端**: HTML5 + CSS3 + Vanilla JavaScript
- **資料庫**: In-Memory (Python List)
- **API**: RESTful API

## 安裝步驟

1. 確保已安裝 Python 3.7 或以上版本

2. 安裝相依套件：
```bash
pip install -r requirements.txt
```

3. 執行應用程式：
```bash
python app.py
```

4. 開啟瀏覽器訪問：
```
http://localhost:5000
```

## API 端點

### 獲取所有待辦事項
```
GET /api/todos
```

### 創建新待辦事項
```
POST /api/todos
Content-Type: application/json

{
    "title": "待辦事項標題",
    "description": "待辦事項描述（選填）"
}
```

### 獲取單個待辦事項
```
GET /api/todos/{id}
```

### 更新待辦事項
```
PUT /api/todos/{id}
Content-Type: application/json

{
    "title": "新標題",
    "description": "新描述",
    "completed": true
}
```

### 刪除待辦事項
```
DELETE /api/todos/{id}
```

### 切換完成狀態
```
POST /api/todos/{id}/toggle
```

## 專案結構

```
.
├── app.py              # Flask 應用程式主檔案
├── requirements.txt    # Python 相依套件清單
├── static/
│   └── style.css      # CSS 樣式檔案
└── templates/
    └── index.html     # HTML 模板檔案
```

## 注意事項

- 本專案使用 In-Memory 資料庫，應用程式重啟後資料會遺失
- 適用於開發、測試或展示用途
- 如需持久化儲存，請考慮使用 SQLite、PostgreSQL 或其他資料庫