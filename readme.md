# Multilingual FAQ Management System

A robust Django-based system for managing and serving Frequently Asked Questions (FAQs) in multiple languages. Built with performance in mind, this system leverages Redis caching and provides a RESTful API interface for seamless integration.

## Key Features 🚀

- Dynamic translation support for English, Hindi, Bengali, and French
- High-performance caching with Redis
- RESTful API endpoints with language-specific responses
- Rich text editing capabilities via CKEditor
- Customized Django admin panel for content management
- Comprehensive test suite
- Docker-ready deployment

## Technical Requirements

```
Python >= 3.10
Redis
Docker & Docker Compose (optional)
```

## Quick Start Guide

### Local Development Setup

1. Get the code:
```bash
git clone https://github.com/vanshchauhan1310/BharatFd-Task.git
cd BharatFd-Task
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Unix
.\venv\Scripts\activate   # Windows
```

3. Install dependencies and prepare database:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

4. Launch the application:
```bash
python manage.py runserver
```

### Docker Deployment

Deploy with containers:
```bash
docker-compose build
docker-compose up -d
```

## Managing FAQ Content

### Via Admin Interface

1. Access `http://localhost:8000/admin`
2. Navigate to FAQ section
3. Add new entries with:
   - Base language question & answer
   - Translations are auto-generated

### Via API

Base endpoint: `/api/faqs/`

Example request for French translation:
```bash
curl "http://localhost:8000/api/faqs/?lang=fr"
```

Sample Response:
```json
[
  {
    "question": "what is django ",
    "answer": "django ",
    "language": "hi"
  }
]
```

## Testing & Quality Assurance

Our test suite covers:
- FAQ creation validation
- Multi-language translation flows
- Caching mechanisms
- Fallback behaviors

Run tests with:
```bash
pytest faq/tests/
```

## Architecture Highlights

### Translation System
- Automatic translation via Google Translate API
- Redis-based caching (24-hour TTL)
- Fallback to English for unsupported languages

### Performance Optimizations
- Redis caching layer
- Efficient database queries
- Docker containerization

## Development Workflow

1. Create feature branch
2. Implement changes
3. Run test suite
4. Submit pull request
5. CI/CD pipeline handles deployment

## Troubleshooting

Common issues and solutions:

1. Redis Connection:
   - Verify Redis service is running
   - Check connection settings

2. Translation Issues:
   - Confirm language codes
   - Check API quotas
   - Verify cache status

## Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

