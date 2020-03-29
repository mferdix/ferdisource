echo "========================"
echo "   Installing Python3   "
echo "========================"

  pkg install python

echo "============================"
echo "   Installing PIP Python3   "
echo "============================"

  pkg install python-pip

echo "==================="
echo "   Upgrading PIP   "
echo "==================="
 
  pip install --upgrade pip

echo "==============================="
echo "   Installing Python Library   "
echo "==============================="

  pip install pandas
  pip install lxml
  pip install bs4
  pip install requests

echo "================"
echo "   Game Start   "
echo "================"

python index.py
