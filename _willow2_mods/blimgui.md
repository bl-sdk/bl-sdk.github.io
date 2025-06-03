---
pyproject_url: https://raw.githubusercontent.com/juso40/blimgui/refs/heads/master/blimgui/pyproject.toml
---
# blimgui
A library that allows modders to easily create and manage a separate window to develope GUI mods.  

## Installation
This mod **cannot** be installed like a regular ``.sdkmod``, instead it comes as a ``.zip``.  
After downloading the ``.zip`` file, place it exactly where you would place a ``.sdkmod`` file.  
Then, extract the contents of the ``.zip`` file.  
You should now have a folder named ``blimgui`` in your mods folder.  
After that you can safely delete the ``.zip`` file.

Your folder structure should look something like this:
```
Borderlands 2/
└── Binaries/
└── DLC/
└── Documents/
└── ...
└── sdk_mods/
    └── __main__.py/
    └── *.sdkmod
    └── *.sdkmod
    └── *.sdkmod
    └── *.sdkmod
    └── blimgui/
        └── pyproject.toml
        └── __init__.py
        └── dist/
            └── ...
```

