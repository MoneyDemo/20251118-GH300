# TodoApp - .NET 10 MVC TODO 網站

使用 .NET 10 MVC 架構建立的 TODO 管理網站，採用 Entity Framework Core In-Memory 資料庫。

## 功能特色

- ✅ **新增待辦事項** - 建立新的 TODO 項目
- ✏️ **編輯待辦事項** - 修改現有的 TODO 項目
- ✔️ **標記完成/取消完成** - 快速切換項目的完成狀態
- 🗑️ **刪除待辦事項** - 移除不需要的項目
- 📊 **統計資訊** - 顯示總計、已完成和待處理的項目數量

## 技術架構

- **框架**: ASP.NET Core MVC (.NET 10)
- **資料庫**: Entity Framework Core In-Memory Database
- **前端**: Bootstrap 5, jQuery
- **架構模式**: MVC (Model-View-Controller)

## 系統需求

- .NET 10 SDK

## 如何執行

1. 克隆專案
```bash
git clone https://github.com/lettucebo/20251118-GH300.git
cd 20251118-GH300
```

2. 執行應用程式
```bash
dotnet run
```

3. 開啟瀏覽器訪問
```
http://localhost:5000
```

或使用 HTTPS:
```
https://localhost:5001
```

## 專案結構

```
TodoApp/
├── Controllers/
│   ├── TodoController.cs    # TODO CRUD 操作控制器
│   └── HomeController.cs    # 預設首頁控制器
├── Models/
│   └── TodoItem.cs          # TODO 資料模型
├── Data/
│   └── ApplicationDbContext.cs  # EF Core 資料庫上下文
├── Views/
│   ├── Todo/
│   │   ├── Index.cshtml     # TODO 列表頁面
│   │   ├── Create.cshtml    # 新增 TODO 頁面
│   │   └── Edit.cshtml      # 編輯 TODO 頁面
│   └── Shared/
│       └── _Layout.cshtml   # 共用版面配置
└── Program.cs               # 應用程式進入點
```

## 資料模型

### TodoItem
- `Id` (int): 唯一識別碼
- `Title` (string): 待辦事項標題
- `IsCompleted` (bool): 完成狀態
- `CreatedDate` (DateTime): 建立日期時間

## 注意事項

⚠️ 本專案使用 **In-Memory 資料庫**，這意味著：
- 資料僅儲存在記憶體中
- 應用程式重新啟動後，所有資料將會遺失
- 適合用於開發、測試和示範用途
- 不適合用於正式環境

如需持久化資料，可以將資料庫改為 SQL Server、PostgreSQL 或其他資料庫系統。