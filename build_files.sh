echo "BUILD START IN BUILD_FILE"
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic -noinput --clear
echo "BUILD END IN BUILD_FILE"
