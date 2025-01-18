# Notes Application 📒

This is a full-stack Notes Application designed to simplify note-taking and provide AI-powered features. The application has a React-based frontend and a Django REST framework backend.

## Features ✨

- **Note Management**: Create, read, update, and delete notes.
- **AI-Powered Features**:
  - 🧠 Generate ideas from text.
  - ✍️ Rewrite notes in a more descriptive way.
  - 🚀 Additional AI functionalities (coming soon).

---

## Folder Structure 🗂️

```
project-root/
|
|-- frontend/   # React application for the frontend
|   |-- public/
|   |-- src/
|   |-- package.json
|   |-- ...
|
|-- backend/    # Django application for the backend REST API
    |-- manage.py
    |-- backend/
    |-- requirements.txt
    |-- ...
```

### Frontend (React) ⚛️
The `frontend` folder contains the React application responsible for the user interface. It interacts with the backend API to fetch and store data.

### Backend (Django) 🐍
The `backend` folder contains the Django application. It serves as the API layer for managing notes and integrates AI features.

---

## Getting Started 🚀

Follow these instructions to set up and run the project locally.

### Prerequisites 📋

- **Node.js** (for the frontend)
- **Python 3.x** (for the backend)
- **Pip** and **virtualenv** (for Python dependencies)
- **OpenAI API Key** (or other AI API keys for AI functionalities)

---

### Setting Up 🛠️

#### Backend 🐍
1. Navigate to the `backend` folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

#### Frontend ⚛️
1. Navigate to the `frontend` folder:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm start
   ```

---

## API Endpoints 🔗

| Method | Endpoint         | Description              |
|--------|------------------|--------------------------|
| GET    | /api/notes/      | Fetch all notes          |
| POST   | /api/notes/      | Create a new note        |
| GET    | /api/notes/{id}/ | Fetch a specific note    |
| PUT    | /api/notes/{id}/ | Update a specific note   |
| DELETE | /api/notes/{id}/ | Delete a specific note   |

### AI Endpoints (Planned) 🤖
| Method | Endpoint            | Description                          |
|--------|---------------------|--------------------------------------|
| POST   | /api/ai/generate/   | 🧠 Generate ideas from text             |
| POST   | /api/ai/rewrite/    | ✍️ Rewrite text in a descriptive manner |

---

## Future Enhancements 🌟

- Advanced AI features like sentiment analysis and summarization.
- User authentication and note sharing.
- Enhanced frontend UI/UX design.

---

## Contributing 🤝

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License 📄

This project is licensed under the MIT License.

