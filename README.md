# 20251118-GH300

## 專案概述

這個專案包含兩個 TODO 網站應用程式的實作範例，分別使用不同的技術堆疊：

1. **.NET 10 MVC TODO 應用程式** - 使用 ASP.NET Core MVC 和記憶體內資料庫
2. **Python TODO 應用程式** - 使用 Python 和記憶體內資料庫

---

## 功能特色 (Features)

- ✅ 建立待辦事項 (Create TODO items)
- ✅ 檢視待辦事項列表 (View TODO list)
- ✅ 更新待辦事項 (Update TODO items)
- ✅ 刪除待辦事項 (Delete TODO items)
- ✅ 使用記憶體內資料庫，無需額外設定 (In-memory database, no additional setup required)

---

## 專案結構 (Project Structure)

```
20251118-GH300/
├── dotnet-todo/          # .NET 10 MVC TODO 應用程式
│   ├── Controllers/      # MVC 控制器
│   ├── Models/           # 資料模型
│   ├── Views/            # 視圖檔案
│   └── Program.cs        # 應用程式進入點
│
├── python-todo/          # Python TODO 應用程式
│   ├── app.py            # Flask/Django 主程式
│   ├── models.py         # 資料模型
│   ├── templates/        # HTML 模板
│   └── requirements.txt  # Python 套件依賴
│
└── README.md             # 專案說明文件
```

---

## .NET 10 MVC TODO 應用程式

### 技術堆疊 (Technology Stack)

- **框架**: ASP.NET Core MVC (.NET 10)
- **資料庫**: Entity Framework Core with In-Memory Database
- **語言**: C#
- **前端**: Razor Views, Bootstrap

### 安裝與執行 (Installation & Setup)

#### 前置需求 (Prerequisites)

- [.NET 10 SDK](https://dotnet.microsoft.com/download)
- 支援的 IDE: Visual Studio 2022, VS Code, 或 Rider

#### 執行步驟 (Steps to Run)

```bash
# 1. 進入 .NET 專案目錄
cd dotnet-todo

# 2. 還原套件
dotnet restore

# 3. 建置專案
dotnet build

# 4. 執行應用程式
dotnet run

# 5. 開啟瀏覽器訪問
# 預設網址: https://localhost:5001 或 http://localhost:5000
```

### API 端點 (API Endpoints)

- `GET /` - 首頁，顯示待辦事項列表
- `GET /Todo/Create` - 建立待辦事項表單
- `POST /Todo/Create` - 提交新增待辦事項
- `GET /Todo/Edit/{id}` - 編輯待辦事項表單
- `POST /Todo/Edit/{id}` - 提交更新待辦事項
- `POST /Todo/Delete/{id}` - 刪除待辦事項

---

## Python TODO 應用程式

### 技術堆疊 (Technology Stack)

- **框架**: Flask / Django (根據實作選擇)
- **資料庫**: SQLite In-Memory Database
- **語言**: Python 3.9+
- **前端**: Jinja2 Templates, Bootstrap

### 安裝與執行 (Installation & Setup)

#### 前置需求 (Prerequisites)

- [Python 3.9+](https://www.python.org/downloads/)
- pip (Python 套件管理工具)

#### 執行步驟 (Steps to Run)

```bash
# 1. 進入 Python 專案目錄
cd python-todo

# 2. 建立虛擬環境 (建議)
python -m venv venv

# 3. 啟動虛擬環境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. 安裝依賴套件
pip install -r requirements.txt

# 5. 執行應用程式
python app.py

# 6. 開啟瀏覽器訪問
# 預設網址: http://localhost:5000
```

### API 端點 (API Endpoints)

- `GET /` - 首頁，顯示待辦事項列表
- `POST /add` - 新增待辦事項
- `POST /update/<id>` - 更新待辦事項
- `POST /delete/<id>` - 刪除待辦事項

---

## 資料庫說明 (Database Information)

兩個應用程式都使用**記憶體內資料庫 (In-Memory Database)**：

- **優點**: 
  - 無需安裝或設定額外的資料庫系統
  - 快速啟動和測試
  - 適合開發和示範用途

- **注意事項**: 
  - 資料僅存在於應用程式執行期間
  - 應用程式重啟後，所有資料將會遺失
  - 不適合用於正式環境

Both applications use **In-Memory Database**:

- **Advantages**: 
  - No need to install or configure additional database systems
  - Fast startup and testing
  - Suitable for development and demonstration purposes

- **Notes**: 
  - Data exists only during application runtime
  - All data will be lost after application restart
  - Not suitable for production environments

---

## 開發指南 (Development Guide)

### 新增功能 (Adding Features)

兩個專案都遵循 MVC (Model-View-Controller) 架構模式：

1. **Model** - 定義資料結構和業務邏輯
2. **View** - 處理使用者介面呈現
3. **Controller** - 處理請求和回應邏輯

### 測試 (Testing)

```bash
# .NET 專案
cd dotnet-todo
dotnet test

# Python 專案
cd python-todo
pytest
```

---

## 常見問題 (FAQ)

### Q: 為什麼使用記憶體內資料庫？
A: 記憶體內資料庫適合快速原型開發和示範，無需額外的資料庫設定，方便學習和測試。

### Q: 如何將資料持久化？
A: 可以將記憶體內資料庫替換為實際的資料庫系統：
- .NET: 使用 SQL Server, PostgreSQL, 或 MySQL
- Python: 使用 SQLite (檔案模式), PostgreSQL, 或 MySQL

### Q: 這兩個實作有什麼不同？
A: 主要差異在於技術堆疊和語言，但功能相同，都實現了基本的 CRUD 操作。

---

## 貢獻指南 (Contributing)

歡迎提交問題報告、功能建議或 Pull Requests！

1. Fork 這個專案
2. 建立您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟一個 Pull Request

---

## 授權條款 (License)

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

---

## 聯絡資訊 (Contact)

如有任何問題或建議，歡迎透過 GitHub Issues 與我們聯繫。

---

## 參考資源 (Resources)

### .NET 相關
- [ASP.NET Core 官方文件](https://docs.microsoft.com/aspnet/core)
- [Entity Framework Core](https://docs.microsoft.com/ef/core)

### Python 相關
- [Flask 官方文件](https://flask.palletsprojects.com/)
- [Django 官方文件](https://docs.djangoproject.com/)

---

**最後更新**: 2025-11-18