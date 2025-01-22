# System Info Tool

A lightweight Python-based tool designed to display essential system information through a clean GUI, accompanied by a custom startup sound.

---

## Why We Created This
In the modern computing environment, understanding the details of your system is essential for troubleshooting, optimization, and hardware compatibility checks. We wanted to create a simple yet intuitive tool that doesn't rely on bulky software and gets the job done efficiently.

The **System Info Tool** provides the following:
- A clear view of your system's **Manufacturer**, **Model**, **Processor**, and **Total RAM**.
- A visually appealing and user-friendly graphical interface.
- A touch of personality with a custom startup sound.

It's designed to be **simple**, **lightweight**, and **effective** for both developers and non-tech-savvy users.

---

## Features
- **Displays System Information:**
  - System Manufacturer
  - System Model
  - Processor
  - Total RAM (in GB)
- **Custom Audio Notification:**  
  Plays a custom sound when the application starts.
- **Graphical User Interface:**  
  Clean and intuitive design built with `tkinter`.

---

## How to Run

### Option 1: Run the Python Script
#### Prerequisites
1. Install Python 3.x on your system.
2. Install dependencies using pip:
   ```bash
   pip install wmi
   ```

#### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/nullpearl-systems/SystemInfoTool.git
   cd SystemInfoTool
   ```
2. Navigate to the `src/` folder:
   ```bash
   cd src
   ```
3. Run the Python script:
   ```bash
   python SysInfoCollector.py
   ```

---

### Option 2: Run the Executable File
If you don't have Python installed, use the pre-packaged executable file:

1. [Download the executable here](https://github.com/nullpearl-systems/SystemInfoTool/releases).
2. Extract the downloaded zip file.
3. Double-click the executable to launch the application.

---

## Building the Executable Yourself
If you'd like to package the tool yourself:

#### Prerequisites
- Python 3.x installed on your system.
- `PyInstaller` package installed:
  ```bash
  pip install pyinstaller
  ```

#### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/nullpearl-systems/SystemInfoTool.git
   cd SystemInfoTool
   ```
2. Navigate to the `src/` folder:
   ```bash
   cd src
   ```
3. Run the following command:
   ```bash
   pyinstaller --onefile --add-data "../audio/system-standby.wav;audio" SysInfoCollector.py
   ```
4. The `.exe` file will be available in the `dist/` folder.

---

## Directory Structure
```
SystemInfoTool/
├── audio/
│   └── system-standby.wav
├── src/
│   └── SysInfoCollector.py
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Download
[Click here to download the executable](https://github.com/nullpearl-systems/SystemInfoTool/releases).

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```