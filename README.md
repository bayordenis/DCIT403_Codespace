# 📘 DCIT 403 – Lab 3

## Goals, Events, and Reactive Behavior

### Course

**DCIT 403 – Designing Intelligent Agents**
Department of Computer Science, University of Ghana

---

## 📌 Lab Objective

The objective of this laboratory is to model **agent goals** and implement **reactive behavior** using a **Finite State Machine (FSM)**. The lab demonstrates how an intelligent agent responds to environmental events by transitioning between different behavioral states.

---

## 🧠 Overview

This lab implements a **RescueAgent** within a simulated disaster environment. The agent:

* Perceives disaster events generated from the environment
* Assesses disaster severity
* Reacts by either performing rescue operations or remaining on standby

The implementation focuses on **event-driven decision-making** and **FSM-based control**, without requiring inter-agent communication.

---

## 🏗️ FSM States

The RescueAgent operates using the following FSM states:

* **IDLE** – Waiting for a disaster event
* **ASSESS** – Evaluating disaster severity
* **RESCUE** – Performing rescue operations for high-severity events
* **STANDBY** – Monitoring low-severity situations

State transitions are triggered by disaster severity levels.

---

## 📂 Project Structure

```text
Lab 3/
│── environment.py      # Simulated disaster environment
│── rescue_agent.py     # RescueAgent with FSM-based behavior
│── run_lab3.py         # Script to execute Lab 3 (offline mode)
│── README.md           # Lab documentation
```

---

## ▶️ How to Run

Ensure Python 3.9 or higher is installed.

From the Lab 3 directory, run:

```bash
python run_lab3.py
```

Expected output includes FSM state transitions such as:

```
[STATE] IDLE
[STATE] ASSESS
[STATE] RESCUE
Rescue completed.
```

---

## ⚙️ Environment Notes

* The lab runs in **offline mode** without XMPP networking.
* This is acceptable for Lab 3 since communication is introduced in later labs.
* The focus is strictly on **goals, events, and reactive behavior**.

---

## ✅ Learning Outcomes

By completing this lab, students demonstrate:

* Goal-oriented agent design
* Event-triggered reactive behavior
* FSM-based control in intelligent agents
* Practical understanding of agent autonomy

---

## 📎 Author

**Denis Bagresolzu Bayor**
Department of Computer Science
University of Ghana



