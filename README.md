# IMBUTO – Youth Opportunity Intelligence Platform

## 1. Project Overview

IMBUTO is a youth opportunity intelligence platform designed to help young people in Rwanda turn their skills, interests, and limited financial resources into realistic business opportunities.

The platform provides information and practical decision-making tools that help aspiring entrepreneurs explore business ideas and understand the conditions that may influence their success.

## 2. Problem Statement

Many young people in Rwanda have the motivation and skills to start businesses but struggle to identify suitable opportunities, access relevant information, and make informed decisions with limited resources.

IMBUTO aims to bridge this gap by providing accessible, location-aware opportunity information and practical tools for exploring business ideas.

## 3. Main Features

- **Opportunity Explorer:** Explore business opportunities based on skills, interests, and available budget.
- **Opportunity Scoring:** Uses a scoring model to assess how well an opportunity matches a user's profile.
- **Financial Considerations:** Considers the user's available financial resources when assessing opportunities.
- **Environmental Intelligence:** Uses weather information to provide additional environmental context for selected locations.
- **Search and Filtering:** Allows users to search opportunities, filter by category, and sort results by score.

### IMBUTO Opportunity Score

The prototype uses a scoring model with a maximum of 100 points:

| Assessment area | Maximum points |
|---|---:|
| Skills match | 35 |
| Interests match | 25 |
| Financial suitability | 25 |
| Environmental factors | 15 |
| **Total** | **100** |

The score is an initial decision-support heuristic, not a guarantee of business success.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| HTML | Page structure |
| CSS | Website styling |
| JavaScript | Interactive features |
| Open-Meteo API | Weather information |
| Gunicorn | Python application server |
| Nginx | Web server and reverse proxy |
| HAProxy | Load balancing |
| Git and GitHub | Version control and project hosting |
| Ubuntu Linux | Server operating system |

## 5. External API Integration

IMBUTO integrates the Open-Meteo Weather API to retrieve current weather information for selected locations in Rwanda, including Kigali, Huye, Musanze, Rubavu, Rwamagana, and Muhanga.

The application uses weather information such as:
- Temperature
- Humidity
- Precipitation
- Wind speed

The retrieved information provides environmental context when exploring business opportunities.

**API provider:** [Open-Meteo](https://open-meteo.com/)

**API documentation:** [Open-Meteo API Documentation](https://open-meteo.com/en/docs)

Open-Meteo is the source of the weather data used by the application.

## 6. Project Structure

```text
IMBUTO/
│
├── app.py
├── requirements.txt
├── README.md
│
├── weather_services/
│   ├── __init__.py
│   └── weather.py
│
└── app/
    ├── templates/
    │   ├── index.html
    │   └── explore.html
    │
    └── static/
        ├── css/
        │   └── style.css
        └── js/
            └── main.js
```

## 7. Installation and Setup

### Requirements

- Python 3
- Git
- pip
- Virtual environment support

### Clone the repository

```bash
git clone https://github.com/Kayitarelibery/IMBUTO.git
cd IMBUTO
```

### Create a virtual environment

```bash
python3 -m venv venv
```

### Activate the environment

Linux/macOS:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open the local application using the address and port displayed by Flask in the terminal.

## 8. Deployment Architecture

IMBUTO is deployed using two web servers and one HAProxy load balancer.

### Infrastructure

- **Web Server 1:** Hosts the Flask application using Gunicorn and Nginx.
- **Web Server 2:** Hosts a second instance of the Flask application using Gunicorn and Nginx.
- **Load Balancer:** HAProxy receives incoming HTTPS requests and distributes them between the two web servers.
- **Domain:** https://liberytech.tech

### Request Flow

```text
             Users
               |
               v
       Domain: liberytech.tech
               |
               v
        HAProxy Load Balancer
          (HTTPS / Round Robin)
               |
          +----+----+
          |         |
          v         v
      Web Server 1  Web Server 2
          |         |
          v         v
        Nginx      Nginx
          |         |
          v         v
       Gunicorn   Gunicorn
          |         |
          v         v
        Flask     Flask
       IMBUTO     IMBUTO
```

### Load Balancing

HAProxy uses the round-robin algorithm to distribute incoming requests between the two web servers.

The configuration was tested by sending ten HTTPS requests through the load balancer. The responses alternated between Web Server 1 and Web Server 2, confirming that both servers were receiving traffic.

## 9. Testing and Verification

The deployment was verified through the following tests:

- Flask application successfully loaded on both web servers.
- Gunicorn services were confirmed active.
- Nginx successfully forwarded requests to Gunicorn.
- Both web servers returned HTTP 200 responses.
- HAProxy successfully distributed requests between both servers.
- Ten consecutive requests confirmed round-robin distribution.
- The public domain successfully displayed the IMBUTO homepage.

## 10. Future Improvements

Potential future improvements include:

- Expanding the business opportunity database.
- Improving the accuracy of the opportunity scoring model.
- Adding more location-specific business intelligence.
- Introducing additional financial planning tools.
- Improving the platform's user experience.
- Adding user accounts and personalized opportunity recommendations.

## 11. Project Purpose

IMBUTO aims to empower young people in Rwanda with accessible information and practical tools that encourage entrepreneurship, innovation, self-reliance, and sustainable economic development.

**Project:** IMBUTO – Youth Opportunity Intelligence Platform  
**Repository:** https://github.com/Kayitarelibery/IMBUTO.git  
**Live Website:** https://liberytech.tech
