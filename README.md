# Number Classification API

## 📌 Project Overview
This is a **public API** built using **FastAPI** that classifies numbers based on their mathematical properties and provides a fun fact.

### **Features:**
- Checks if a number is **prime**.
- Checks if a number is **perfect**.
- Checks if a number is **Armstrong**.
- Determines if a number is **even or odd**.
- Computes the **sum of digits**.
- Fetches a **fun fact** from [Numbers API](http://numbersapi.com/#42).

---

## 🚀 API Endpoints
### **1️⃣ Classify a Number**
**Endpoint:**
```
GET /api/classify-number?number=<integer>
```

**Example Request:**
```
GET https://number-api.vercel.app/api/classify-number?number=371
```

**Example Response:**
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

### **2️⃣ Health Check**
**Endpoint:**
```
GET /api/health
```

**Example Response:**
```json
{
    "status": "API is running"
}
```

---

## 🛠️ Local Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
```

### **2️⃣ Set Up a Virtual Environment**
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the API Server**
```sh
uvicorn main:app --reload
```

### **5️⃣ Test the API**
Open a browser or use Postman:
```
http://127.0.0.1:8000/api/classify-number?number=371
```

---

## 📦 Deployment (Vercel)
1. Push your code to **GitHub**:
```sh
git add .
git commit -m "Initial commit"
git push origin main
```
2. Deploy to **Vercel**:
   - Install Vercel CLI: `npm install -g vercel`
   - Run `vercel login` to authenticate
   - Navigate to the project folder and run `vercel`
   - Follow the prompts to deploy the project
   - Get the **Live URL** from the output

---

## 🤝 Hiring Information
Interested in hiring a **Python developer**?
🔗 [https://hng.tech/hire/python-developers](https://hng.tech/hire/python-developers)

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 👨‍💻 Author
- **Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: `your-email@example.com`

🔥 **Happy Coding!** 🚀

