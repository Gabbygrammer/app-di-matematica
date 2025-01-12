import subprocess
import sys

dist_path = sys.argv[1]

cpp_executables = ["math-root-extractor.exe"]

mingw_path = "C:/MinGW/bin"

command = f"pyinstaller --onefile --noconsole --name app-mate --add-binary=\"{mingw_path}:.\" --add-binary=\"{mingw_path}/g++.exe:.\""

for executable in cpp_executables:
    command += f" --add-binary=\"{executable}:.\""

command += " main.py"

print("Bundling app...")
bundling = subprocess.run(command)
if bundling.returncode == 0:
    print("Bundled math app succesfully!")
else:
    print("An error occurred during the bundling.")

print("Executing app...")
execution = subprocess.run(f"{dist_path}\\app-mate.exe")
print("Program terminated.")
quit()
