# AmiVerse Backend

## Installing dependencies

1. Install Python dependencies:

    ```shell
    poetry install
    ```

## Generating Protobuf

If you make any changes to the `amizone.proto` file, you'll need to regenerate the corresponding Python code. You can do this by running the following command:

```shell
make gen
```

## Run the server in dev mode

If you want to automatically restart the server whenever you make changes to the code, you can use watch mode. Run the following command:

```shell
make dev
```

## Good to knows

The server runs on port 8000 by default. username and password must be passed as query parameters for each request. For example:

```shell
localhost:8000?username=<username>&password=<password>
```

## Using a separate port

You can specify which port to use by adding ``--port <PORT>`` at the end of the dev command in makefile:

```makefile
dev:
	poetry run uvicorn main:app --reload --port 3030
````