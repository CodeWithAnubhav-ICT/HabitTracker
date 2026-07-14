# 📊 Pixela Habit Tracker CLI (Day 37)

An interactive, menu-driven Command Line Interface (CLI) application built as part of the `#100DaysOfCode` Python challenge. This project interfaces with the **Pixela API** to log, modify, and manage daily habits using advanced HTTP methods (`POST`, `PUT`, `DELETE`) secured with custom header authentication.

Unlike static scripts, this version runs as a continuous interactive tool allowing dynamic record management in a single session.

---

## 🚀 Features

* **Full CRUD Operations:** Seamlessly interact with your tracking grid through HTTP requests:
  * **Create (`POST`):** Instantly log today's progress using automatic `datetime` formatting.
  * **Update (`PUT`):** Modify records for any specific past date (`YYYYMMDD`).
  * **Delete (`DELETE`):** Purge incorrect or unwanted entries completely from your history.
* **Continuous Runtime:** Structured with an operational loop allowing multiple modifications without script restarts.
* **Production-Ready Security:** Implements absolute separation of concerns by pulling API keys and personal tokens from environment variables rather than hardcoding credentials.

---

## 🛠️ API Architecture Mapping

The script translates user terminal choices into standardized RESTful API actions:

| Operation | HTTP Method | Endpoint Target | Purpose |
| :--- | :--- | :--- | :--- |
| **Default Input** | `POST` | `/v1/users/<user>/graphs/<graph>` | Creates/commits a new tracking pixel for today |
| **"update"** | `PUT` | `/v1/users/<user>/graphs/<graph>/<date>` | Overwrites quantity data for a given date |
| **"delete"** | `DELETE` | `/v1/users/<user>/graphs/<graph>/<date>` | Permanently removes pixel data for a given date |

---

## 📦 Setup & Environment Variables

### 1. Prerequisites
Ensure you have the `requests` library installed:
```bash
pip install requests
