# Full Stack Python Django and Vue Project

This is a full-stack project built with Python (Django) and Vue.js, designed to manage players' data. Users can perform CRUD (Create, Read, Update, Delete) operations on players' information.

## Getting Started

### Clone the Project

To get started, clone the project repository to your local machine:

```bash
git clone <repository-url>
```

# Set Up the Backend

- Navigate to the backend directory:

```bash
cd psl
```

- Create a virtual environment for Python:

```bash
python -m venv venv
```

- Activate the virtual environment:

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

- Install the required packages:

```bash
pip install -r requirements.txt
```

- Run the Django development server:

```bash
python manage.py runserver
```

# Set Up the Frontend

- Navigate to the frontend directory:

```bash
cd frontend
```

- Install the necessary dependencies:

```bash
npm install
```

- Start the Vue.js project:

```bash
npm run dev
```

### Now, you can perform CRUD operations on players' data through the application.

## NOTES:

- This project uses Tailwind CSS for styling but does not contain extensive custom styles.
- Some validations are added when users are adding or updating player information.
