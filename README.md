# N'osairis Sight: IoT Terminal & Switch Monitor

> **N'osairis Sight** is the intelligent command center for your distributed IoT infrastructure, providing real-time visibility into the health and operational status of remote switches, terminal devices.

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/cbalan30/nosairis-sight/actions)
[![Latest Release](https://img.shields.io/github/v/release/cbalan30/nosairis-sight?style=flat)](https://github.com/cbalan30/nosairis-sight/releases)
[![Tech Stack](https://img.shields.io/badge/Stack-Go%20%7C%20React%20%7C%20Kafka-orange)](docs/architecture.md)

---

## ✨ Key Features

* **Real-time Switch Status:** Instantly monitor the binary state (UP/DOWN) and connected switches.
* **Terminal Ping Results Logging:** Capture ping results for diagnostics and historical analysis.
* **Alerting:** Alert is triggered when the is detected to be DOWN.
* **Time-Series Visualization:** Visualize Switch status in graphical view.
* **Scalable Architecture:** Built on a microservices model designed to handle millions of simultaneous data entry (using REDIS and Celery).

## 📈 Workflow Diagram

![nosairis-sight-workflow](https://github.com/user-attachments/assets/acdabf03-5c7e-4e35-beab-caba83e408f9)


## 📈 Entity Relationship Diagram
<img width="800" height="500" alt="nosairis-sight-base-erd" src="https://github.com/user-attachments/assets/4413c9f0-1213-4061-8c17-2ef3f235620c" />


## 🚀 Quick Start (Installation & useful commands)

### Install Python
`sudo apt install python3`

### Python Version
`python3 --version`

### Create Virtual Environment
`python3 -m venv .venv`

### Activate Virtual Environment
`source .venv/bin/activate`

### Deactivate Virtual Environnt
`deactivate`

### Install Django framework
`python3 -m pip install Django`

### Check Django version
`python3 -m django --version`

### Re-applying changes to the projects/setting/etc.
`python3 manage.py migrate`

### Reload model changes
`python3 manage.py makemigrations`

### Apply model changes to DB
`python3 manage.py migrate core`

### Django shell console
`python3 manage.py shell`

### Django create App
`python3 manage.py startapp parser`

### Start Django Project
`django-admin startproject <project_name>`

### Start server
do this from main project folder
`python3 manage.py runserver`

### Install AdminLTE Template
`pip install django-adminlte3`

### Get AdminLTE static assets into project folder
`python3 manage.py collectstatic`

### create superuser
`python3 manage.py createsuperuser`

### Install Celery
`pip install celery redis`

### Install Redis
`sudo apt install redis-server`

### Start Redis
`/nosairis-sight/sightproject/ redis-server`

### Start Celery App
`/nosairis-sight/sightproject/ ../.venv/bin/celery -A celeryapp worker -l info`

### Start Server
`/mnt/d/projects/NOSAIRIS/repo/nosairis-sight/sightproject/ runserver`



## 💻 Screenshots

<img width="929" height="484" alt="screenshot01" src="https://github.com/user-attachments/assets/877e0804-ace9-4e2e-81a0-caf4fcc30b25" />

<img width="918" height="482" alt="screenshot02" src="https://github.com/user-attachments/assets/5e120e60-bf7c-4088-954d-6beb26d0e6dd" />

<img width="929" height="483" alt="screenshot03" src="https://github.com/user-attachments/assets/d96c1b6c-be0d-4a2a-9c9d-f657f655cf0d" />

<img width="929" height="483" alt="screenshot04" src="https://github.com/user-attachments/assets/0e71dcde-ce34-40b1-a7e3-58809593d1ac" />

<img width="830" height="409" alt="screenshot05" src="https://github.com/user-attachments/assets/42053fc6-9d7c-4eb6-8a6d-bbe59bcf8758" />

<img width="928" height="484" alt="screenshot06" src="https://github.com/user-attachments/assets/256acce2-3157-4480-bf03-a7fbbcf4e739" />

<img width="928" height="483" alt="screenshot07" src="https://github.com/user-attachments/assets/827a17f1-eb3d-41de-9d14-b18b0f2ed42b" />

<img width="927" height="484" alt="screenshot08" src="https://github.com/user-attachments/assets/d2070df2-1fed-41b2-b561-135024137501" />




