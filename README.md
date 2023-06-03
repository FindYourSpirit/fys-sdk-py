# FYS SDK for FYS API

The FYS SDK is a Python library that provides an easy-to-use interface for interacting with the FYS API. It simplifies the process of integrating your applications with the FYS platform and accessing its features.

## Features

- **Simplified API Calls**: The SDK encapsulates the complexity of API requests and responses, allowing you to make API calls using simple methods.
- **Authentication Handling**: The SDK provides built-in authentication mechanisms and helps you manage authentication tokens or credentials required for accessing the FYS API securely.
- **Error Handling**: Easily handle and manage errors returned by the API, including custom exception types specific to the SDK.
- **High-Level Abstractions**: The SDK provides high-level abstractions and data models that align with the concepts and entities of the FYS API, making it easier to work with the API data.

## Installation

You can install the FYS SDK via [PyPI](https://pypi.org/project/fys-sdk/). Simply run the following command:

	pip install fys-sdk



## Usage

To get started with the FYS SDK, follow these steps:

1. **Initialize the SDK**: Create an instance of the `SdkClient` class by passing the appropriate configuration options.

   ```python
   from fys_sdk import SdkClient, SdkConfiguration

   configuration = SdkConfiguration(api_key, base_url)
   client = SdkClient(configuration)


2. Make API Requests: Use the methods provided by the SdkClient class to interact with the FYS API.
   ```python
	endpoint = "/api/resource"
	response = await client.GetApiResponseAsync(endpoint)

3. Handle Responses: Process the API responses according to your application's requirements.

   ```python
	if response:
		# Handle the successful API response
	else:
		# Handle the empty or error response

## Testing
The FYS SDK includes a set of unit tests to ensure the correctness and reliability of the library. These tests are written using the unittest framework, a standard testing framework in Python.

To run the tests:

1. Open the terminal and navigate to the SDK project directory.

2. Run the following command to execute all the tests:

   ```python
	python -m unittest discover tests

## Contributing
Contributions to the FYS SDK are welcome! If you find any issues, have feature requests, or want to contribute improvements, please submit them via GitHub issues or create a pull request.

