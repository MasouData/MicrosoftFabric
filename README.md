# Microsoft Fabric DP-700 Hands-On Labs

<p align="center">
  <img src="https://debruyn.dev/fabric.png" alt="Microsoft Fabric Logo" width="300">
</p>

A practical learning repository for **Microsoft Fabric Data Engineer (DP-700)** preparation.

The goal of this repository is to complement theory with small hands-on exercises in **Microsoft Fabric Data Engineering, Real-Time Intelligence, OneLake, KQL, notebooks, and Git integration**.

> This repository is a learning environment and will grow as I continue preparing for DP-700.

---

## Current Fabric Items

| Item | Purpose |
|---|---|
| `First_demo_notebook.Notebook` | Practice with Fabric notebooks, PySpark, and Git/version-control workflows |
| `demo_lakehouse.Lakehouse` | Practice with Lakehouse concepts, OneLake, and Delta tables |
| `demoEventStream.Eventstream` | Real-time ingestion and transformation with Fabric Eventstream |
| `demoEventHouse.Eventhouse` | Store and query real-time data using Eventhouse / KQL |

---

## Real-Time Streaming Demo

One of the hands-on exercises streams **live CPU usage from a local computer** into Microsoft Fabric.

### Architecture

```text
Laptop CPU metrics
      |
      v
Python + psutil
      |
      v
Fabric Eventstream
Custom Endpoint
(Event Hubs-compatible)
      |
      v
Tumbling-window transformation
AVG(cpu_percent)
      |
      v
Eventhouse / KQL Database
      |
      v
KQL Table
```

### Example incoming event

```json
{
  "computer": "LAPTOP-XXXX",
  "cpu_percent": 17.9,
  "timestamp": "2026-09-13T20:22:59"
}
```

### Example transformed output

```text
computer        AVG_CPUUsage    Window_End_Time
-------------   ------------    -------------------
LAPTOP-XXXX     18.43           2026-09-13 20:23:00
```

The Eventstream uses a **tumbling window**, meaning each window has a fixed size and does not overlap with the next window.

---

## Concepts Practiced

### Real-Time Intelligence

- Eventstream sources and destinations
- Custom Endpoint ingestion
- Event Hubs-compatible endpoints
- JSON event ingestion
- Schema inference
- Eventstream retention
- Event throughput
- Filtering and field management
- Time-window aggregation
- Tumbling windows
- Eventhouse and KQL databases
- Streaming data into KQL tables

### Data Engineering

- Fabric Lakehouse
- OneLake
- Delta tables
- Fabric notebooks
- PySpark fundamentals

### Git / CI-CD

- Connecting a Fabric workspace to Git
- Tracking Fabric items in GitHub
- Commits and version history
- Reverting changes
- Understanding merge conflicts
- Maintaining repository documentation

---

## Quick DP-700 Notes

| Concept | Remember |
|---|---|
| **Eventstream** | Ingest, transform, and route streaming events |
| **Custom Endpoint** | Send events from your own application directly to Eventstream |
| **Event Hubs-compatible endpoint** | Lets producers use Event Hubs/Kafka-compatible connectivity without creating a separate Event Hub resource |
| **Tumbling window** | Fixed-size, non-overlapping windows |
| **Eventhouse** | Optimized storage and analytics for real-time/event data |
| **KQL Database** | Store and query Eventhouse data with KQL |
| **Lakehouse** | Combines data-lake flexibility with table-based analytics |
| **Retention** | How long Eventstream keeps events available |
| **Throughput** | Capacity for how much streaming data can flow through the Eventstream |
| **Schema** | Field names and data types that define an event's structure |

---

## Repository Structure

```text
MicrosoftFabric/
│
├── First_demo_notebook.Notebook/
│   └── Fabric notebook definition
│
├── demo_lakehouse.Lakehouse/
│   └── Fabric Lakehouse definition
│
├── demoEventStream.Eventstream/
│   └── Fabric Eventstream definition
│
├── demoEventHouse.Eventhouse/
│   └── Fabric Eventhouse definition
│
└── README.md
```

Fabric-generated folders represent items synchronized from the connected Fabric workspace.

---

## Next Hands-On Exercises

Planned exercises include:

- Build a Data Factory pipeline
- Practice Copy activity / Copy job
- Load batch data into a Lakehouse
- Apply Delta optimization techniques
- Practice OneLake shortcuts
- Query data with SQL and KQL
- Build a simple Medallion architecture
- Explore Eventstream → Eventhouse → dashboard workflows
- Practice deployment and Git-based CI/CD scenarios

---

## Useful Microsoft Documentation

- [Microsoft Fabric documentation](https://learn.microsoft.com/fabric/)
- [DP-700 study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/dp-700)
- [Microsoft Fabric Eventstreams](https://learn.microsoft.com/fabric/real-time-intelligence/event-streams/overview)
- [Microsoft Fabric Eventhouse](https://learn.microsoft.com/fabric/real-time-intelligence/eventhouse)
- [Microsoft Fabric Lakehouse](https://learn.microsoft.com/fabric/data-engineering/lakehouse-overview)
- [Fabric Git integration](https://learn.microsoft.com/fabric/cicd/git-integration/intro-to-git-integration)

---

## Purpose

This repository is primarily for:

- DP-700 exam preparation
- Hands-on Microsoft Fabric practice
- Recording experiments and learning progress
- Building a practical Fabric portfolio

---

**Status:** 🚧 Work in progress — continuously updated during DP-700 preparation.
