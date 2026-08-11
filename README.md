# 🎓 UCI CS Academic Advisor: A Narrow AI Project

A specialized Narrow AI agent built using **Alltius KNO+** to serve as a high-precision, instant knowledge assistant for Computer Science students at the University of California, Irvine (UCI).

## 💡 Origin & Motivation

My curiosity about Artificial Intelligence started through completing 3 different AI courses across **Google** and **IBM SkillsBuild**. Through those courses, I became fascinated by the inner mechanics of AI:
* How models are trained and how different training approaches impact performance.
* How LLMs process data to form responses.
* The root causes of **model hallucinations** and why standard models often state false facts with high confidence.
To move beyond theory and gain true hands-on experience, I decided to build my own **Narrow AI**—a targeted assistant built on **Alltius KNO+** to solve a personal challenge i had: navigating UCI’s vast number of websites on Computer Science degree requirements, prerequisites, and academic policies.

---

## 🛠️ The Development Journey: Failures & Data Engineering Insights

### Phase 1: The Raw Web Scraping Failure ❌
I initially started by feeding raw UCI website URLs directly into the Alltius platform. 
* **The Result:** The AI failed miserably. 
* **The Lesson:** Raw web pages contain excessive HTML noise, navigation bars, footers, and unstructured formatting that pollute the retrieval space and confuse the model.

### Phase 2: Data Cleaning & Modular Sources 🧹
Realizing the critical importance of **Data Quality and Preparation**, I manually extracted the necessary information directly from UCI catalogs and policy portals. I cleaned, structured, and organized the raw text into **4 distinct, curated pdf files**:

1. **`01_Compsci-Prereqs`** – Compsci courses offered with the description and pre-requisites.
2. **`02_UCI_CS`** – Add/Drop deadlines, P/NP grading limits, unit caps, and retake rules.
3. **`CS-26-27`** – Core degree requirements
4. **`LD & UD courses`** – Compulsory Lower Division and Upper Division Courses.

* **The Result:** The model’s response quality and factual accuracy improved immediately.

---
### 🔄 The Data Engineering Evolution: From Manual to Automated

1. **Initial Manual Ingestion:** I started by manually collecting and cleaning raw policy text into Markdown to test RAG response quality on Alltius KNO+.
2. **Recognizing the Automation Bottleneck:** I quickly realized that manual data extraction was inefficient, as it wouldn't scale as university catalogs and prerequisites update.
3. **Automated Pipeline via BeautifulSoup:** To automate any further data ingestion, I built a custom Python web scraper using `requests` and `BeautifulSoup4` (`scripts/scraper.py`). The script automatically fetches live UCI web pages, strips away HTML boilerplate (navbars, footers, scripts), and formats clean `.md` files which then only had to be converted to pdf and then uploaded, making the process quite efficient.
   
## 🔍 Key Findings & Current Work in Progress

### The Interim Solution: Graceful Link Fallbacks 🔗
While actively working on solving this multi-hop reasoning gap, I implemented a fallback system:
* Whenever the AI encounters a logical gap or cannot answer with 100% certainty from its files, it gracefully provides **direct official UCI links**. 
* This ensures the user is never left stranded with a dead end, always receiving a useful resource.

---

## 🚀 Final Result

I have successfully built a **functional Narrow AI working prototype** that performs direct information retrieval straight from verified source documents. 
Instead of opening dozens of browser tabs across multiple UCI websites, I can now query a single, fact-grounded assistant that consolidates complex academic policies into instant, direct answers.

---

## 👤 Author

* **Developer:** Natania Jim Rakesh
