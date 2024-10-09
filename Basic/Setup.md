## Python in Linux

In every major Linux distribution, Python should be already installed and working properly.

## Python in Windows

### Use PATH in the Installer

**Download the Python Windows Installer from the official website**:
- Avoid installing it as an App from MS Store.

**Install Python with the "Add Python to PATH" Option**:
- Ensure the checkbox for "Add Python to PATH" is checked during the installation process.

### Test It

Test the installation by running the following commands in Command Prompt (`cmd`):

```bash
python --version

py --version
   - Add both paths to the `Path` variable in Environment Variables.
```

If the commands do not work, edit the PATH manually:

### Edit Environment Variables

1. **Locate Python Executable**:
   - Find the path of the Python executable (usually in `C:\PythonXX`, where `XX` is the version number).

2. **Locate Scripts Folder**:
   - Find the path of the `Scripts` subfolder (usually in `C:\PythonXX\Scripts`).

3. **Add Paths to Environment Variables**:
   - Add both paths to the `Path` variable in Environment Variables.