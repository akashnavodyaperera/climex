"""
Build executable for Windows, macOS, and Linux
"""
import os
import sys
import platform
import subprocess

def build_executable():
    """Build executable for current platform"""
    
    system = platform.system()
    print(f"🔨 Building Climex for {system}...")
    
    # Common PyInstaller options
    base_command = [
        'pyinstaller',
        '--name=Climex',
        '--onefile',   
        '--windowed',  
        '--clean',   
    ]
    
   
    if system == 'Windows':
      
        base_command.append('--icon=climexico')
        pass
    elif system == 'Darwin':   
   
        base_command.append('--icon=climexico')
        pass
    
    # Add the main script
    base_command.append('main.py')
    
    try:
        # Run PyInstaller
        result = subprocess.run(base_command, check=True)
        
        print("\n✅ Build successful!")
        print(f"📦 Executable location:")
        
        if system == 'Windows':
            print(f"   → dist\\Climex.exe")
        else:
            print(f"   → dist/Climex")
            
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ PyInstaller not found!")
        print("Install it with: pip install pyinstaller")
        sys.exit(1)

def clean_build():
    """Clean build artifacts"""
    import shutil
    
    dirs_to_remove = ['build', 'dist', '__pycache__']
    files_to_remove = ['Climex.spec']
    
    print("🧹 Cleaning build artifacts...")
    
    for dir_name in dirs_to_remove:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"   Removed {dir_name}/")
    
    for file_name in files_to_remove:
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"   Removed {file_name}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'clean':
        clean_build()
    else:
        build_executable()