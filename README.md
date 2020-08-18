## Deployment
[Heroku](https://seamless-brian.herokuapp.com/)

## Running locally
1. `make docker-build`
2. `make docker-up`
3. Navigate to [localhost 7000](localhost:7000/)

## Technologies
From [Pipfile](https://github.com/brian-e-haley/seamless/blob/master/Pipfile)
* `Python ~= 3.8`
* `Django ~= 3.1`
* `python-dotenv ~= 0.14`
* `psycopg2 ~= 2.8`
* `django-heroku ~= 0.3`
* `gunicorn ~= 20.0`

## What it does
This is a very simple web app built with Django that parses 
[patient.json](https://github.com/brian-e-haley/seamless/blob/master/patients/source_data/patient.json)
to generate a `Patient` and `Condition`. This information is displayed on the `/` route as a list view.

### Patient
| Name | Data type | Comments |
| --- | --- | --- |
| `id` | integer | Django default auto increment |
| `first_name` | string |  |
| `last_name` | string |  |
| `organization` | string | |
| `gender` | string | Stores a single character representing `m` male, `f` female, or `u` undisclosed. |
| `conditions` | many-to-many |  |

### Condition
| Name | Data type | Comments |
| --- | --- | --- |
| `id` | integer | Django default auto increment |
| `name` | string |
