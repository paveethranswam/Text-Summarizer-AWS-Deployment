call 
echo 'Starting program -> Activating textSum evn -> Running main.py from env'
call textSum\Scripts/activate
call python main.py
echo 'Pausing to check errors and cmd logs'
call deactivate
@REM pause
