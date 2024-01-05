<p align="center">
    <h1 align="center">FASTAPI-MONGO-CRUD</h1>
</p>
<p align="center">
    <em>FastAPI-Mongo: Simplify CRUD with lightning speed!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/usmanmukhtar/FastAPI-Mongo-Crud?style=default&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/usmanmukhtar/FastAPI-Mongo-Crud?style=default&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/usmanmukhtar/FastAPI-Mongo-Crud?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/usmanmukhtar/FastAPI-Mongo-Crud?style=default&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<hr>

##  Quick Links
- [ Quick Links](#-quick-links)
- [ Overview](#-overview)
- [ Repository Structure](#-repository-structure)
- [ Getting Started](#-getting-started)
    - [ Installation](#-installation)
    - [ Running FastAPI-Mongo-Crud](#-running-FastAPI-Mongo-Crud)
- [ Contributing](#-contributing)
- [ License](#-license)

---

##  Overview

FastAPI-Mongo-Crud is a project that provides a fast and efficient way to perform CRUD operations on a MongoDB database using a FastAPI framework. It offers a set of routes that allow users to interact with a social app collection, including creating, updating, and deleting todos. The project's value proposition lies in its simplicity and ease of use, enabling developers to quickly build and deploy applications that require basic CRUD functionality with a MongoDB backend. The codebase includes modules for handling database connections, defining data models, serializing data, and implementing the routes for the different HTTP methods. Overall, FastAPI-Mongo-Crud facilitates the development of scalable and performant applications that rely on MongoDB for data storage.

---

##  Repository Structure

```sh
└── FastAPI-Mongo-Crud/
    ├── config
    │   └── database.py
    ├── main.py
    ├── models
    │   └── todo.py
    ├── requirements.txt
    ├── routes
    │   └── route.py
    └── schema
        └── schemas.py
```

---

##  Getting Started

###  Installation

1. Clone the FastAPI-Mongo-Crud repository:
```sh
git clone https://github.com/usmanmukhtar/FastAPI-Mongo-Crud
```

2. Change to the project directory:
```sh
cd FastAPI-Mongo-Crud
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

###  Running FastAPI-Mongo-Crud
Use the following command to run FastAPI-Mongo-Crud:
```sh
uvicorn main:app --reload
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/usmanmukhtar/FastAPI-Mongo-Crud/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/usmanmukhtar/FastAPI-Mongo-Crud/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/usmanmukhtar/FastAPI-Mongo-Crud/issues)**: Submit bugs found or log feature requests for FastAPI-Mongo-Crud.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone <your-forked-repo-url>
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear and concise message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the [MIT](https://github.com/usmanmukhtar/FastAPI-Mongo-Crud/blob/main/LICENSE) License.

---
