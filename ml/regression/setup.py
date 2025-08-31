#!/usr/bin/env python3
"""
Setup script for JupyterLab regression environment
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        if e.stderr:
            print(f"Error details: {e.stderr}")
        return False

def main():
    # Get the directory where this script is located
    script_dir = Path(__file__).parent.absolute()
    
    print("🚀 Setting up JupyterLab for regression analysis...")
    print(f"📁 Working directory: {script_dir}")
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Check if virtual environment exists
    venv_path = script_dir / "venv"
    
    if not venv_path.exists():
        print("\n📦 Creating virtual environment...")
        if not run_command(f"{sys.executable} -m venv venv", "Creating virtual environment"):
            return False
    else:
        print("\n✅ Virtual environment already exists")
    
    # Determine the python executable in the virtual environment
    if os.name == 'nt':  # Windows
        python_exe = venv_path / "Scripts" / "python.exe"
        pip_exe = venv_path / "Scripts" / "pip.exe"
    else:  # Unix-like (Linux, macOS)
        python_exe = venv_path / "bin" / "python"
        pip_exe = venv_path / "bin" / "pip"
    
    # Install requirements
    print("\n📚 Installing requirements...")
    if not run_command(f"{pip_exe} install --upgrade pip", "Upgrading pip"):
        return False
    
    if not run_command(f"{pip_exe} install -r requirements.txt", "Installing packages from requirements.txt"):
        return False
    
    print("\n🎉 Setup complete!")
    print("\n📋 To start JupyterLab:")
    print(f"1. Navigate to: {script_dir}")
    print("2. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("3. Start JupyterLab:")
    print("   jupyter lab")
    
    # Ask if user wants to start JupyterLab now
    start_now = input("\n🤔 Would you like to start JupyterLab now? (y/n): ").lower().strip()
    
    if start_now in ['y', 'yes']:
        print("\n🚀 Starting JupyterLab...")
        try:
            # Start JupyterLab
            subprocess.run([str(python_exe), "-m", "jupyter", "lab"], cwd=script_dir)
        except KeyboardInterrupt:
            print("\n👋 JupyterLab stopped by user")
        except Exception as e:
            print(f"❌ Error starting JupyterLab: {e}")

if __name__ == "__main__":
    main() 