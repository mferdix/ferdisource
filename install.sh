echo "========================"
echo "   Installing Python3   "
echo "========================"

  apt install python3

echo "============================"
echo "   Installing PIP Python3   "
echo "============================"

  apt install python3-pip

echo "==================="
echo "   Upgrading PIP   "
echo "==================="
 
  pip3 install --upgrade pip

echo "==============================="
echo "   Installing Python Library   "
echo "==============================="

  pip3 install lxml
  pip3 install bs4
echo "==============="
echo "   Sabar Cuy   "
echo "==============="
  pip3 install requests

echo "================"
echo "   Game Start   "
echo "================"

python3 index.py
