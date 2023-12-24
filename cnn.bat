@echo off
rem 激活python3.6的虚拟环境
call .\venv\Scripts\activate
rem 运行eval.py评估
python .\cnn_mailclassify\eval.py
rem 结束
echo finish
exit
