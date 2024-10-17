Для правильной работы с Allure в Lesson_10 необходимо:

1. Установить с сайта pypi, раздел allure-pytest
    Команда установки: pip install allure-pytest

2. Чтобы терминал распознал команду Allure необходимо установить Allure Report
    Для пользователей Windows в терминале VC code вводим:
       Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
       Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
    Затем команду: scoop install allure

3. Для запуска теста test_01_form.py используем команду: pytest test_01_form.py --alluredir FormResult
4. Для просмотра сформированного отчета для теста test_01_form.py используем команду: allure serve FormResult

5. Для запуска теста test_02_calc.py используем команду: pytest test_02_calc.py --alluredir CalcResult
6. Для просмотра сформированного отчета для теста test_02_calc.py используем команду: allure serve CalcResult

7. Для запуска теста test_03_shop.py используем команду: pytest test_03_shop.py --alluredir ShopResult
8. Для просмотра сформированного отчета для теста test_03_shop.py используем команду: allure serve ShopResult
