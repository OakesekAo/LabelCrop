# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# Define the path to the Python DLLs
python_dll_path = os.path.join(sys.exec_prefix, 'DLLs')

a = Analysis(
    ['src/main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        (os.path.join(python_dll_path, '_tkinter.pyd'), '.'),
        (os.path.join(python_dll_path, 'tcl86t.dll'), '.'),
        (os.path.join(python_dll_path, 'tk86t.dll'), '.')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ShippingLabelProcessor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ShippingLabelProcessor',
)
