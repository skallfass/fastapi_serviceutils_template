# Configuration


## config.yml

The service is configured using a config-file (`config.yml`).
It is possible to overwrite these setting using environment-variables.

The config contains four main sections:

* service
* external_resources
* logger
* available_environment_variables

!!! note

    For details about the yaml-filetype in general see [YAML](/references#yaml).


The config for this service should look like the following (with other values):

```yaml
service:
    name: 'exampleservice'
    mode: 'devl'
    port: 50001
    description: ''
    apidoc_dir: 'docs/_build'
    readme: 'README.md'
    allowed_hosts:
        - '*'
    use_default_endpoints:
        - alive
        - config
external_resources:
    databases: null
    services: null
    other: null
logger:
    path: './log/exampleservice'
    filename: 'service_{mode}.log'
    level: 'debug'
    rotation: '1 days'
    retention: '1 months'
    format: "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> [id: {extra[request_id]}] - <level>{message}</level>"

available_environment_variables:
    env_vars:
        - EXAMPLESERVICE__SERVICE__MODE
        - EXAMPLESERVICE__SERVICE__PORT
        - EXAMPLESERVICE__LOGGER__LEVEL
        - EXAMPLESERVICE__LOGGER__PATH
        - EXAMPLESERVICE__LOGGER__FILENAME
        - EXAMPLESERVICE__LOGGER__ROTATION
        - EXAMPLESERVICE__LOGGER__RETENTION
        - EXAMPLESERVICE__LOGGER__FORMAT
    external_resources_env_vars: []
    rules_env_vars: []
```


## config: [service]

Inside this section we define the name of the service `name`.
This name is used for the OpenAPI-documentation and extraction of the
environment-variables.

The `mode` define the runtime-mode of the service.
This mode can be overwritten with the environment-variable
`EXAMPLESERVICE__SERVICE__MODE` (where `'EXAMPLESERVICE'` is the name of
the service, meaning if you have a service named `SOMETHING` the
environment-variable would be `SOMETHING__SERVICE__MODE`).

The `port` configure the port the service will listen to.
This can also be overwritten using the environment variable
`EXAMPLESERVICE__SERVICE__PORT`.

The `description` is used for the swagger-documentation.

To define the folder where the to find the apidoc to serve by route
`/api/apidoc/index.html` the keyword `apidoc_dir` is used.

`readme` defines where to get the readme from to be used as main description
for the swagger-documentation at `/docs` / `/redoc`.

To control if only specific hosts are allowed to access the service we use
`allowed_hosts`.
Per default a service would allow all hosts (`*`) but this can be
customized here in the config.

To define which default endpoints should be included in our service we use
`use_default_endpoints`.
Currently we support the default endpoints `/api/alive` (inside config:
`'alive'`) and `/api/config` (inside config: `'alive'`).


## config: [external_resources]

Inside this section external dependencies (resources) are defines.
A service can depend on other services, databases, remote-connections or
files / folders.

Dependencies to other services should be defined inside `services`.
Database connections inside `databases` (currently only postgres is
supported).
If any other dependency exist define it in `other`.

Defined services can be accessed in the code using
`app.config.external_resources.services` or
`ENDPOINT.config.external_resources.services` depending if you are in a main
part of the app or inside an endpoint.

Databases are automatically included into the `startup` and `shutdown`
handlers.
You can access the database connection using `app.databases['DATABASE_NAME']`
or `ENDPOINT.databases['DATABASE_NAME']` depending if you are in a main part
of the app or inside an endpoint.


## config: [logger]

All settings inside this section are default Loguru_ settings to configure the
logger.
You can control where to log (`path`) and how the logfile should be named
(`filename`).
Also which minimum level to log (`level`).
To control when to rotate the logfile use `rotation`.
`retention` defines when to delete old logfiles.
The `format` defines the format to be used for log-messages.


## config: [available__environment_variables]

The environment-variables are separated into three types:

* `env_vars`
* `external_resources_env_vars`
* `rules_env_vars`

Here you can control which environment-variables to use if they are set.

The environment-variables are named like the following:
`<SERVICENAME>__<MAJOR_SECTION>__<PARAMETER_NAME>`.
The servicename would be `'EXAMPLESERVICE'` in our example.
The major-section is one of:

* `'SERVICE'`
* `'LOGGER'`
* `'EXTERNAL_RESOURCES'`

`env_vars` control the sections `service` and `logger`.
`external_resources_env_vars` control the configurations inside the section
`external_resources`.
The `rules_env_vars` should overwrite settings of a ruleset of the service.
Such a ruleset defines constants and other rules for the logic of the
endpoints.
For example a default time-range for your pandas dataframes, etc.
Currently this is not implemented, so you would have to use these definitions
yourself to overwrite your ruleset-definitions.


## Environment-variables

Setting environment-variables overwrites the default values defined in the
`app/config.yml`.


!!! note

    For details about environment-variables in general see [Environment
    variable](/references#environment-variable).

The environment-variables for this service are:

* `SERVICENAME__SERVICE__MODE`
* `SERVICENAME__SERVICE__PORT`
* `SERVICENAME__LOGGER__PATH`
* `SERVICENAME__LOGGER__FILENAME`
* `SERVICENAME__LOGGER__ROTATION`
* `SERVICENAME__LOGGER__RETENTION`
* `SERVICENAME__LOGGER__FORMAT`
* `SERVICENAME__EXTERNAL_RESOURCES__DATABASES__<DATABASE_NAME>__DSN`
* `SERVICENAME__EXTERNAL_RESOURCES__DATABASES__<DATABASE_NAME>__DATABASETYPE`
* `SERVICENAME__EXTERNAL_RESOURCES__SERVICES__<SERVICE_NAME>__URL`
* `SERVICENAME__EXTERNAL_RESOURCES__SERVICES__<SERVICE_NAME>__SERVICETYPE`
* `SERVICENAME__EXTERNAL_RESOURCES__OTHER__<OTHER_NAME>__<OTHER_KEY>`

Please ensure to use the environment-variables if you want to overwrite some
default-settings of the service.

The environment-variables to be available should be defined inside the
`config.yml`.
Setting the values of the environment-variables is done inside the
`docker-compose.yml` during deployment (for details see
[deployment](../deployment/index.html)).
