[app]

title = AstroVR
package.name = astrovr
package.domain = org.astrovr

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait

fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1


[app:android]

android.api = 36
android.minapi = 24
android.archs = arm64-v8a
