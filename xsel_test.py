import subprocess

def copy_to_clipboard(text):
    try:
        subprocess.run(['xsel', '-i'], input = text.encode(), check=True)
    except FileNotFoundError:
        print("xsel command not found. Clipboard operations may not work.")

def paste_text():
    try:
        result = subprocess.run(['xsel', '-o'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print("Error: Unable to paste text using xsel.")
            return None
    except FileNotFoundError:
        print("Error: xsel command not found. Make sure xsel is installed.")
        return None


def main():
    text = 'This is the test text'
    copy_to_clipboard(text)
    print(paste_text())

if __name__ == '__main__':
    main()