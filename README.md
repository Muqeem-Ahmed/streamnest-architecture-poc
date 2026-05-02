# StreamNest: Scalable Cloud Architecture & Data Lakehouse

## Project Overview
This repository contains a professional proof-of-concept (PoC) for modernizing the infrastructure of a large-scale video streaming platform, **StreamNest**. As the platform scaled to 2 million users, legacy systems faced deployment friction and data siloing.

This solution demonstrates a transition to a **containerized microservices architecture** and a **Data Lakehouse model** on Google Cloud Platform (GCP).

## Technical Architecture
* **Microservices Orchestration:** Google Kubernetes Engine (GKE) Autopilot for automated scaling and zero-downtime deployments.
* **Containerization:** Dockerized Python-based User Activity Logger API.
* **Data Ingestion:** Raw CSV event logs stored in Google Cloud Storage (GCS).
* **Analytics Engine:** BigQuery utilized as a Lakehouse layer to query external GCS data without ingestion overhead.

## Business Impact: Human-Centric Data Science
The primary objective was to bridge the gap between raw backend technical events and genuine human understanding. By centralizing logs in a queryable Lakehouse, the Data Science team can now:
1.  Analyze regional content performance in real-time.
2.  Understand device-specific engagement patterns (Mobile vs. SmartTV).
3.  Rapidly iterate on recommendation models using clean, structured data.

## Proof of Concept Results
* **Phase 1:** Successfully deployed a scalable API on GKE, verified via public endpoint.
* **Phase 2:** Automated ingestion of simulated watch events into GCS.
* **Phase 3:** Executed complex SQL transformations in BigQuery to answer critical business engagement questions.

---
*Developed as part of the CE-308 Cloud Computing Assignment.*
