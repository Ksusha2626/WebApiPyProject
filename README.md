# WebApiPyProject

- Создать и активировать виртуальное окружение
```
python3 -m venv .env
source .env/bin/activate
```
- Установить необходимые пакеты python из requirements.txt
```
pip install -r requirements.txt
```
- Для управления бразуером с помощью Selenium нужны соответсвующие драйвера. Установка ChromeDriver под Linux.
 ```
1) Скачать архив хрома-драйвера, взяв нужную версию из https://chromedriver.chromium.org/downloads
wget https://chromedriver.storage.googleapis.com/88.0.4324.96/chromedriver_linux64.zip

2) Распаковать:
sudo unzip chromedriver_linux64.zip -d /usr/local/bin/

3) Добавить в PATH 
export PATH=$PATH:/path/to/driver/chrome-driver

4) Проверить, что все работает, запустив команду:
chromedriver -v
```
Установка ChromeDriver под MacOS:
 ```
1) Поставить пакетный мэнеджер Brew:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

2) Установить chromedriver:
brew install --cask chromedriver

3) Проверить, что все работает, запустив команду:
chromedriver -v
```
Установка ChromeDriver под Windows 10:
 ```
Видео с установкой: https://www.youtube.com/watch?v=dz59GsdvUF8&ab_channel=ArturSpirin

1) Скачать архив хром-драйвера, взяв нужную версию из https://chromedriver.chromium.org/downloads

2) Распаковать в удобное для вас место, например:
C:/webdrivers/

3) Добавить папку с драйвером в PATH:
Инструкция тут https://www.computerhope.com/issues/ch000549.htm#windows10

4) Проверить, что все работает, запустив команду:
chromedriver -v
```

#### Запуск тестов:

Нужно в конфигурации запуска прописать путь до конфиг файла: 

Edit Configurations -> Templates -> Python tests -> pytest в Aditional Arguments прописать команду:
```
-s -v  --hostconf="{HOST_CONF_FULL_PATH}"
```
