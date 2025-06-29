import os

def print_structure(start_path='.', max_depth=3, current_depth=0):
    for item in os.listdir(start_path):
        item_path = os.path.join(start_path, item)
        try:
            size = os.path.getsize(item_path)
            size_mb = size / (1024 * 1024)
        except:
            size_mb = 0
        
        indent = '│   ' * current_depth + ('├── ' if os.path.isdir(item_path) else '└── ')
        print(f"{indent}{item} ({size_mb:.2f} MB)")

        if os.path.isdir(item_path) and current_depth < max_depth:
            print_structure(item_path, max_depth, current_depth + 1)

if __name__ == "__main__":
    print("📁 Folder Structure (with file sizes):\n")
    print_structure('.', max_depth=4)
