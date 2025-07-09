
#  Lymphography Classification - Full Stack ML App

This is a full-stack machine learning project that classifies lymph node conditions using a trained decision tree model. It includes:

-  A Flask backend with a trained ML model
-  A React frontend with a medical form
-  Deployment-ready with a single public link via Render

---

##  Project Structure

```
lymphography-app/
├── backend/
│   ├── app.py                  # Flask API
│   ├── requirements.txt        # Python dependencies
│   └── lymphography_model.joblib  # Pre-trained ML model (placeholder)
├── frontend/
│   ├── src/
│   │   └── App.tsx             # React frontend code
│   └── package.json
└── render.yaml                 # Render deployment blueprint
```

---

##  Deployment Instructions (One Link for All)

### Step 1: Upload to GitHub
1. Create a new repo on GitHub (e.g., `lymphography-app`)
2. Push the contents of this folder to that repo.

### Step 2: Deploy with Render
1. Go to [https://render.com](https://render.com)
2. Click **New → Blueprint** (because we have a `render.yaml` file)
3. Connect your GitHub repo
4. Render will deploy both backend and frontend automatically 🎉

You’ll get a link like:
```
https://lymphography-app.onrender.com
```

 This one link shows the full working web app.

---

##  How It Works

- **Frontend** (`App.tsx`) contains a dropdown form for 18 medical features.
- **Backend** (`app.py`) receives the data, runs a prediction, and sends back the class.
- The frontend shows: `Class 1: Normal`, `Class 2: Inflamed`, etc.

---

##  Tech Stack

- Python, Flask, Pandas, Scikit-learn
- React, TypeScript
- Render (for fullstack hosting)
- GitHub (version control)

---

##  Notes

- You can replace `lymphography_model.joblib` with your trained model.
- If using real data, ensure it’s cleaned and preprocessed before training.
- Update the dropdown options in `App.tsx` if needed.

---

