# HISTROY

## 0.0.2 [2019-2-13]

### Added

- app/static: 存放了 Bootstrap 使用的css和js相关文件。
- app/templates/common: 网上抄的 header, sidebar, base, footer 的 templates。
- app/templates/index.html: 主页。

### Modified

- app/templates/common/header.html: 修改了一下，现在更贴切选座位的需求了。

## 0.0.1 [2018-12-30]

### Added

- 大幅度地修改了程序结构。
  - `config.py` 中存放相关配置信息
  - `manage.py` 为程序的应用脚本，通过 `flask run -h 0.0.0.0` 来启动，或者也可以用 `gunicorn -w 2 -b 0.0.0.0 manage:app` 来部署。
  - `app/` 中存放程序的主要内容。