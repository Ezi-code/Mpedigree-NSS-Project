# InvoiceApp

InvoiceApp is a Django project that allows users to create invoices through form input and file upload. It also provides an API endpoint for listing all invoices and creating invoices through file upload.

## Installation

1. Clone the repository:
   - thte code is in the master branch of the repo, not the main branch.

```shell
git clone https://github.com/Ezi-code/Mpedigree-NSS-Project.git
```

2. Navigate to the project directory:

```shell
cd InvoiceApp
```

3. Create a virtual environment:

```shell
python -m venv env
```

4. Activate the virtual environment:

- For mac or linux:

```shell
source env/bin/activate
```

- For windows PCs:

```shell
env\Scripts\activate
```

5. Install the required dependencies:

```shell
pip install -r requirements.txt
```

6. Run database migrations:

```shell
python manage.py migrate
```

7. Start the development server:

```shell
python manage.py runserver
```

## Usage

### Web Interface

1. Open your web browser and navigate to `http://localhost:8000/main/list-invoice/`.
2. Fill in the invoice details using the provided form.
3. Optionally, you can upload a file containing additional invoice information.
4. Click the "Create Invoice" button to submit the form and create the invoice.

### API Endpoint

#### List all invoices

- Endpoint: `/api/list-invoice/`
- Method: GET
- Response: JSON array containing all invoices

#### Create invoice through file upload

- Endpoint: `/api/create-invoice/`
- Method: POST
- Request: Multipart form data with the following fields:
  - `csv_file`: The file containing additional invoice information
- Response: JSON object representing the created invoice

## Docker Setup

To run the InvoiceApp project using Docker, follow these steps:

1. Install Docker on your machine if you haven't already. You can download Docker from the official website: [https://www.docker.com/get-started](https://www.docker.com/get-started).

2. Build the Docker image for the project:

```shell
docker build -t invoice-app .
```

3. Run the Docker container:

```shell
docker run -p 8000:8000 invoice-app
```

4. Open your web browser and navigate to `http://localhost:8000` to access the InvoiceApp.

## Usage with Docker

Once the Docker container is running, you can use the InvoiceApp in the same way as described in the previous section.

### API Endpoint

The API endpoints for listing all invoices and creating invoices through file upload remain the same when using Docker.

## Contributing

Contributions are welcome! If you would like to contribute to InvoiceApp, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

The InvoiceApp project is licensed under the MIT License. For more details, refer to the [LICENSE](http://www.apache.org/licenses/) file.
