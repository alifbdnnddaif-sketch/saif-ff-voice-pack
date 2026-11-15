[app]

# (str) Title of your application
title = SAIF FF VOICE PACK

# (str) Package name
package.name = saifffvoicepack

# (str) Package domain (needed for android packaging)
package.domain = org.saif

# (str) Source directory where the main.py file is located
source.dir = .

# (str) Supported source extensions (comma separated)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,requests,certifi,urllib3,idna,charset_normalizer

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE

# (int) Target Android API, should be as high as possible
android.api = 31

# (int) Minimum API your APK will support
android.min_api = 21

# (str) Android NDK version to use
android.ndk = 25b

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug command)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
