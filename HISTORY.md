# HISTROY

## 0.0.1 [2018-12-30]

### Added

- 大幅度地修改了程序结构。
  - `config.py` 中存放相关配置信息
  - `manage.py` 为程序的应用脚本，通过 `flask run -h 0.0.0.0` 来启动，或者也可以用 `gunicorn -w 2 -b 0.0.0.0 manage:app` 来部署。
  - `app/` 中存放程序的主要内容。