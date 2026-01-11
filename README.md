# DataLens - AI-Powered Data Cleaning & Analytics Platform

<div align="center">

![DataLens Logo](https://img.shields.io/badge/DataLens-AI%20Analytics-6366f1?style=for-the-badge)

**An intelligent data cleaning and insight platform for analysts to quickly understand, clean, and analyze datasets.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [API Documentation](#-api-documentation)

</div>

---

## 🚀 Features

### Core Data Management
- 📤 **File Upload** - Support for CSV and XLSX files (up to 50MB)
- 📊 **Dataset Overview** - Comprehensive statistics with categorical/numerical breakdown
- 🔍 **Schema & Column Analysis** - Detailed column information with data types and statistics
- 💾 **Export** - Download cleaned data in CSV or XLSX format

### AI-Powered Cleaning
- ✨ **AI Assistant** - Natural language data cleaning commands
  - "Remove duplicate rows"
  - "Fill missing values with mean"
  - "Convert all text to lowercase"
  - "Remove outliers from numeric columns"
  - And many more!

### Data Quality Checks
- 🔍 **Missing Values** - Detection with options to delete rows or impute (mean/median/mode)
- 🔄 **Duplicate Detection** - Identify and remove duplicate rows
- 🎯 **Outlier Detection** - IQR and Z-score methods with removal/capping options
- 📝 **Text Standardization** - Trim whitespace, fix capitalization (title/upper/lower)

### Advanced Transformations
- 🔄 **Data Type Conversion** - Convert between int, float, string, datetime, bool
- 📅 **Date Parsing** - Parse and format date columns with multiple format support
- 🗂️ **Column Operations** - Rename, drop, copy columns
- 🔍 **Row Filtering** - Filter with conditions (>, <, =, contains, between)
- 📊 **Data Normalization** - Min-max and Z-score scaling
- 🔤 **Special Characters** - Remove special characters from text columns
- 💱 **Unit Conversion** - Convert currency, weight, distance, temperature units

### Visualization & Analytics
- 📈 **Interactive Charts** - Bar, Line, Area, Pie, Donut, Scatter, Combo charts
- 🔍 **Chart Filters** - Advanced filtering with multiple conditions
- 📊 **Enhanced Legends** - Clear, professional chart legends
- 💡 **Quick Insights** - Automated insights including correlations, distributions, and quality scores

### Developer Tools
- 📋 **Cheat Sheet** - Quick reference for Power BI DAX, Pandas, and SQL formulas
- 📝 **Cleaning Logs** - Track all cleaning operations
- 📊 **Quality Reports** - Generate comprehensive data quality reports

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 18.2.0
- **Build Tool**: Vite 5.0.0
- **Styling**: Tailwind CSS 3.3.6
- **Charts**: Recharts 2.15.4
- **Icons**: Lucide React 0.263.1
- **HTTP Client**: Axios 1.6.2

### Backend
- **Framework**: Flask 3.0.0
- **Data Processing**: Pandas 2.1.3, NumPy 1.26.2
- **Statistics**: SciPy 1.11.4
- **Excel Support**: openpyxl 3.1.2
- **CORS**: flask-cors 4.0.0

---

## 📦 Installation

### Prerequisites
- Python 3.8+ 
- Node.js 16+ and npm
- Git

### Backend Setup

1. **Navigate to backend directory:**
```bash
cd backend
```

2. **Create virtual environment (recommended):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

4. **Run the Flask server:**
```bash
python app.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Install dependencies:**
```bash
npm install
```

3. **Run the development server:**
```bash
npm run dev
```

The frontend will run on `http://localhost:3000`

---

## 🎯 Usage

1. **Start both servers:**
   - Backend: `python backend/app.py` (in backend directory)
   - Frontend: `npm run dev` (in frontend directory)

2. **Open the application:**
   - Navigate to `http://localhost:3000` in your browser

3. **Upload your dataset:**
   - Click "Upload Dataset" in the sidebar
   - Select a CSV or XLSX file (max 50MB)

4. **Explore your data:**
   - **Dataset Overview**: View statistics and data type breakdown
   - **Schema & Columns**: Explore column details
   - **Data Quality**: Run quality checks and apply cleaning actions

5. **Clean your data:**
   - Use the **AI Assistant** for natural language commands
   - Or use **Data Quality** panel for specific operations
   - Apply transformations like unit conversion, normalization, etc.

6. **Visualize:**
   - Go to **Charts & Graphs** section
   - Select chart type and columns
   - Apply filters for focused analysis

7. **Export:**
   - Navigate to **Export Data**
   - Choose format (CSV or XLSX)
   - Download your cleaned dataset

---

## 📁 Project Structure

```
DataLens/
├── backend/
│   ├── app.py                 # Flask API server
│   ├── requirements.txt       # Python dependencies
│   └── uploads/               # Uploaded files (auto-created, gitignored)
│
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   │   └── client.js      # API client functions
│   │   ├── components/
│   │   │   └── Dashboard.jsx  # Main dashboard component
│   │   ├── App.jsx            # App root component
│   │   ├── main.jsx           # Entry point
│   │   └── index.css          # Global styles
│   ├── index.html             # HTML template
│   ├── package.json           # Node dependencies
│   ├── tailwind.config.js     # Tailwind CSS config
│   ├── vite.config.js         # Vite config with proxy
│   └── postcss.config.js      # PostCSS config
│
├── .gitignore                 # Git ignore rules
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Contribution guidelines
└── README.md                  # This file
```

---

## 🔌 API Documentation

### File Management
- `POST /api/upload` - Upload CSV/XLSX file
- `GET /api/data/download/<file_id>?format=csv|xlsx` - Download cleaned file
- `GET /api/health` - Health check

### Data Analysis
- `GET /api/data/overview/<file_id>` - Get dataset overview with statistics
- `GET /api/data/schema/<file_id>` - Get schema and column summary
- `GET /api/data/column/<file_id>/<column_name>` - Get detailed column insights
- `GET /api/data/chart/<file_id>` - Get chart data
- `POST /api/data/chart-filter/<file_id>` - Filter chart data

### Data Quality
- `GET /api/data/missing/<file_id>` - Detect missing values
- `DELETE /api/data/missing/<file_id>` - Delete rows with missing values
- `POST /api/data/impute/<file_id>` - Impute missing values (mean/median/mode)
- `GET /api/data/duplicates/<file_id>` - Detect duplicate rows
- `DELETE /api/data/duplicates/<file_id>` - Remove duplicates
- `POST /api/data/standardize/<file_id>` - Standardize text formatting
- `GET /api/data/outliers/<file_id>` - Detect outliers
- `POST /api/data/handle-outliers/<file_id>` - Remove or cap outliers

### Advanced Transformations
- `POST /api/data/convert-types/<file_id>` - Convert data types
- `POST /api/data/parse-dates/<file_id>` - Parse date columns
- `POST /api/data/column-operations/<file_id>` - Column operations (rename/drop/copy)
- `POST /api/data/filter-rows/<file_id>` - Filter rows with conditions
- `POST /api/data/normalize/<file_id>` - Normalize data (min-max/z-score)
- `POST /api/data/remove-special-chars/<file_id>` - Remove special characters
- `POST /api/data/convert-units/<file_id>` - Convert units (currency/weight/distance/temp)

### AI & Insights
- `POST /api/data/nlp-command/<file_id>` - Process natural language commands
- `GET /api/data/insights/<file_id>` - Generate quick insights

### Reports
- `GET /api/data/report/quality/<file_id>` - Generate quality report
- `GET /api/data/report/cleaning-log/<file_id>` - Get cleaning log

---

## 🎨 UI Features

### Theme
- **Mode**: Dark theme with vibrant color palette
- **Primary Colors**: Indigo (#6366f1), Purple (#8b5cf6), Pink (#ec4899)
- **Accent Colors**: Emerald, Amber, Cyan
- **Font**: Inter (system fallback)

### Components
- Responsive sidebar navigation
- Interactive data tables
- Professional chart visualizations
- Modal dialogs for user input
- Loading states and error handling

---

## 💡 Example Use Cases

### 1. Natural Language Cleaning
```
"Remove duplicate rows"
"Fill missing values with median"
"Convert all text columns to lowercase"
"Remove outliers from price column"
```

### 2. Unit Conversion
- Convert currency: USD → EUR, GBP → USD
- Convert weight: kg → lb, g → kg
- Convert distance: km → mile, m → km
- Convert temperature: Celsius → Fahrenheit

### 3. Data Transformation
- Normalize numeric columns for ML models
- Parse dates from various formats
- Filter rows: `price > 100 AND category = 'Electronics'`
- Merge or split columns

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For detailed guidelines, see [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👥 User Persona

Designed for:
- **Data Analysts** - Quick data cleaning and profiling
- **Product Analysts** - Fast dataset onboarding
- **Business Analysts** - Data quality assessment
- **Data Scientists** - Pre-processing for ML pipelines

---

## 🐛 Known Issues & Limitations

- Data is stored in memory (not persisted across server restarts)
- Maximum file size: 50MB
- Supported formats: CSV, XLSX only
- Unit conversion uses static rates (for production, use live API)

---

## 🔮 Future Enhancements

- [ ] Database persistence
- [ ] Real-time unit conversion rates
- [ ] Support for more file formats (JSON, Parquet)
- [ ] Collaborative features
- [ ] Advanced ML-based cleaning suggestions
- [ ] Export to cloud storage (S3, GCS)
- [ ] Scheduled cleaning jobs
- [ ] API authentication

---

<div align="center">

**Made with ❤️ for Data Analysts**

⭐ Star this repo if you find it useful!

</div>
