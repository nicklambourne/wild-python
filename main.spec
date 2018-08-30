# -*- mode: python -*-

block_cipher = None


added_files = [
    ( 'src/audio/*', 'audio' )
]

a = Analysis(['src/main.py'],
             pathex=['/Users/nickl93/projects/fun/wild-python'],
             binaries=[],
             datas=added_files,
             hiddenimports=['PyQt5.sip'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='main',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
app = BUNDLE(exe,
             name='main.app',
             icon='icon.icns',
             info_plist={
                'NSHighResolutionCapable': 'True'
             },
             bundle_identifier=None)
