# Arch Linux System Configuration Script

## 1. Install uv

```sh
sudo pacman -Syu python-uv 
```

## 2. Create a virtual environment

```sh
uv venv
```

## 3. Install dependencies

```sh
uv pip install -r requirements.txt
```

## 4. Run script

```sh
python main.py [-v for verbose output]
```
