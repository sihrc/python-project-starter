# {{package}}

{{description}}

Built on: Python3 and Docker (alpine) and Poetry (Package Manager)<br>
Maintained by: {{author}} [{{email}}]

## Getting Started

### Docker

- Additional Python3 dependencies can be added to requirements.txt<br>
- Tests are located in ./tests <br>
- To run the docker container with the basic requirements, dependencies, and the package installed:
  ```bash
  $ touch .env
  $ docker-compose up
  ```

### Poetry

```
$ poetry install
$ poetry run python3 -m {{package}}.main
```
