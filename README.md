# Multi-Step Agent System (Workflow-based)

##  Project Overview

This project implements a **workflow-based AI Agent system** for controlled multi-step task execution.

Unlike naive LLM agents, this system focuses on:

- Structured task decomposition
- Controlled execution flow
- Tool integration
- Error handling and robustness

The goal is to make LLM-based agents **reliable, debuggable, and production-ready**.

---

##  My Contributions

- Designed **Planner + Executor architecture**
- Built **multi-step workflow control (state machine)**
- Implemented **tool calling system (search / compute / analysis)**
- Added **execution control (step limit / retry / fallback)**
- Developed **memory module** for multi-step context tracking
- Improved system stability and avoided infinite loops

---

##  System Architecture

User Query
↓
Planner (task decomposition)
↓
Workflow Controller
↓
Executor
↓
Tool Calls
↓
Memory Update
↓
Final Output

---

##  Key Features

- Planner + Executor design
- Workflow control (state machine / DAG)
- Tool abstraction (search / python / SQL)
- Memory support (context tracking)
- Error handling (retry / fallback)
- Step limit to prevent infinite loops
