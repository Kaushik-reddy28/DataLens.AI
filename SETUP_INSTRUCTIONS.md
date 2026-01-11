# DataLens Setup Instructions

## Current Status
- ✅ Backend server is running on port 5000
- ⚠️ Frontend requires Node.js to be installed

## Step 1: Install Node.js (if not already installed)

1. Download Node.js from: https://nodejs.org/
2. Install the **LTS (Long Term Support)** version
3. During installation, make sure to check "Add to PATH" option
4. **Restart your computer** or **close and reopen all terminal windows** after installation

## Step 2: Verify Node.js Installation

Open a **new** Command Prompt or PowerShell window and run:
```cmd
node --version
npm --version
```

Both commands should show version numbers.

## Step 3: Start the Frontend Server

### Option A: Using the Batch File (Easiest)
1. Double-click `start_frontend_fixed.bat` in the project root folder
2. Wait for dependencies to install (first time only)
3. The server will start on http://localhost:3000

### Option B: Manual Start
1. Open Command Prompt
2. Navigate to the frontend folder:
   ```cmd
   cd "C:\Users\Admin\Downloads\DA agent (vin)\frontend"
   ```
3. Install dependencies (first time only):
   ```cmd
   npm install
   ```
4. Start the server:
   ```cmd
   npm run dev
   ```

## Step 4: Access the Application

1. Open your web browser
2. Go to: **http://localhost:3000**
3. You should see the DataLens dashboard

## Troubleshooting

### Port 3000 already in use
If you get an error about port 3000 being in use:
- Close any other applications using port 3000
- Or modify `frontend/vite.config.js` to use a different port

### Backend not connecting
- Make sure the backend is running on port 5000
- Check `backend/app.py` is running
- Verify CORS is enabled in the backend

### npm command not found
- Node.js is not installed or not in PATH
- Reinstall Node.js and make sure to check "Add to PATH"
- Restart your terminal/computer after installation

## Quick Start (Once Node.js is Installed)

1. **Backend** (already running): `python backend/app.py`
2. **Frontend**: Double-click `start_frontend_fixed.bat` or run `npm run dev` in the frontend folder
3. **Open browser**: http://localhost:3000

