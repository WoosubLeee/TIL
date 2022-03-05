# Django SECRET_KEY

장고 프로젝트를 생성하면, 기본적으로 메인 폴더에 settings.py가 생성된다. settings.py 안에는 다양한 설정 항목들이 있는데 그중 SECRET_KEY 라는 것이 있다. [Django 공식문서](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)를 보면 다음과 같이 안내 되어 있다. 

SECRET_KEY의 사용 용도

- django.contrib.sessions.backends.cache 이외의 session backend를 사용하고 있거나, 기본 get_session_auth_hash()를 사용하는 모든 sessions
- CookieStorage 혹은 FallbackStorage를 사용하는 모든 messages 
- 모든 PasswordResetView
- 다른 키가 제공되지 않는 암호화 서명 사용 시 사용된다. 

**"SECRET_KEY 란 특정 django 설치을 위한 비밀 키이며 이는 암호화 서명을 제공하는 데 사용되며 고유하고 예측할 수 없는 값으로 설정해야 한다. "라고** 나와 있다. 즉, 암호화 인증에 사용되는 비밀키라는 말이다. - (보안 관리)

SECRET_KEY가 없으면 Django project는 실행되지 않고, 보안을 위해 외부에 공개되면 안된다. SECRET_KEY는 꼭 초기에 저장된 값을 유지할 필요없고, 배포된 이후에도 계속 변경하여도 된다.

## How to protect

### 외부에 저장하기

1. secrets.json 생성

   ```
   tistory
   |
   |
   | ㅡㅡ app
   |       |
   |       |ㅡㅡ __init__.py
   |       |ㅡㅡ asgi.py
   |       |ㅡㅡ settings.py
   |       |ㅡㅡ urls.py
   |       |ㅡㅡ wsgi.py
   |
   |ㅡㅡ db.sqlite3
   |ㅡㅡ secrets.json
   |ㅡㅡ manage.py
   ```

   위와 같이 프로젝트 최상단 폴더에 생성해준다.

2. SECRET_KEY 작성

   ```json
   # secrets.json
   
   {
   	"SECRET_KEY": "<Your Django SECRET KEY>"
   }
   ```

3. settings.py 작성

   ```python
   # settings.py
   
   import os, json
   from django.core.exceptions import ImproperlyConfigured
   
   BASE_DIR = Path(__file__).resolve().parent.parent
   
   
   secret_file = os.path.join(BASE_DIR, 'secrets.json')  # secrets.json 파일 위치를 명시
   
   with open(secret_file) as f:
       secrets = json.loads(f.read())
   
   def get_secret(setting):
       """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
       try:
           return secrets[setting]
       except KeyError:
           error_msg = "Set the {} environment variable".format(setting)
           raise ImproperlyConfigured(error_msg)
   
   
   SECRET_KEY = get_secret("SECRET_KEY")
   ```

4. .gitignore에 추가

   ```
   # .gitignore
   
   secrets.json
   ```

   

## References

[Django 02] - 시크릿 키(SECRET_KEY) 분리 설정 (https://grape-blog.tistory.com/17)