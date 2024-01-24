from setuptools import setup

APP = ['anki.py']  # Replace with your script's filename
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter', 'genanki', 'hashlib'],
    'plist': {
        'CFBundleName': "Anki Deck Generator",
        'CFBundleShortVersionString': "0.1.0",  # Version of your application
        'CFBundleIdentifier': "com.yourdomain.ankideckgenerator",  # A unique identifier for your app
        'NSFullSizeContentView': True,
        'NSAppTransportSecurity': {'NSAllowsArbitraryLoads': True},
        'LSUIElement': True,
    }
}

setup(
    app=APP,
    name="Anki Deck Generator",
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
