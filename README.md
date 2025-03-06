## 📌 Automated UI Testing for SauceDemo using Selenium  

## 🔗 Links  
- **App URL:** [SauceDemo](https://www.saucedemo.com/)  
- **GitHub Repository:** [SauceDemo Automation](https://github.com/ShariraSaniane/QA-SauceDemo-Selenium)  
- **Test Scenarios:** [Google Spreadsheet](https://docs.google.com/spreadsheets/d/1VYHNUnf61af2g0gSD_-JE0GlZudrGvduZIVohOF5DAM/edit?usp=sharing)  
- **Documentation:** [Documentation](https://drive.google.com/file/d/1eYXf8cDzQ41hTB-qUfIIjSAi13IFSvrB/view?usp=sharing)

---

## 🛠 Tools & Technologies  
| Technology           | Description                          |
|----------------------|--------------------------------------|
| Selenium WebDriver  | Automates browser interaction        |
| Python              | Scripting language                   |
| ChromeDriver        | WebDriver for Google Chrome         |
| Visual Studio Code  | Code editor for running tests       |
| GitHub              | Version control and project hosting |

---

## 🔧 Installation & Setup  
### Clone Repository  
```bash
git clone https://github.com/ShariraSaniane/QA-SauceDemo-Selenium
```

### Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

**Download ChromeDriver**
- Ensure you have Google Chrome installed.
- Download the compatible ChromeDriver for your browser version.
- Extract and place it in the project directory or set it in the system path.

**Install Selenium**
Open cmd and run comment:
```bash 
pip install selenium
```

### 🚀 Running the Tests
**▶️ Run All Test Cases**
```bash
pytest test_cases.py -v
```

**▶️ Run a Specific Test File:**
```bash
pytest tests/test_login.py
```

#### 📊 Test Scenarios
- Login Functionality ✅
- Product Page Functionality ✅
- Shopping Cart Functionality ✅
- Your Cart Functionality ✅
- Checkout Functionality ✅

#### 📬 Contact
- Created by: Sharira Saniane
- GitHub: ShariraSaniane
- Email: sharirasaniane95@gmail.com
