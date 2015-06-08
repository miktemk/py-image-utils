@echo off
setlocal
:PROMPT
SET /P AREYOUSURE=Are you sure (delete all in todecompose) (Y/[N])? 
IF /I "%AREYOUSURE%" NEQ "Y" GOTO END

del /q todecompose\*
del /q todecompose\decomposed\*

:END
endlocal

pause