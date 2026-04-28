# 🕷️ Web Scraping Automation Suite

> An intelligent **automated web scraping and monitoring system** built with Python, featuring advanced CAPTCHA solving, secure login automation, and intelligent notifications.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![License](https://img.shields.io/badge/license-MIT-blue)](#license)
[![Created](https://img.shields.io/badge/created-November%202023-brightgreen)]()
[![Last Updated](https://img.shields.io/badge/updated-September%202025-brightgreen)]()

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Module Documentation](#module-documentation)
- [How It Works](#how-it-works)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)
- [Security Considerations](#security-considerations)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## 🎯 Overview

**Web Scraping Automation Suite** is a production-ready Python application designed to automate complex web interactions. It specializes in:

- **Automated login workflows** with dynamic CAPTCHA solving
- **Real-time data extraction** from protected web pages
- **Intelligent monitoring** with conditional alerts
- **Email notification system** for status updates
- **Robust error handling** with retry mechanisms

This project is particularly useful for:
- License/subscription monitoring
- Automated data collection
- Regular web page monitoring
- Scheduled batch operations
- Alert systems for critical thresholds

### Use Case Example
Monitor a web application's license quantity and receive email alerts when licenses fall below a threshold, with automatic login handling and CAPTCHA solving.

---

## ✨ Features

### 🔐 Automated Login System
- **Selenium WebDriver** integration for browser automation
- **Dynamic element detection** using XPath and CSS selectors
- **Wait mechanisms** with configurable timeouts
- **Retry logic** with configurable attempt limits
- **Session management** and error recovery

### 🤖 Intelligent CAPTCHA Solving
- **Image preprocessing** with OpenCV
- **Tesseract OCR** for character recognition
- **Advanced image conversion** (grayscale, thresholding)
- **Configurable whitelist** for character sets
- **High accuracy** on alphanumeric CAPTCHAs

### 📊 Data Extraction
- **XPath navigation** through complex DOM structures
- **CSS selector** support for element targeting
- **Text parsing** and data type conversion
- **Multiple retry attempts** for reliability
- **Error handling** with graceful failures

### 🔔 Email Notification System
- **SMTP integration** (Office 365, Gmail, custom servers)
- **Template-based messages** in Spanish/English
- **Multiple notification types**:
  - Login failures with retry status
  - License threshold alerts
  - Custom messages
- **Secure credential handling** via YAML configuration

### ⚙️ Configuration Management
- **YAML-based configuration** for easy management
- **Separation of concerns** (credentials, endpoints, thresholds)
- **Environment variable support** for sensitive data
- **Hot-reloadable configuration** without restarts

---

## 💻 Tech Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Core Runtime** | Python | 3.8+ | Programming language |
| **Web Automation** | Selenium | 4.0+ | Browser automation |
| **Web Driver** | ChromeDriver | Latest | Browser control |
| **OCR Engine** | Tesseract | 5.0+ | CAPTCHA recognition |
| **Image Processing** | OpenCV | 4.5+ | Image manipulation |
| **Image Library** | Pillow | 8.0+ | Image operations |
| **Configuration** | PyYAML | 6.0+ | Config file parsing |
| **Email** | smtplib | Built-in | SMTP communications |

---

## 🏗️ Architecture
