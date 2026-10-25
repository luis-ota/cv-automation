# -*- coding: utf-8 -*-
"""Gera os 14 currículos específicos atualizados (7 ptbr + 7 ingles)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gen_docx_base import *

GH = "https://github.com/luis-ota/"
ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "output" / "docx"

# =============================================================================
# 1) C# BACKEND
# =============================================================================
sum_cs_pt = ("Desenvolvedor Backend C# com experiência em ASP.NET Core e Entity Framework Core. "
             "Conhecimento em microsserviços com RabbitMQ, MongoDB e PostgreSQL. "
             "Experiência também em Python, Rust e TypeScript. Estudante de Engenharia de Software "
             "pela PUCPR, com conclusão prevista para dezembro de 2026.")
sum_cs_en = ("C# Backend Developer experienced in ASP.NET Core and Entity Framework Core. Knowledge of "
             "microservices with RabbitMQ, MongoDB and PostgreSQL. Also experienced in Python, Rust and "
             "TypeScript. Software Engineering student at PUCPR, expected graduation December 2026.")

proj_cs_pt = [
    ("Medica.ly", "Projeto Universitário - PUCPR", None, None, [
        "Aplicação web para agendamento de consultas médicas com ASP.NET Core, C# e PostgreSQL.",
        "Frontend em Angular 12 com Angular Material e design responsivo; CRUD completo e autenticação de usuários.",
        "Containerização com Docker e autenticação com Supabase Auth."]),
    ("Sistema EPI Biométrico", "Serdia", None, None, [
        "Sistema embarcado em Raspberry Pi com autenticação biométrica (sensor UART + Python) para validação de segurança eletrostática antes do acesso às linhas de produção.",
        "Sincronização SQLite/PostgreSQL e API REST para monitoramento em tempo real, eliminando registros em papel."]),
    ("Sistema de Chamados Internos", "Serdia", None, None, [
        "CRUD completo com Next.js, TypeScript e PostgreSQL, com cronômetro independente, gerenciamento de usuários e mapa interativo da fábrica."]),
    ("Crabchat", "Rust", "github.com/luis-ota/crabchat-server", GH + "crabchat-server", [
        "Servidor de chat multi-threaded com Tokio para I/O assíncrona, autenticação de usuários e WebSockets."]),
]
proj_cs_en = [
    ("Medica.ly", "University Project - PUCPR", None, None, [
        "Web application for medical appointment scheduling built with ASP.NET Core, C# and PostgreSQL.",
        "Angular 12 frontend with Angular Material and responsive design; full CRUD and user authentication.",
        "Docker containerization and Supabase Auth integration."]),
    ("Biometric PPE System", "Serdia", None, None, [
        "Raspberry Pi embedded system with biometric authentication (UART sensor + Python) to validate electrostatic safety before access to production lines.",
        "SQLite/PostgreSQL synchronization and REST API for real-time monitoring, replacing paper logs."]),
    ("Internal Ticketing System", "Serdia", None, None, [
        "Full CRUD with Next.js, TypeScript and PostgreSQL, including an independent timer, user management and an interactive factory map."]),
    ("Crabchat", "Rust", "github.com/luis-ota/crabchat-server", GH + "crabchat-server", [
        "Multi-threaded chat server with Tokio for async I/O, user authentication and WebSockets."]),
]

skills_cs_pt = [
    ("Linguagens", "C#, Python, Rust, TypeScript/JavaScript"),
    ("Frameworks .NET", "ASP.NET Core, Entity Framework Core, LINQ, Blazor"),
    ("Outros Frameworks", "FastAPI, Django, Node.js, Spring Boot"),
    ("Bancos de Dados", "PostgreSQL, SQL Server, MongoDB, SQLite, MySQL"),
    ("Mensageria", "RabbitMQ, filas de requisições assíncronas"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Arquitetura", "Microsserviços, APIs RESTful, Clean Architecture, SOLID, DDD"),
    ("Sistemas", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_cs_en = [
    ("Languages", "C#, Python, Rust, TypeScript/JavaScript"),
    (".NET Frameworks", "ASP.NET Core, Entity Framework Core, LINQ, Blazor"),
    ("Other Frameworks", "FastAPI, Django, Node.js, Spring Boot"),
    ("Databases", "PostgreSQL, SQL Server, MongoDB, SQLite, MySQL"),
    ("Messaging", "RabbitMQ, async request queues"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Architecture", "Microservices, RESTful APIs, Clean Architecture, SOLID, DDD"),
    ("Systems", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# 2) DATA DEVELOPER
# =============================================================================
sum_data_pt = ("Desenvolvedor de Dados com experiência prática em pipelines ETL, automação de processos e "
               "otimização de consultas SQL. Atuação com Python (Pandas, Openpyxl, Flask), PostgreSQL, "
               "MongoDB e integração de fontes de dados diversas. Vivência com IA aplicada a dados: RAG, "
               "embeddings e indexação vetorial (Hackathon UFPR 2025). Interesse em Data Engineering, BI e "
               "Machine Learning. Estudante de Engenharia de Software pela PUCPR, com conclusão prevista "
               "para dezembro de 2026.")
sum_data_en = ("Data Developer with hands-on experience in ETL pipelines, process automation and SQL query "
               "optimization. Works with Python (Pandas, Openpyxl, Flask), PostgreSQL, MongoDB and the "
               "integration of diverse data sources. Hands-on with AI applied to data: RAG, embeddings and "
               "vector indexing (UFPR Hackathon 2025). Interested in Data Engineering, BI and Machine "
               "Learning. Software Engineering student at PUCPR, expected graduation December 2026.")

proj_data_pt = [
    ("Dashboard e Agente de Análise de Dados", "Hackathon UFPR 2025", "github.com/luis-ota/hackathon-ufpr-dados-2025",
     GH + "hackathon-ufpr-dados-2025", [
        "Dashboard em Streamlit para exploração de planilhas Excel e CSV, com visualizações e relatórios interativos.",
        "Agente híbrido (RAG + análise) com Gemini e LlamaIndex: cálculos e rankings com Pandas, busca semântica por embeddings e indexação vetorial de PDFs, planilhas e CSVs.",
        "Pipeline de indexação com barra de progresso e persistência do índice em disco para carregamento instantâneo."]),
    ("Pipeline ETL Automatizado", "Projeto Interno - Serdia", None, None, [
        "Pipeline ETL em Python com Pandas para consolidação de dados de produção, validação de integridade e geração automática de relatórios em Excel e PostgreSQL.",
        "Automação de processo que levava 3 dias, reduzido para 1-2 minutos com ganho de eficiência superior a 99%."]),
    ("Dashboard de Chamados Técnicos", "Projeto Interno - Serdia", None, None, [
        "Sistema de gestão de chamados com Next.js, TypeScript e PostgreSQL; dashboard com métricas de tempo de resposta, filtros por setor e mapa interativo da empresa."]),
]
proj_data_en = [
    ("Data Dashboard and Analysis Agent", "UFPR Hackathon 2025", "github.com/luis-ota/hackathon-ufpr-dados-2025",
     GH + "hackathon-ufpr-dados-2025", [
        "Streamlit dashboard for exploring Excel and CSV spreadsheets, with interactive visualizations and reports.",
        "Hybrid agent (RAG + analysis) with Gemini and LlamaIndex: calculations and rankings with Pandas, embedding-based semantic search and vector indexing of PDFs, spreadsheets and CSVs.",
        "Indexing pipeline with progress reporting and on-disk index persistence for instant loading."]),
    ("Automated ETL Pipeline", "Internal Project - Serdia", None, None, [
        "ETL pipeline in Python with Pandas for production data consolidation, integrity validation and automated report generation in Excel and PostgreSQL.",
        "Automated a 3-day process down to 1-2 minutes, with a 99%+ efficiency gain."]),
    ("Technical Ticketing Dashboard", "Internal Project - Serdia", None, None, [
        "Ticketing management system with Next.js, TypeScript and PostgreSQL; dashboard with response-time metrics, sector filters and an interactive company map."]),
]

skills_data_pt = [
    ("Linguagens", "Python, SQL, Rust, TypeScript/JavaScript"),
    ("Bibliotecas de Dados", "Pandas, NumPy, Openpyxl, Matplotlib, SQLAlchemy"),
    ("Bancos de Dados", "PostgreSQL, MongoDB, SQLite, MySQL, Firebase"),
    ("ETL e Pipelines", "Extração, transformação e carga com Python e Pandas; validação de integridade"),
    ("IA e Busca", "Embeddings, indexação vetorial, RAG (LlamaIndex), LLMs"),
    ("APIs", "Flask, FastAPI, Django, APIs RESTful para exposição de dados"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Sistemas", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_data_en = [
    ("Languages", "Python, SQL, Rust, TypeScript/JavaScript"),
    ("Data Libraries", "Pandas, NumPy, Openpyxl, Matplotlib, SQLAlchemy"),
    ("Databases", "PostgreSQL, MongoDB, SQLite, MySQL, Firebase"),
    ("ETL and Pipelines", "Extraction, transformation and loading with Python and Pandas; integrity validation"),
    ("AI and Search", "Embeddings, vector indexing, RAG (LlamaIndex), LLMs"),
    ("APIs", "Flask, FastAPI, Django, RESTful APIs for data exposure"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Systems", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# 3) FLUTTER / MOBILE
# =============================================================================
sum_fl_pt = ("Desenvolvedor Mobile com experiência em Flutter (Dart) e React Native/Expo. Projetos "
             "publicados com integração Firebase, notificações push, builds distribuídos e pagamentos via "
             "Pix. Vivência com backend Python (Flask, FastAPI). Estudante de Engenharia de Software pela "
             "PUCPR, com conclusão prevista para dezembro de 2026.")
sum_fl_en = ("Mobile Developer experienced in Flutter (Dart) and React Native/Expo. Published projects with "
             "Firebase integration, push notifications, distributed builds and Pix payments. Hands-on with "
             "Python backend (Flask, FastAPI). Software Engineering student at PUCPR, expected graduation "
             "December 2026.")

proj_fl_pt = [
    ("App de Gestão de Fretes (Flutter)", "Flutter, Firebase", "github.com/luis-ota/AppTransportadora",
     GH + "AppTransportadora", [
        "Aplicativo móvel multiplataforma para empresa de transportes: rastreamento de remessas, gestão de entregas e notificações push.",
        "Integração com Firebase Auth e Firestore; builds distribuídos via tags Git."]),
    ("Vitrines", "Expo / React Native", None, None, [
        "App mobile de vitrine de produtos digitais para criadores venderem pelo link da bio, compartilhando validação e tipos com o app web via monorepo."]),
]
proj_fl_en = [
    ("Freight Management App (Flutter)", "Flutter, Firebase", "github.com/luis-ota/AppTransportadora",
     GH + "AppTransportadora", [
        "Cross-platform mobile app for a transport company: shipment tracking, delivery management and push notifications.",
        "Firebase Auth and Firestore integration; builds distributed via Git tags."]),
    ("Vitrines", "Expo / React Native", None, None, [
        "Mobile app for a creator storefront selling digital products via bio link, sharing validation and types with the web app through a monorepo."]),
]

skills_fl_pt = [
    ("Mobile", "Flutter (Dart), React Native, Expo"),
    ("Linguagens", "Dart, JavaScript/TypeScript, Python"),
    ("Firebase", "Auth, Firestore, Realtime Database, Push Notifications"),
    ("Backend", "Node.js, Python (Flask, FastAPI)"),
    ("Bancos de Dados", "PostgreSQL, MongoDB, SQLite, Firebase"),
    ("Frontend", "React, Next.js, Tailwind CSS"),
    ("Pagamentos", "Pix, cartão de crédito, assinaturas"),
    ("DevOps", "Docker, GitHub Actions, Vercel, CI/CD"),
    ("Sistemas", "Linux (Arch, Ubuntu), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_fl_en = [
    ("Mobile", "Flutter (Dart), React Native, Expo"),
    ("Languages", "Dart, JavaScript/TypeScript, Python"),
    ("Firebase", "Auth, Firestore, Realtime Database, Push Notifications"),
    ("Backend", "Node.js, Python (Flask, FastAPI)"),
    ("Databases", "PostgreSQL, MongoDB, SQLite, Firebase"),
    ("Frontend", "React, Next.js, Tailwind CSS"),
    ("Payments", "Pix, credit card, subscriptions"),
    ("DevOps", "Docker, GitHub Actions, Vercel, CI/CD"),
    ("Systems", "Linux (Arch, Ubuntu), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# 4) FULL STACK
# =============================================================================
sum_fs_pt = ("Desenvolvedor Full-Stack com atuação em backend Python/Rust e frontend React/Next.js. "
             "Experiência em APIs RESTful, bancos relacionais e NoSQL (PostgreSQL, MongoDB), automação de "
             "processos e produtos com cobrança recorrente (Pix e cartão). Vivência com IA: LLMs, RAG, "
             "agentes ReAct e Tool Calling. Estudante de Engenharia de Software pela PUCPR, com conclusão "
             "prevista para dezembro de 2026.")
sum_fs_en = ("Full-Stack Developer working with Python/Rust backends and React/Next.js frontends. "
             "Experience in RESTful APIs, relational and NoSQL databases (PostgreSQL, MongoDB), process "
             "automation and products with recurring billing (Pix and card). Hands-on with AI: LLMs, RAG, "
             "ReAct agents and tool calling. Software Engineering student at PUCPR, expected graduation "
             "December 2026.")

proj_fs_pt = [
    ("Vitrines", "Next.js + Expo, pagamentos Pix", None, None, [
        "SaaS para criadores transformarem o link da bio em vitrine de produtos digitais: monorepo Bun com Next.js e app Expo.",
        "Autenticação por organizações, cobrança por assinatura e cartão, Pix com ledger de criadores e payouts, jobs em background (Inngest), i18n e deploy self-hosted com Docker Compose e Caddy."]),
    ("ai.ther", "Open-source (AGPL), produto operado", None, None, [
        "Plataforma open-source de agendamento e publicação em redes sociais com copiloto de IA, publicação nativa em 12 redes e servidor MCP para assistentes de IA.",
        "Opero a instância em produção, incluindo autenticação social, conexão de contas e o fluxo completo de publicação."]),
    ("Análise Inteligente de Dados", "Hackathon UFPR 2025", "github.com/luis-ota/hackathon-ufpr-dados-2025",
     GH + "hackathon-ufpr-dados-2025", [
        "Agente ReAct com Tool Calling para análise de dados e busca semântica; RAG com embeddings e indexação vetorial de PDFs, CSVs e planilhas; dashboards interativos em Streamlit."]),
    ("Medica.ly", "Projeto Universitário - PUCPR", None, None, [
        "Aplicação full stack para gestão de consultas médicas: APIs REST em ASP.NET Core, autenticação com Supabase Auth e modelagem PostgreSQL; interface responsiva em Angular Material."]),
]
proj_fs_en = [
    ("Vitrines", "Next.js + Expo, Pix payments", None, None, [
        "SaaS that turns a creator's bio link into a digital-product storefront: Bun monorepo with Next.js and an Expo app.",
        "Organization-based auth, subscription and card billing, Pix with creator ledger and payouts, background jobs (Inngest), i18n and self-hosted deployment with Docker Compose and Caddy."]),
    ("ai.ther", "Open-source (AGPL), operated product", None, None, [
        "Open-source social media scheduling platform with an AI copilot, native publishing to 12 networks and an MCP server for AI assistants.",
        "Operate the production instance, including social auth, account connections and the complete publishing pipeline."]),
    ("Intelligent Data Analysis", "UFPR Hackathon 2025", "github.com/luis-ota/hackathon-ufpr-dados-2025",
     GH + "hackathon-ufpr-dados-2025", [
        "ReAct agent with Tool Calling for data analysis and semantic search; RAG with embeddings and vector indexing for PDFs, CSVs and spreadsheets; interactive Streamlit dashboards."]),
    ("Medica.ly", "University Project - PUCPR", None, None, [
        "Full-stack medical appointment management app: REST APIs in ASP.NET Core, Supabase Auth and PostgreSQL modeling; responsive Angular Material interface."]),
]

skills_fs_pt = [
    ("Linguagens", "Python, TypeScript/JavaScript, Rust, Dart, C#"),
    ("Backend", "FastAPI, Django, Flask, Node.js, Axum, ASP.NET Core"),
    ("Frontend", "React, Next.js, Angular, Tailwind CSS"),
    ("Mobile", "Flutter (Dart), React Native, Expo"),
    ("Bancos de Dados", "PostgreSQL, MongoDB, SQLite, MySQL, Firebase, Redis"),
    ("IA", "LLMs, RAG, Tool Calling, agentes ReAct, LlamaIndex, embeddings"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, Vercel, CI/CD"),
    ("Arquitetura", "Microsserviços, APIs RESTful, Clean Architecture, SOLID"),
    ("Sistemas", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_fs_en = [
    ("Languages", "Python, TypeScript/JavaScript, Rust, Dart, C#"),
    ("Backend", "FastAPI, Django, Flask, Node.js, Axum, ASP.NET Core"),
    ("Frontend", "React, Next.js, Angular, Tailwind CSS"),
    ("Mobile", "Flutter (Dart), React Native, Expo"),
    ("Databases", "PostgreSQL, MongoDB, SQLite, MySQL, Firebase, Redis"),
    ("AI", "LLMs, RAG, tool calling, ReAct agents, LlamaIndex, embeddings"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, Vercel, CI/CD"),
    ("Architecture", "Microservices, RESTful APIs, Clean Architecture, SOLID"),
    ("Systems", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# 5) JAVA BACKEND
# =============================================================================
sum_java_pt = ("Desenvolvedor Backend com experiência em Java, Spring Boot e integração de sistemas. "
               "Conhecimento em microsserviços com RabbitMQ, MongoDB e PostgreSQL. Experiência também com "
               "Python (backend e automação) e Rust (sistemas). Estudante de Engenharia de Software pela "
               "PUCPR, com conclusão prevista para dezembro de 2026.")
sum_java_en = ("Backend Developer experienced in Java, Spring Boot and systems integration. Knowledge of "
               "microservices with RabbitMQ, MongoDB and PostgreSQL. Also experienced with Python (backend "
               "and automation) and Rust (systems). Software Engineering student at PUCPR, expected "
               "graduation December 2026.")

proj_java_pt = [
    ("Medica.ly", "Projeto Universitário - PUCPR", None, None, [
        "Aplicação web para agendamento de consultas médicas com ASP.NET Core e PostgreSQL; CRUD completo, autenticação de usuários e frontend Angular 12."]),
    ("Crabchat", "Rust", "github.com/luis-ota/crabchat-server", GH + "crabchat-server", [
        "Servidor de chat multi-threaded com Tokio para I/O assíncrona, autenticação de usuários, salas e WebSockets, com cliente de terminal."]),
    ("Sistema de Chamados Internos", "Serdia", None, None, [
        "CRUD completo com Next.js, TypeScript e PostgreSQL, com cronômetro independente, gerenciamento de usuários e mapa interativo da fábrica."]),
    ("Big Data com Hadoop", "Projeto Acadêmico", None, None, [
        "Processamento distribuído de dados com Hadoop (HDFS e MapReduce) e Java, aplicado a exercícios de análise em larga escala."]),
]
proj_java_en = [
    ("Medica.ly", "University Project - PUCPR", None, None, [
        "Medical appointment scheduling web application with ASP.NET Core and PostgreSQL; full CRUD, user authentication and Angular 12 frontend."]),
    ("Crabchat", "Rust", "github.com/luis-ota/crabchat-server", GH + "crabchat-server", [
        "Multi-threaded chat server with Tokio for async I/O, user authentication, rooms and WebSockets, with a terminal client."]),
    ("Internal Ticketing System", "Serdia", None, None, [
        "Full CRUD with Next.js, TypeScript and PostgreSQL, including an independent timer, user management and an interactive factory map."]),
    ("Big Data with Hadoop", "Academic Project", None, None, [
        "Distributed data processing with Hadoop (HDFS and MapReduce) and Java, applied to large-scale analysis exercises."]),
]

skills_java_pt = [
    ("Linguagens", "Java, Python, Rust, TypeScript/JavaScript"),
    ("Frameworks Backend", "Spring Boot, JPA/Hibernate, Django, Flask, Node.js"),
    ("Bancos de Dados", "PostgreSQL, MongoDB, SQLite, MySQL"),
    ("Mensageria", "RabbitMQ, filas de requisições assíncronas"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Arquitetura", "Microsserviços, APIs RESTful, Clean Architecture, SOLID"),
    ("Estrutura de Dados", "Algoritmos de busca, Árvores, Grafos direcionados"),
    ("Sistemas", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_java_en = [
    ("Languages", "Java, Python, Rust, TypeScript/JavaScript"),
    ("Backend Frameworks", "Spring Boot, JPA/Hibernate, Django, Flask, Node.js"),
    ("Databases", "PostgreSQL, MongoDB, SQLite, MySQL"),
    ("Messaging", "RabbitMQ, async request queues"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Architecture", "Microservices, RESTful APIs, Clean Architecture, SOLID"),
    ("Data Structures", "Search algorithms, Trees, Directed graphs"),
    ("Systems", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# 6) PYTHON BACKEND
# =============================================================================
sum_py_pt = ("Desenvolvedor Backend Python com experiência prática em APIs RESTful, microsserviços e "
             "automação de processos. Atuação em produção com FastAPI, Django e Flask. Conhecimento em "
             "RabbitMQ, MongoDB e PostgreSQL. Vivência com IA: LLMs, RAG, agentes ReAct e Tool Calling "
             "em projetos próprios e de hackathon. Estudante de Engenharia de Software pela PUCPR, com "
             "conclusão prevista para dezembro de 2026.")
sum_py_en = ("Python Backend Developer with hands-on experience in RESTful APIs, microservices and process "
             "automation. Production experience with FastAPI, Django and Flask. Knowledge of RabbitMQ, "
             "MongoDB and PostgreSQL. Hands-on with AI: LLMs, RAG, ReAct agents and tool calling in "
             "personal and hackathon projects. Software Engineering student at PUCPR, expected graduation "
             "December 2026.")

proj_py_pt = [
    ("Análise Inteligente de Dados", "Hackathon UFPR 2025", "github.com/luis-ota/hackathon-ufpr-dados-2025",
     GH + "hackathon-ufpr-dados-2025", [
        "Agente ReAct com Tool Calling para análise de dados e busca semântica; RAG com embeddings e indexação vetorial de PDFs, CSVs e planilhas; dashboards em Streamlit."]),
    ("Wired Leads", "SaaS em produção", None, None, [
        "SaaS de prospecção e inteligência comercial: encontra negócios locais via Google Maps, detecta oportunidades digitais e gera abordagens personalizadas com IA configurável pelo usuário (BYOK).",
        "Começou como bot de Telegram e evoluiu para SaaS completo com interface web FastAPI, autenticação e deploy contínuo em produção."]),
]
proj_py_en = [
    ("Intelligent Data Analysis", "UFPR Hackathon 2025", "github.com/luis-ota/hackathon-ufpr-dados-2025",
     GH + "hackathon-ufpr-dados-2025", [
        "ReAct agent with Tool Calling for data analysis and semantic search; RAG with embeddings and vector indexing of PDFs, CSVs and spreadsheets; Streamlit dashboards."]),
    ("Wired Leads", "Production SaaS", None, None, [
        "Prospecting and sales-intelligence SaaS: finds local businesses via Google Maps, detects digital opportunities and generates personalized outreach with user-configured AI (BYOK).",
        "Started as a Telegram bot and evolved into a complete SaaS with a FastAPI web interface, authentication and continuous deployment in production."]),
]

skills_py_pt = [
    ("Linguagens", "Python, Rust, TypeScript/JavaScript, SQL"),
    ("Frameworks", "FastAPI, Django, Flask, Node.js"),
    ("Bibliotecas", "Pandas, Openpyxl, SQLAlchemy, Streamlit, Pydantic"),
    ("IA", "LLMs, RAG, agentes ReAct, Tool Calling, LlamaIndex, embeddings, Gemini, Llama 3"),
    ("Bancos de Dados", "PostgreSQL, MongoDB, SQLite, MySQL"),
    ("Mensageria", "RabbitMQ, filas de requisições assíncronas"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Arquitetura", "Microsserviços, APIs RESTful, Clean Architecture"),
    ("Sistemas", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_py_en = [
    ("Languages", "Python, Rust, TypeScript/JavaScript, SQL"),
    ("Frameworks", "FastAPI, Django, Flask, Node.js"),
    ("Libraries", "Pandas, Openpyxl, SQLAlchemy, Streamlit, Pydantic"),
    ("AI", "LLMs, RAG, ReAct agents, tool calling, LlamaIndex, embeddings, Gemini, Llama 3"),
    ("Databases", "PostgreSQL, MongoDB, SQLite, MySQL"),
    ("Messaging", "RabbitMQ, async request queues"),
    ("DevOps", "Docker, GitHub Actions, Azure DevOps, CI/CD"),
    ("Architecture", "Microservices, RESTful APIs, Clean Architecture"),
    ("Systems", "Linux (Arch, Ubuntu, Alpine), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# 7) REACT FRONTEND
# =============================================================================
sum_re_pt = ("Desenvolvedor Frontend com experiência em React, Next.js e TypeScript. Atuação em produtos "
             "full-stack com integração de APIs RESTful, pagamentos (Pix e cartão) e interfaces responsivas. "
             "Conhecimento em microsserviços, MongoDB e PostgreSQL. Estudante de Engenharia de Software "
             "pela PUCPR, com conclusão prevista para dezembro de 2026.")
sum_re_en = ("Frontend Developer experienced in React, Next.js and TypeScript. Worked on full-stack products "
             "with RESTful API integration, payments (Pix and card) and responsive interfaces. Knowledge of "
             "microservices, MongoDB and PostgreSQL. Software Engineering student at PUCPR, expected "
             "graduation December 2026.")

proj_re_pt = [
    ("Vitrines", "Next.js, Tailwind, PWA", None, None, [
        "Frontend de SaaS para criadores venderem pelo link da bio: páginas de loja, checkout com cartão e Pix, painel de pedidos e i18n.",
        "Monorepo Bun com app Expo compartilhando validação e tipos por pacotes comuns; deploy com Docker Compose e Caddy."]),
    ("manifestacao.online", "Next.js 16, WebSocket, Canvas", None, None, [
        "Mural coletivo de pixels sobre o mapa do Brasil: Next.js 16 (App Router) com Canvas 2D, tempo real por WebSocket (snapshot binário e ressincronização automática) e pagamentos Pix com fallback em cartão.",
        "Autenticação Google (Neon Auth), denúncias com painel admin e moderação automática por volume, e prévia Open Graph gerada ao vivo."]),
    ("ChromaString", "React, Vite, Tailwind CSS", "luis-ota.github.io/chromastring", "https://luis-ota.github.io/chromastring/", [
        "Aplicação web que transforma qualquer texto em uma cor hexadecimal determinística, com preview instantâneo, cópia em um clique e layout responsivo."]),
    ("Medica.ly", "Projeto Universitário - PUCPR", None, None, [
        "Interface responsiva em Angular 12 com Angular Material para gestão de consultas médicas, integrada a APIs REST em ASP.NET Core."]),
]
proj_re_en = [
    ("Vitrines", "Next.js, Tailwind, PWA", None, None, [
        "SaaS frontend for creators selling via bio link: store pages, card and Pix checkout, order dashboard and i18n.",
        "Bun monorepo with an Expo app sharing validation and types through common packages; deployment with Docker Compose and Caddy."]),
    ("manifestacao.online", "Next.js 16, WebSocket, Canvas", None, None, [
        "Collective pixel mural over the map of Brazil: Next.js 16 (App Router) with Canvas 2D, real-time over WebSocket (binary snapshot and automatic resync) and Pix payments with card fallback.",
        "Google auth (Neon Auth), report tooling with an admin panel and automatic volume-based moderation, plus live-generated Open Graph previews."]),
    ("ChromaString", "React, Vite, Tailwind CSS", "luis-ota.github.io/chromastring", "https://luis-ota.github.io/chromastring/", [
        "Web app that turns any text into a deterministic hexadecimal color, with instant preview, one-click copy and a responsive layout."]),
    ("Medica.ly", "University Project - PUCPR", None, None, [
        "Responsive Angular 12 interface with Angular Material for medical appointment management, integrated with ASP.NET Core REST APIs."]),
]

skills_re_pt = [
    ("Linguagens", "TypeScript, JavaScript, Python"),
    ("Frontend", "React, Next.js, Angular, Tailwind CSS, Vite, Streamlit"),
    ("Mobile", "React Native, Expo, Flutter (Dart)"),
    ("Backend", "Node.js, Python (Flask, FastAPI, Django)"),
    ("Bancos de Dados", "PostgreSQL, MongoDB, Firebase, SQLite"),
    ("Pagamentos", "Pix, cartão de crédito"),
    ("DevOps", "Vercel, Netlify, Docker, GitHub Actions, CI/CD"),
    ("Sistemas", "Linux (Arch, Ubuntu), Windows"),
    ("Versionamento", "Git (GitHub)"),
]
skills_re_en = [
    ("Languages", "TypeScript, JavaScript, Python"),
    ("Frontend", "React, Next.js, Angular, Tailwind CSS, Vite, Streamlit"),
    ("Mobile", "React Native, Expo, Flutter (Dart)"),
    ("Backend", "Node.js, Python (Flask, FastAPI, Django)"),
    ("Databases", "PostgreSQL, MongoDB, Firebase, SQLite"),
    ("Payments", "Pix, credit card"),
    ("DevOps", "Vercel, Netlify, Docker, GitHub Actions, CI/CD"),
    ("Systems", "Linux (Arch, Ubuntu), Windows"),
    ("Version Control", "Git (GitHub)"),
]

# =============================================================================
# Geração
# =============================================================================
JOBS = [
    ("pt-BR/PT-CSharp-Backend-Luis-Otavio", "pt", "Desenvolvedor Backend C#", sum_cs_pt, proj_cs_pt, skills_cs_pt),
    ("pt-BR/PT-Data-Developer-Luis-Otavio", "pt", "Desenvolvedor de Dados", sum_data_pt, proj_data_pt, skills_data_pt),
    ("pt-BR/PT-Flutter-Mobile-Luis-Otavio", "pt", "Desenvolvedor Mobile", sum_fl_pt, proj_fl_pt, skills_fl_pt),
    ("pt-BR/PT-FullStack-Luis-Otavio", "pt", "Desenvolvedor Full Stack", sum_fs_pt, proj_fs_pt, skills_fs_pt),
    ("pt-BR/PT-Java-Backend-Luis-Otavio", "pt", "Desenvolvedor Backend Java", sum_java_pt, proj_java_pt, skills_java_pt),
    ("pt-BR/PT-Python-Backend-Luis-Otavio", "pt", "Desenvolvedor Backend Python", sum_py_pt, proj_py_pt, skills_py_pt),
    ("pt-BR/PT-React-Frontend-Luis-Otavio", "pt", "Desenvolvedor Frontend React", sum_re_pt, proj_re_pt, skills_re_pt),
    ("en/EN-CSharp-Backend-Luis-Otavio", "en", "C# Backend Developer", sum_cs_en, proj_cs_en, skills_cs_en),
    ("en/EN-Data-Developer-Luis-Otavio", "en", "Data Developer", sum_data_en, proj_data_en, skills_data_en),
    ("en/EN-Flutter-Mobile-Luis-Otavio", "en", "Mobile Developer", sum_fl_en, proj_fl_en, skills_fl_en),
    ("en/EN-FullStack-Luis-Otavio", "en", "Full-Stack Developer", sum_fs_en, proj_fs_en, skills_fs_en),
    ("en/EN-Java-Backend-Luis-Otavio", "en", "Java Backend Developer", sum_java_en, proj_java_en, skills_java_en),
    ("en/EN-Python-Backend-Luis-Otavio", "en", "Python Backend Developer", sum_py_en, proj_py_en, skills_py_en),
    ("en/EN-React-Frontend-Luis-Otavio", "en", "React Frontend Developer", sum_re_en, proj_re_en, skills_re_en),
]

if __name__ == "__main__":
    for name, lang, headline, summary, projects, skills in JOBS:
        path = str(OUT / f"{name}.docx")
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        exps = EXP_PT if lang == "pt" else EXP_EN
        edu = EDU_PT if lang == "pt" else EDU_EN
        langs = LANG_PT if lang == "pt" else LANG_EN
        courses = COURSES_PT if lang == "pt" else COURSES_EN
        build_cv(path, lang, headline, summary, projects, skills, exps, edu, langs, courses)
        print("OK:", path)
    print(f"\n{len(JOBS)} currículos gerados em {OUT}")
