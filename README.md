# TeleLinks - Telegram Link Sharing Platform

<div align="center">

![TeleLinks](https://img.shields.io/badge/TeleLinks-Share%20Telegram%20Links-blue?style=for-the-badge&logo=telegram)
![Django](https://img.shields.io/badge/Django-5.2.7-green?style=for-the-badge&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=for-the-badge&logo=bootstrap)

*A modern platform for discovering and sharing Telegram channels, groups, and bots*

[![Features](https://img.shields.io/badge/Features-✨-yellow)](#features)
[![Demo](https://img.shields.io/badge/Demo-🚀-orange)](#demo)
[![Installation](https://img.shields.io/badge/Installation-📦-blue)](#installation)

</div>

## 🌟 Overview

TeleLinks is a feature-rich web application built with Django that allows users to discover, share, and organize Telegram links. Whether you're looking for communities, channels, or bots, TeleLinks provides a centralized platform to explore the vast Telegram ecosystem.

## ✨ Features

### 🔍 Discovery & Search
- **Advanced Search**: Find links by title, description, or category
- **Smart Filtering**: Filter by category, link type, and popularity
- **Sort Options**: Sort by recent, popular, or most liked content

### 👥 User Features
- **User Registration & Authentication**: Secure user accounts with customizable password policies
- **Personal Dashboard**: Manage your uploaded links in "My Links" section
- **Social Interactions**: Like posts and engage with comments
- **Bookmark System**: Save your favorite Telegram links

### 🛡️ Security & Moderation
- **Secure URLs**: Hash-based unique identifiers instead of sequential IDs
- **Content Moderation**: Admin verification system for links
- **Soft Delete**: Non-destructive deletion preserving data integrity
- **Spam Protection**: Robust comment and link moderation

### 🎨 User Experience
- **Dark Theme**: Eye-friendly dark interface with modern design
- **Responsive Design**: Optimized for desktop and mobile devices
- **Real-time Stats**: View counts, likes, and comments tracking
- **Related Links**: Smart recommendations based on categories

### 📱 Telegram Integration
- **URL Validation**: Automatic normalization of Telegram links
- **Link Previews**: Rich metadata display for shared links
- **Category System**: Organized content with emoji-enhanced categories

## 🚀 Demo

### Live Demo
*Coming soon!*

### Screenshots
| Home Page | Link Details | User Dashboard |
|-----------|-------------|----------------|
| ![Home](https://via.placeholder.com/400x250?text=Home+Page) | ![Details](https://via.placeholder.com/400x250?text=Link+Details) | ![Dashboard](https://via.placeholder.com/400x250?text=User+Dashboard) |

## 🛠️ Technology Stack

### Backend
- **Framework**: Django 5.2.7
- **Database**: SQLite (Development) / PostgreSQL (Production)
- **Authentication**: Django Auth System
- **Security**: CSRF Protection, XSS Protection

### Frontend
- **Styling**: Bootstrap 5.3 + Custom CSS
- **Icons**: Font Awesome 6.4
- **JavaScript**: Vanilla JS + jQuery
- **Rich Text**: CKEditor for content creation

### Additional Features
- **Pagination**: Efficient content loading
- **AJAX**: Smooth like/unlike functionality
- **URL Security**: Hash-based unique identifiers
- **Responsive Design**: Mobile-first approach

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtualenv (recommended)

### Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/telelinks.git
   cd telelinks
   ```

2. **Set up Virtual Environment**
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # Linux/Mac
   # OR
   myenv\Scripts\activate    # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

8. **Access the Application**
   ```
   http://localhost:8000
   ```

### Production Deployment

For production deployment, consider:
- Using PostgreSQL instead of SQLite
- Setting up proper environment variables
- Configuring static files with WhiteNoise
- Using Gunicorn as WSGI server
- Setting up Nginx reverse proxy

## 🗂️ Project Structure

```
telelinks/
├── link/                          # Main application
│   ├── models.py                 # Database models
│   ├── views.py                  # Application views
│   ├── urls.py                   # URL routing
│   ├── forms.py                  # Django forms
│   └── templates/                # HTML templates
├── static/                       # Static files
│   ├── css/                      # Stylesheets
│   ├── js/                       # JavaScript files
│   └── images/                   # Images and icons
├── media/                        # User uploaded files
├── requirements.txt              # Python dependencies
└── manage.py                    # Django management script
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file with the following variables:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
```

### Customization Options
- Modify categories in `models.py`
- Adjust pagination settings in views
- Customize styling in CSS files
- Configure email settings for notifications

## 🤝 Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

### Code Style
- Follow PEP 8 for Python code
- Use meaningful commit messages
- Add comments for complex logic
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please [open an issue](https://github.com/yourusername/telelinks/issues) on GitHub.

## 🙏 Acknowledgments

- Django community for the excellent framework
- Bootstrap team for the responsive CSS framework
- Telegram for the inspiration and API
- Contributors and testers who helped improve TeleLinks

## 📞 Support

Need help? 
- 📧 Email: support@telelinks.com
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/telelinks/discussions)
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/telelinks/issues)

---

<div align="center">

**⭐ Star this repo if you find it helpful!**

*Built with ❤️ using Django and Bootstrap*

[![GitHub stars](https://img.shields.io/github/stars/yourusername/telelinks?style=social)](https://github.com/yourusername/telelinks)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/telelinks?style=social)](https://github.com/yourusername/telelinks)

</div>
