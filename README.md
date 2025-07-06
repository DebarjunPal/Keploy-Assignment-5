# Keploy-Assignment-5

## Org Chart API

A **RESTful API** built with [Drogon](https://github.com/drogonframework/drogon), a high-performance C++ framework. This API is designed to manage organizational structures—persons, departments, and job roles.  
**All routes are protected using JWT for token-based authentication.**

---

## 🚀 New Feature: Automated C++ Unit Test Generation with LLM

This repository now includes a tool to **automatically generate and refine C++ unit tests using a large language model (LLM)**, streamlining the process of writing comprehensive tests for C++ applications.

### 🛠️ Features

- **Automated Test Generation:** Uses a self-hosted or GitHub-hosted LLM (e.g., LLaMA) to analyze your C++ codebase and produce initial unit tests.
- **Iterative Test Improvement:** The LLM refines generated tests, removes duplicates, adds relevant libraries, and improves overall quality.
- **Build Integration:** Tests are built with your project. On failure, the LLM receives build logs and files to propose fixes.
- **Test Coverage Feedback:** After a successful build, test coverage data is sent back to the LLM for further test enhancements.
- **Final Output:** Provides a clean `tests` folder with high-quality, non-duplicate, and properly formatted unit tests, plus a brief test coverage report.

### 🧑‍💻 How It Works

1. **Setup the Environment**
   - Create or use a working directory for your project.
   - Ensure a C++ compiler and a testing framework like Google Test are installed.
   - Choose your LLM setup (self-hosted or GitHub-hosted).

2. **Initial Test Generation**
   - The tool takes your C++ project as input.
   - Sends the code with a strict YAML instruction file to the LLM.
   - LLM generates initial unit tests and saves them in the `tests` folder.

3. **Refine the Tests**
   - The tool sends generated tests back to the LLM.
   - The LLM removes duplicates, adds necessary libraries, and refines the tests.

4. **Build and Debug**
   - The tool builds the project with the generated tests.
   - If the build fails, the LLM receives the relevant files and build logs for fixes.
   - If the build passes, test coverage is measured and reported to the LLM for further improvement.

5. **Final Output**
   - The tool outputs a final `tests` folder with all improved unit tests and a report on test coverage achieved.

### 📂 Project Structure (Relevant to Test Generation)

```
project-root/
│
├── src/             # Source files
├── tests/           # Auto-generated and iteratively improved unit tests
│   └── ...          # (Final, non-duplicate, formatted tests)
├── test_coverage/   # (Optional) Test coverage reports
├── ...              # Other standard directories
└── README.md
```

### 📋 Example Workflow

1. **Run the LLM-based generator:**
   ```bash
   # Command may vary depending on your wrapper script
   python generate_tests.py --input ./src --output ./tests
   ```
2. **Build and run tests:**
   ```bash
   mkdir build && cd build
   cmake ..
   make
   ctest
   ```
3. **Review test coverage:**
   - Coverage reports will be found in `test_coverage/` after the build.
   - The tool will summarize the coverage in the final report.

4. **Final Submission:**
   - Submit the `tests` folder and the coverage report as part of your deliverables.

---

## 📚 API Endpoints

### 👤 Persons

| Method   | URI                                                       | Action                    |
| -------- | --------------------------------------------------------- | ------------------------- |
| `GET`    | `/persons?limit={}&offset={}&sort_field={}&sort_order={}` | Retrieve all persons      |
| `GET`    | `/persons/{id}`                                           | Retrieve a single person  |
| `GET`    | `/persons/{id}/reports`                                   | Retrieve direct reports   |
| `POST`   | `/persons`                                                | Create a new person       |
| `PUT`    | `/persons/{id}`                                           | Update a person's details |
| `DELETE` | `/persons/{id}`                                           | Delete a person           |

### 🏢 Departments

| Method   | URI                                                           | Action                      |
| -------- | ------------------------------------------------------------- | --------------------------- |
| `GET`    | `/departments?limit={}&offset={}&sort_field={}&sort_order={}` | Retrieve all departments    |
| `GET`    | `/departments/{id}`                                           | Retrieve a department       |
| `GET`    | `/departments/{id}/persons`                                   | Retrieve department members |
| `POST`   | `/departments`                                                | Create a department         |
| `PUT`    | `/departments/{id}`                                           | Update department info      |
| `DELETE` | `/departments/{id}`                                           | Delete a department         |

### 💼 Jobs

| Method   | URI                                                     | Action                        |
| -------- | ------------------------------------------------------- | ----------------------------- |
| `GET`    | `/jobs?limit={}&offset={}&sort_fields={}&sort_order={}` | Retrieve all job roles        |
| `GET`    | `/jobs/{id}`                                            | Retrieve a job role           |
| `GET`    | `/jobs/{id}/persons`                                    | Retrieve people in a job role |
| `POST`   | `/jobs`                                                 | Create a job role             |
| `PUT`    | `/jobs/{id}`                                            | Update job role               |
| `DELETE` | `/jobs/{id}`                                            | Delete a job role             |

### 🔐 Auth

| Method | URI              | Action                              |
| ------ | ---------------- | ----------------------------------- |
| `POST` | `/auth/register` | Register a user and get a JWT token |
| `POST` | `/auth/login`    | Login and receive a JWT token       |

---

## 📦 Project Setup (API)

### Docker (Recommended)
```bash
git clone https://github.com/DebarjunPal/Keploy-Assignment-5.git
cd Keploy-Assignment-5/orgChartApi
docker-compose up
```

### Manual
- Install system dependencies: GCC, CMake, PostgreSQL, OpenSSL, libjsoncpp-dev, Google Test, etc.
- See the original instructions above for detailed manual steps.

---

## 🏗️ Build the Project

```bash
mkdir build && cd build
cmake ..
make
```

---

## ▶️ Run the Application

After building and setting up `config.json` for DB config:
```bash
./org_chart
```
The app runs at [http://localhost:3000](http://localhost:3000).

---

## 🧯 Troubleshooting

- **OpenSSL not found?**
  ```bash
  cmake -DOPENSSL_ROOT_DIR=/usr/local/opt/openssl ..
  ```
- **LSP/IntelliSense not working?**
  ```bash
  cmake -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ..
  ```

---

## 🛠️ Tech Stack

- C++ (Drogon framework)
- PostgreSQL
- JWT for authentication
- Docker (optional for setup)
- Google Test (for unit testing)
- LLM-based automation for test generation and refinement

---
