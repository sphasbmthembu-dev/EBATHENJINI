# EBATHENJINI - Deployment Guide

## Deploying to Android

### Prerequisites
- Python 3.8+
- Buildozer
- Android SDK
- Java Development Kit (JDK)

### Step 1: Install Buildozer
```bash
pip install buildozer
```

### Step 2: Configure buildozer.spec
```bash
buildozer android debug
```

Edit `buildozer.spec`:
```ini
[app]
title = EBATHENJINI
package.name = ebathenjini
package.domain = org.ebathenjini

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf

version = 1.0

requirements = python3,kivy,pillow,pyyaml,reportlab

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 25c
```

### Step 3: Build APK
```bash
buildozer android debug
```

### Step 4: Install on Device
```bash
adb install -r bin/ebathenjini-1.0-debug.apk
```

### Step 5: Release Build
```bash
buildozer android release
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore my-release-key.jks \
  bin/ebathenjini-1.0-release-unsigned.apk \
  alias_name
```

## Deploying to iOS

### Prerequisites
- macOS
- Xcode
- Python 3.8+
- Kivy for iOS

### Step 1: Install Kivy for iOS
```bash
pip install kivy-ios
cd ~/code  # Choose your working directory
git clone https://github.com/kivy/kivy-ios
cd kivy-ios
```

### Step 2: Create iOS Build
```bash
toolchain create MyApp ~/path/to/ebathenjini
```

### Step 3: Build for iOS
```bash
cd MyApp
xcodebuild -scheme MyApp -configuration Release
```

### Step 4: Submit to App Store
1. Create App ID in Apple Developer
2. Create provisioning profile
3. Build and sign app
4. Upload to TestFlight
5. Submit for App Store review

## Deploying to Windows

### Step 1: Create Executable
```bash
pip install pyinstaller
pyinstaller --onefile --icon=app/assets/icon.ico main.py
```

### Step 2: Create Installer
Use NSIS or Inno Setup to create Windows installer

```bash
# Using Inno Setup
iscc /O+ /cc "installer_config.iss"
```

## Deploying to macOS

### Step 1: Create macOS App Bundle
```bash
pip install py2app
py2applet --make-setup main.py
python setup.py py2app -A
```

### Step 2: Sign App
```bash
codesign --deep --force --verify --verbose --sign "-" dist/EBATHENJINI.app
```

### Step 3: Create DMG
```bash
hdiutil create -volname "EBATHENJINI" -srcfolder dist -ov -format UDZO EBATHENJINI.dmg
```

## Deploying to Linux

### Step 1: Create AppImage
```bash
pip install appimage-builder
appimage-builder --recipe AppImageBuilder.yml
```

### Step 2: Create DEB Package
```bash
sudo apt-get install python3-kivy
fpm -s python -t deb main.py
```

## Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
```

### Build and Run
```bash
docker build -t ebathenjini .
docker run -it ebathenjini
```

## Cloud Deployment

### Google Cloud Platform
```bash
gcloud app deploy
```

### AWS Lambda
```bash
zip -r ebathenjini.zip app/
aws lambda create-function --function-name ebathenjini \
  --runtime python3.9 --role arn:aws:iam::ACCOUNT:role/lambda-role \
  --handler main.lambda_handler --zip-file fileb://ebathenjini.zip
```

### Heroku
```bash
heroku login
heroku create ebathenjini
git push heroku main
```

## Troubleshooting

### Android Issues
- Clear build cache: `buildozer android clean`
- Update dependencies: `pip install --upgrade buildozer`
- Check Java path: `java -version`

### iOS Issues
- Ensure Xcode is updated: `xcode-select --install`
- Clear build: `rm -rf build dist`
- Check iOS SDK: `xcrun --show-sdk-version`

### General Issues
- Virtual environment issues: Create fresh venv
- Dependency conflicts: Use compatible versions
- Permission errors: Check file permissions

## Release Checklist

- [ ] All tests passing
- [ ] Version number updated
- [ ] CHANGELOG updated
- [ ] README current
- [ ] Screenshots prepared
- [ ] App description ready
- [ ] Privacy policy updated
- [ ] Build tested on target platform
- [ ] Performance optimized
- [ ] Crash reports reviewed
