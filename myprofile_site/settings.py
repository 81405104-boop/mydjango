(venv) D:\mydjango>python manage.py collectstatic --noinput
Traceback (most recent call last):
  File "D:\mydjango\manage.py", line 22, in <module>
    main()
    ~~~~^^
  File "D:\mydjango\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
    ~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^
  File "D:\mydjango\venv\Lib\site-packages\django\core\management\__init__.py", line 442, in execute_from_command_line
    utility.execute()
    ~~~~~~~~~~~~~~~^^
  File "D:\mydjango\venv\Lib\site-packages\django\core\management\__init__.py", line 382, in execute
    settings.INSTALLED_APPS
  File "D:\mydjango\venv\Lib\site-packages\django\conf\__init__.py", line 81, in __getattr__
    self._setup(name)
    ~~~~~~~~~~~^^^^^^
  File "D:\mydjango\venv\Lib\site-packages\django\conf\__init__.py", line 68, in _setup
    self._wrapped = Settings(settings_module)
                    ~~~~~~~~^^^^^^^^^^^^^^^^^
  File "D:\mydjango\venv\Lib\site-packages\django\conf\__init__.py", line 166, in __init__
    mod = importlib.import_module(self.SETTINGS_MODULE)
  File "D:\Python\Lib\importlib\__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1398, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1371, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1342, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 938, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 758, in exec_module
  File "<frozen importlib._bootstrap_external>", line 896, in get_code
  File "<frozen importlib._bootstrap_external>", line 826, in source_to_code
  File "<frozen importlib._bootstrap>", line 491, in _call_with_frames_removed
  File "D:\mydjango\myprofile_site\settings.py", line 68
    'django.template.context_p_
    ^
SyntaxError: unterminated string literal (detected at line 68)

(venv) D:\mydjango>
