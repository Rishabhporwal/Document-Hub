# Document‑Hub

**Document‑Hub** is an AI-powered document intelligence platform that enables efficient information retrieval and processing across multiple file types using state-of-the-art LLMs, embeddings, and vector search techniques.

---

## 🌟 Why Document‑Hub?

Document‑Hub simplifies advanced retrieval and interaction over document corpora by combining powerful LLMs, embedding techniques, and scalable vector search in one modular, deployable package. Whether you're prototyping an AI assistant, building a knowledge management system, or enhancing search capabilities, Document‑Hub offers flexibility and ready-to-go integrations.

---

## 🚀 Features

* **Multi-Layered Architecture**

  * **API**: Expose endpoints via the `api/` directory.
  * **Core Processing**: Code in `src/`, `model/`, `utils/`, and `logger/` handles ingestion, parsing, embedding, and query logic.
  * **Prompt Management**: Explore and manage prompts within the `prompt/` directory.
  * **Notebooks**: Interactive Jupyter notebooks for demos, testing, or experimentation within `notebook/`.
  * **Templates & Frontend**: Includes HTML/CSS templates in `templates/` and frontend assets in `static/`.

* **Deployment-Ready**

  * Dockerized app via the included `Dockerfile`.
  * Streamlined package setup and dependency management with `setup.py` and `requirements.txt`.

* **Flexible AI Integrations**

  * Supports advanced LLMs: Groq, OpenAI, Gemini, Claude, Hugging Face, and Ollama (local).
  * Embedding models integrate with OpenAI, Gemini, or Hugging Face out-of-the-box.

* **Vector Database Agnostic**

  * Compatible with in-memory, on-disk, or cloud-based vector stores for adaptable deployment.

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/Rishabhporwal/Document-Hub.git
cd Document-Hub

# (Optional) Create and activate a virtual environment (e.g., via conda)
conda create -p env python=3.10 -y
conda activate env

# Install dependencies
pip install -r requirements.txt

# (Optional) Install as a package
python setup.py install
```

---

## ⚙️ Configuration

Copy and configure the environment:

```bash
cp .env.example .env
# Then open .env and add API keys and configuration values for your AI provider.
```

Customize via `.env` for settings like:

* Selected LLM provider (e.g., OpenAI, Groq, etc.)
* Chosen embedding model
* Vector database connection details
* Prompt templates and other logic parameters

---

## 📖 Usage Overview

1. Ingest documents using scripts or endpoints in `src/`, `api/`, or `notebook/`.
2. Documents are processed, embedded, and indexed into your chosen vector store.
3. Use the API or notebook to submit natural language queries.
4. Retrieve relevant results through vector similarity search.

---

## 📂 Directory Structure

```
Document‑Hub/
├── api/                // API endpoint implementations
├── src/                // Core logic for document ingestion & processing
├── model/              // AI model interfaces and integration
├── notebook/           // Jupyter notebooks for experimentation
├── prompt/             // Prompt templates & prompt-handling logic
├── templates/          // HTML templates
├── static/             // Frontend assets like CSS/JS
├── utils/, logger/, exception/ // Helpers and error handlers
├── config/, archive/   // Configuration files and backups
├── Dockerfile
├── .env.example
├── README.md           // You are here
├── setup.py
├── requirements.txt
└── versions.py
```

---

## 🤖 Supported AI Providers & Vector Stores

### LLM Options

| Provider     | Access Type       |
| ------------ | ----------------- |
| Groq         | Free              |
| OpenAI       | Paid              |
| Gemini       | 15-Day Free Trial |
| Claude       | Paid              |
| Hugging Face | Free              |
| Ollama       | Local Setup       |

### Embedding Models

* OpenAI
* Hugging Face
* Gemini

### Vector Databases

* In-memory (for lightweight testing)
* On-disk (local storage)
* Cloud-based (scalable use)

---

## 📜 Supported Document Types

* PDF
* TXT
* DOCX
* Markdown

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** the repo.
2. Create your **feature branch**: `git checkout -b feature/my-new-feature`.
3. Commit your changes: `git commit -m "Add awesome feature"`.
4. Push: `git push origin feature/my-new-feature`.
5. Open a **Pull Request** and describe your changes.


