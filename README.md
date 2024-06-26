# Harvest - Your Job Search Companion

[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Harvest is a web application designed to streamline the job search process. It provides a centralized platform for searching, saving, and tracking job applications.

## Features

- **Job Search:** Search for jobs from various sources (currently using the Adzuna API) using keywords.
- **Save Jobs:**  Save interesting job listings for later review.
- **Track Applications:** Keep track of your applications in different stages: Saved, Applied, In Progress.
- **User Profile:** Manage your profile information, including bio, location, and experience.
- **Clean and Intuitive UI:**  A modern and user-friendly interface for an efficient job search experience.

## Screenshots 

**Signup or login**
![Image of Signup/login page](Signup-login.png) 

**Homepage**
![Image of Home page](Home.png) 


## Technologies Used

- **Backend:**
    - Django
    - Django REST Framework
    - python-dotenv (for environment variables)
- **Frontend:**
    - Vue.js
    - Vuex (state management)
    - Vue Router (routing)
    - Axios (HTTP requests)
- **Other:**
    - Adzuna Job Search API
    - Font Awesome (icons)

## Prerequisites

- Python (3.x)
- Node.js and npm (or yarn)

## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/tshegofatsoseane/harvest
   cd harvest/backend    # Navigate to the backend directory

2. Set up a virtual environment:

        python3 -m venv env


3. Activate your virtual environment:

        source env/bin/activate


5. Install the Python dependencies:

        pip install -r requirements.txt


6. Create a .env file and set necessary secret keys below:

7. Apply migrations to create the database schema:

        python3 manage.py migrate

8. Start the development server: 
     ```
     python3 manage.py runserver
     ```

The API should now be running locally at [http://localhost:8000/](http://localhost:8000/).



## Frontend setup

1. **Navigate to the frontend directory**

   ```bash
   cd harvest/frontend_harvest_frontend

2. **Install frontend dependencies**

```
npm install
```

3. **Compiles and hot-reloads for development**
```
npm run serve
```

4. **Compiles and minifies for production**
```
npm run build
```

4. **Lints and fixes files**
```
npm run lint
```

The vue.js should now be running locally at http://localhost:8080/.

## Third-Party Licenses

This project utilizes the following third-party libraries and APIs:

- **Adzuna Job Search API:**
    - License: The Adzuna API is governed by its own Terms of Service. Please refer to the [Adzuna Developer Portal](https://developer.adzuna.com/overview) for details.
- **Django REST Framework Simple JWT:**
    - License: [MIT License](https://github.com/jazzband/djangorestframework-simplejwt/blob/master/LICENSE)


## License

This project (excluding third-party components) is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
