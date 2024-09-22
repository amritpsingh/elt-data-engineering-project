# ELT Data Engineering Project

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Setup Instructions](#setup-instructions)
6. [Usage Guide](#usage-guide)
7. [Data Flow](#data-flow)
8. [Customization](#customization)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)
11. [License](#license)

## Project Overview

This project demonstrates a robust Extract, Load, Transform (ELT) data pipeline using modern data engineering tools and practices. The pipeline extracts data from a source PostgreSQL database, loads it into a destination database, and performs transformations using dbt (data build tool). The entire process is orchestrated using Apache Airflow, with all components containerized using Docker for easy deployment and scalability.

Key features of this project include:
- Containerized services using Docker and Docker Compose
- Data extraction and loading with custom Python scripts
- Data transformation using dbt
- Workflow orchestration with Apache Airflow
- Data quality checks and testing

## Technologies Used

- Docker and Docker Compose
- PostgreSQL
- Apache Airflow
- dbt (data build tool)
- Python

## Project Structure

```
ELT-DEMO/
│   ├── airflow/
│   │   ├── dags/
│   │   │   └── elt_dag.py
│   │
│   ├── custom_postgres/
│   │   ├── models/
│   │   │   └── example/
│   │   │       ├── actors.sql
│   │   │       ├── film_actors.sql
│   │   │       ├── film_ratings.sql
│   │   │       └── films.sql
│   │   ├── macros/
│   │   │   └── film_ratings_macro.sql
│   │   └── dbt_project.yml
│   │
│   ├── elt/
│   │   ├── Dockerfile
│   │   └── elt_script.py
│   │
│   ├── source_db_init/
│   │   └── init.sql
│   │
│   ├── docker-compose.yaml
│   ├── Dockerfile
│   ├── elt.sh
│   ├── start.sh
│   └── stop.sh
│
├── .gitignore
├── README.md
└── LICENSE
```

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:
- Docker and Docker Compose
- Git

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your-username/elt-data-engineering-project.git
   cd elt-data-engineering-project
   ```

2. Create a `.env` file in the root directory and add the following environment variables:
   ```
   POSTGRES_USER=admin
   POSTGRES_PASSWORD=admin
   SOURCE_DB_NAME=source_db
   DESTINATION_DB_NAME=destination_db
   ```

3. Build and start the Docker containers:
   ```
   ./start.sh
   ```

   This script will initialize the Airflow database and start all necessary containers.

4. Access the Airflow web interface:
   Open a web browser and navigate to `http://localhost:8080`. Log in with the following credentials:
   - Username: airflow
   - Password: airflow

## Usage Guide

1. **Trigger the ELT process:**
   - In the Airflow web interface, navigate to the DAGs page.
   - Find the `elt_and_dbt` DAG and toggle it on.
   - Click on the "Trigger DAG" button to start the ELT process.

2. **Monitor the process:**
   - Click on the `elt_and_dbt` DAG to view its details.
   - Navigate to the "Graph View" to see the progress of individual tasks.

3. **View transformed data:**
   - Once the DAG run is complete, you can connect to the destination PostgreSQL database to view the transformed data.
   - Use a PostgreSQL client and connect with the following details:
     - Host: localhost
     - Port: 5434
     - Database: destination_db
     - Username: admin
     - Password: admin

4. **Stop the project:**
   When you're done, stop all containers using:
   ```
   ./stop.sh
   ```

## Data Flow

1. Source data is initialized in the source PostgreSQL database using `source_db_init/init.sql`.
2. The Airflow DAG triggers the ELT process:
   - Data is extracted from the source database and loaded into the destination database.
   - dbt models are run to transform the data in the destination database.
3. Transformed data is available in the destination database for analysis.

## Customization

- To modify the source data, edit the `source_db_init/init.sql` file.
- To change the transformations, modify the SQL files in the `custom_postgres/models/` directory.
- To adjust the Airflow DAG, edit the `airbyte/airflow/dags/elt_dag.py` file.

## Troubleshooting

- If containers fail to start, check Docker logs:
  ```
  docker-compose logs
  ```
- For Airflow task failures, check task logs in the Airflow web interface.
- Ensure all required ports (5433, 5434, 8080) are available on your system.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
