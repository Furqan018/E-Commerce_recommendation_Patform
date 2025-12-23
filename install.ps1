Write-Host "Creating Python virtual environment..." -ForegroundColor Green
python -m venv ecommerce_env

Write-Host "Activating environment..." -ForegroundColor Green
.\ecommerce_env\Scripts\Activate.ps1

Write-Host "Upgrading pip and installing core tools..." -ForegroundColor Green
python -m pip install --upgrade pip setuptools wheel

Write-Host "Installing packages..." -ForegroundColor Green
pip install numpy pandas scikit-learn plotly streamlit

Write-Host "`n----------------------------------------------" -ForegroundColor Cyan
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host "To activate the environment and run your app:" -ForegroundColor Yellow
Write-Host "    .\ecommerce_env\Scripts\Activate.ps1" -ForegroundColor Yellow
Write-Host "    streamlit run app.py" -ForegroundColor Yellow
Write-Host "----------------------------------------------" -ForegroundColor Cyan

Read-Host "Press Enter to continue"