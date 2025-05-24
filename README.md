# 📄 Automated College Registration System using Python & OpenCV

> **Final Year Thesis Project | Document Intelligence, OCR & Data Automation**  
> **Tools:** Python, OpenCV, Pytesseract, MongoDB, Flask, ReportLab

---

##  **Overview**

This end-to-end system automates the student registration workflow for educational institutions using **Python-based data extraction, validation, and document generation**. It combines **computer vision and OCR technologies** to streamline manual entry from academic certificates—reducing time, errors, and improving administrative efficiency.

---

##  **Project Objectives**

- Automate manual form-filling from Grade 10 mark sheets.
- Enhance data accuracy using OCR and image preprocessing.
- Structure and store extracted data securely.
- Generate standardized PDF registration forms.

---

##  **Core Functionalities**

- **OCR-Based Data Capture**: Extracts symbol number, grades, name, and issue date from scanned documents.
- **Image Preprocessing**: Uses OpenCV for grayscale conversion, noise reduction, and thresholding.
- **Data Validation & Storage**: Cleans and validates extracted data before saving to **MongoDB**.
- **PDF Generation**: Automatically generates printable forms using **ReportLab**.
- **Web App (Flask)**: Demonstrates usability with a basic **Flask-based interface**.
- **Security Measures**: Implements **AES-256 encryption** and SSL for secure handling of sensitive data.

---

## 🛠️ **Tech Stack**

- **Languages & Libraries**: Python, OpenCV, Pytesseract, ReportLab, Flask, PyMongo, Pandas, NumPy
- **Database**: MongoDB  
- **UI Design (Prototype)**: Figma  
- **IDE**: Visual Studio Code

---

## 🧭 **Workflow Summary**

1. **Upload Certificate**: Scanned Grade 10 mark sheet is uploaded.
2. **Preprocessing**: Image quality enhanced via OpenCV (grayscale, blur, edge detection).
3. **OCR Extraction**: Text pulled using **Pytesseract**.
4. **Validation**: Cleaned and structured data is verified.
5. **Storage**: Student info stored in **MongoDB**.
6. **PDF Output**: Printable registration forms generated.
7. **Flask App**: Students interact with the system via a lightweight demo interface.

---

##  **Real-World Impact**

This system is highly relevant for institutions (especially in Nepal) digitizing their administrative workflows. It supports:
- Bulk document intake with higher speed and reliability
- Automated reporting and structured outputs
- Improved data quality and reduced operational overhead

---

## 🖼 **Sample Screenshots**

<p align="center">
  <img src="images/system_demo_1.png" width="45%" alt="OCR Screenshot">
  &nbsp;
  <img src="images/system_demo_2.png" width="45%" alt="Generated PDF Screenshot">
</p>

---

##  **Skills Demonstrated**

- **Python Development**: Built modular, reusable OCR + data pipeline.
- **Data Handling**: Designed validation logic for transforming unstructured input into structured output.
- **Database Skills**: Implemented CRUD operations using **MongoDB**.
- **Reporting**: Generated consistent outputs using **ReportLab**.
- **Security Awareness**: Applied AES-256 encryption and SSL.
- **Interface Prototyping**: Designed and deployed a simple Flask UI and wireframed UX in Figma.

---

## 🔧 **Future Enhancements**

- Admin dashboard for real-time application management
- Deep learning OCR models for better accuracy
- Mobile responsiveness and Nepali language support
- Centralized database integration for live verification

---

##  **Getting Started**

```bash
# Clone the repository
git clone https://github.com/purnimabohara/thesis-automated-college-registration.git
cd thesis-automated-college-registration

# (Optional) Set up virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app (for demo)
python flask_app/app.py
