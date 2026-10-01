"""Compila una versión nueva para Google Play.

1. Sube versionCode en +1 (Play rechaza un AAB con un versionCode ya usado).
2. python build.py  ->  npx cap sync android  ->  gradlew bundleRelease assembleRelease
3. Copia el .aab y el .apk firmados a app/release/

Uso: python release.py            (sube versionCode, mantiene versionName)
     python release.py 0.2.0      (además cambia versionName)
"""
import os
import re
import shutil
import subprocess
import sys

APP = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(APP)
ANDROID = os.path.join(APP, 'android')
GRADLE = os.path.join(ANDROID, 'app', 'build.gradle')
JDK = r'C:\Users\Gabriel\android-tools\jdk'

if not os.path.exists(os.path.join(ANDROID, 'keystore.properties')):
    raise SystemExit('Falta android/keystore.properties (copia C:/Users/Gabriel/cripta-keys/keystore.properties)')

g = open(GRADLE, encoding='utf-8').read()
code = int(re.search(r'versionCode (\d+)', g).group(1)) + 1
g = re.sub(r'versionCode \d+', f'versionCode {code}', g)
if len(sys.argv) > 1:
    g = re.sub(r'versionName "[^"]*"', f'versionName "{sys.argv[1]}"', g)
name = re.search(r'versionName "([^"]*)"', g).group(1)
open(GRADLE, 'w', encoding='utf-8').write(g)
print(f'Versión {name} (versionCode {code})')

env = dict(os.environ, JAVA_HOME=JDK)
subprocess.run([sys.executable, 'build.py'], cwd=ROOT, check=True)
subprocess.run('npx cap sync android', cwd=APP, shell=True, check=True)
subprocess.run([os.path.join(ANDROID, 'gradlew.bat'), 'bundleRelease', 'assembleRelease', '--no-daemon', '-q'], cwd=ANDROID, check=True, env=env)

out = os.path.join(APP, 'release')
os.makedirs(out, exist_ok=True)
base = os.path.join(ANDROID, 'app', 'build', 'outputs')
aab = os.path.join(out, f'cripta-{name}-{code}.aab')
apk = os.path.join(out, f'cripta-{name}-{code}.apk')
shutil.copy(os.path.join(base, 'bundle', 'release', 'app-release.aab'), aab)
shutil.copy(os.path.join(base, 'apk', 'release', 'app-release.apk'), apk)
print('Listo:\n ', aab, '\n ', apk)
