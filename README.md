# 🚀 EliteSearch: Premium Product Discovery

EliteSearch is a state-of-the-art product discovery platform built with **Django** and **Elasticsearch**. It features a lightning-fast search engine with fuzzy matching, intelligent autocomplete, and a premium **Glassmorphism** user interface.

![Modern UI Design](https://img.shields.io/badge/Design-Glassmorphism-blue)
![Search Speed](https://img.shields.io/badge/Search-Elasticsearch-green)
![Framework](https://img.shields.io/badge/Framework-Django-092E20)

---

## ✨ Key Features

- **🔍 Smart Autocomplete**: Real-time suggestions using Elasticsearch `edge_ngram` analyzer.
- **⚡ Fuzzy Full-Text Search**: Matches products even with typos or partial keywords.
- **🎨 Premium UI/UX**: Dark-themed glassmorphism design with smooth animations and responsive grid.
- **✨ Keyword Highlighting**: Visually highlights matched parts of words in the search recommendations.
- **📱 Fully Responsive**: Seamless experience across mobile, tablet, and desktop devices.

---

## 🛠️ Tech Stack

- **Backend**: Python, Django, Django Rest Framework (DRF)
- **Search Engine**: Elasticsearch 8.x
- **Integration**: Django Elasticsearch DSL
- **Frontend**: Vanilla HTML5, CSS3 (Custom Variables), JavaScript (ES6+)

---

## ⚙️ Setup & Installation

Follow these steps to get the project running locally.

### 1. Prerequisites
Ensure you have the following installed:
- **Python 3.12+**
- **Elasticsearch 8.x** (Started and running on `http://localhost:9200`)

## 🐳 Elasticsearch Setup Guide

### 🐧 For Ubuntu (Debian/Linux)
1. **Import GPG Key & Add Repo**:
   ```bash
   curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
   echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
   ```
2. **Install Elasticsearch**:
   ```bash
   sudo apt update && sudo apt install elasticsearch
   ```
3. **Start Service**:
   ```bash
   sudo systemctl start elasticsearch
   sudo systemctl enable elasticsearch
   ```
4. **Dev Configuration**: For local development, if you encounter connection issues, you may need to disable security features in `/etc/elasticsearch/elasticsearch.yml`:
   ```yaml
   xpack.security.enabled: false
   ```

### 🪟 For Windows
1. **Download**: Visit the [Official Download Page](https://www.elastic.co/downloads/elasticsearch) and download the `.zip` archive.
2. **Extract**: Unzip the folder to your preferred location (e.g., `C:\elasticsearch`).
3. **Run**: Open PowerShell or Command Prompt, navigate to the `bin` folder, and run:
   ```powershell
   .\elasticsearch.bat
   ```
4. **Access**: Once started, verify it's running by visiting `http://localhost:9200` in your browser.

### 2. Clone and Initialize Environment
```bash
# Clone the repository (if applicable)
# git clone <repo-url>
# cd "Elastic search"

# Create a virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py migrate
```

### 5. Elasticsearch Indexing
This project uses a custom autocomplete analyzer. You **must** rebuild the index to apply these configurations:
```bash
python manage.py search_index --rebuild --force
```

### 6. Run the Application
```bash
python manage.py runserver
```
Visit the app at: `http://127.0.0.1:8000/`

---

## 📂 Project Structure

- `core/`: Project settings and root URL configurations.
- `products/`: Main application containing search logic, models, and UI.
  - `documents.py`: Elasticsearch document definitions & custom analyzers.
  - `views.py`: Search API implementation with highlighting.
  - `templates/`: Premium glassmorphism frontend.

---

## 💡 Usage

1. **Start Typing**: Simply begin typing in the search bar. Suggestions will appear instantly.
2. **Keyboard Navigation**: Use the mouse or tap to select a suggestion.
3. **Responsive Cards**: Hover over product cards to see smooth lifting animations.

---

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---
*Developed with ❤️ by Antigravity*
