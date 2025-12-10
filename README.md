# N'osairis Sight: IoT Terminal & Switch Monitor

> **N'osairis Sight** is the intelligent command center for your distributed IoT infrastructure, providing real-time visibility into the health and operational status of remote switches, terminal devices.

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)](https://github.com/cbalan30/nosairis-sight/actions)
[![Latest Release](https://img.shields.io/github/v/release/cbalan30/nosairis-sight?style=flat)](https://github.com/cbalan30/nosairis-sight/releases)
[![Tech Stack](https://img.shields.io/badge/Stack-Go%20%7C%20React%20%7C%20Kafka-orange)](docs/architecture.md)

---

## ✨ Key Features

* **Real-time Switch Status:** Instantly monitor the binary state (On/Off) and current/voltage draw of connected IoT power switches.
* **Terminal Output Logging:** Capture and stream terminal and console output from remote edge devices for live diagnostics and historical analysis.
* **Intelligent Alerting:** Define custom rules to trigger alerts (e.g., email, webhook, SMS) when a device fails to check in, or terminal logs contain specific error patterns (`FATAL`, `EXCEPTION`).
* **Time-Series Visualization:** Utilize a built-in dashboard (or Grafana integration) to visualize historical data (latency, switch uptime, power consumption).
* **Scalable Architecture:** Built on a microservices model designed to handle millions of simultaneous device connections (using Kafka/MQTT).

## 🚀 Quick Start (Installation)

The easiest way to get **N'osairis Sight** running is using Docker Compose.

### Prerequisites

* Docker (v20.10.0 or later)
* Docker Compose (v2.0.0 or later)

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YourOrg/nosairis-sight.git](https://github.com/YourOrg/nosairis-sight.git)
    cd nosairis-sight
    ```

2.  **Configure Environment Variables:**
    Copy the sample environment file and adjust necessary variables (e.g., database credentials, SMTP settings for alerts).

    ```bash
    cp .env.example .env
    # Edit the .env file with your specific settings
    ```

3.  **Start the Services:**
    This command will start the Core API, Message Broker (Kafka/Mosquitto), Time-Series Database, and the Web UI.

    ```bash
    docker-compose up -d
    ```

4.  **Access the Dashboard:**
    Open your browser to the following address:

    > 🌐 **`http://localhost:3000`**

---

## 💻 Technical Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Ingestion Layer** | Go (Golang) | High-concurrency service for low-latency device connection handling. |
| **Data Pipeline** | Apache Kafka / MQTT | Reliable, scalable message broker for buffering streaming data. |
| **Core API / Rules** | Java / Spring Boot | Manages user accounts, alerting rules, and device state. |
| **Database** | TimescaleDB (PostgreSQL) | Optimized Time-Series Database for metrics storage. |
| **Frontend** | React / TypeScript | Component-based, real-time web dashboard. |

## 🧩 Device Integration (The Client)

To connect an IoT device, you need to use our lightweight **N'osairis Agent** or publish directly to the MQTT broker.

### Publishing Switch Status (Example)

Devices can post JSON data to the ingestion endpoint:
```json
{
  "device_id": "Switch-001",
  "metric": "switch_status",
  "value": 1, 
  "timestamp": 1704067200
}
