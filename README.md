# 📘 BrowserStack Cloud Integration
This project demonstrates how to automate login functionality testing for [SauceDemo](https://www.saucedemo.com/) using Selenium WebDriver with the Page Object Model (POM) design pattern. Tests are executed on [BrowserStack's](https://automate.browserstack.com/) cloud infrastructure, enabling cross-browser and cross-platform testing without the need for local setup.

# 🚀 Features
- Automated login tests for SauceDemo.
- Page Object Model (POM) design pattern.
- Integration with BrowserStack for cloud-based testing.
- Configurable test environments via browserstack.yml.
- Support for parallel and headless test execution.

# 📁 Project Structure
<pre> 
BrowserStack-Cloud-Integration/
├── pages/
│   └── login_page.py
├── tests/
│   └── test_login.py
├── utils/
│   └── browserstack_driver.py
├── browserstack.yml
├── conftest.py
├── requirements.txt
└── README.md
</pre>

# ⚙️ How to Run

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

2. **Set Your BrowserStack Credentials**
   
   Update your username and access key in both:
   - `conftest.py`
   - `browserstack.yml`

3. **Update browserstack.yml (Optional)**
   
   Modify the `browserstack.yml` file to specify desired browsers, operating systems, and other configurations.

4. **Run The Login Test**
   ```bash 
   browserstack-sdk pytest   .\tests\test_login.py

# 📊 Viewing Test Results
After test execution, you can view detailed results, including logs, screenshots, and videos, on [the BrowserStack Automate Dashboard](https://automate.browserstack.com/dashboard/v2/public-build/a3RXd1JhMFJOR1dFS0RyMmh5ZkN0OHdQNnc2eHJPWTc1b2ZWeGk4dGRlTjBvUUM4VWFESGowY1dJMFZ3YWZXbXliMDNES2ovRkdCeTZURVd3K3FaVUE9PS0tcm05NlZYd1UxM2t5V1NsekJHdmNjUT09--b76d6f0ace030f225551591f8347e51386b34587).

# 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.
