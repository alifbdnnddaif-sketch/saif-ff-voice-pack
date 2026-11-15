[app]
title = SAIF FF VOICE PACK
package.name = saifffvoicepack
package.domain = org.saif
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,requests,certifi,urllib3,idna,charset_normalizer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE
android.api = 31
android.min_api = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
