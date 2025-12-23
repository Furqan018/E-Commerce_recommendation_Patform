@echo off
echo Creating Python virtual environment...
python -m venv ecommerce_env

echo Activating environment...
call ecommerce_env\Scripts\activate

echo Installing packages with pre-compiled wheels...
pip install numpy==1.24.4 pandas==2.0.3 scikit-learn==1.3.0 plotly==5.17.0 streamlit==1.28.0

echo Installation complete!
echo.
echo To run your app:
echo 1. ecommerce_env\Scripts\activate
echo 2. streamlit run app.py
pause