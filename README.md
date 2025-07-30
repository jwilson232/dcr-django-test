# DCR - Django Test

A Django project to serve JSON API of country data


## Running the Project Locally

Follow these steps to get the project up and running on your local machine:

1. **Clone the repository**
    ```bash
    git clone git@github.com:jwilson232/dcr-django-test.git
    cd dcr-django-test
    ```

2. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Load country data**
    ```bash
    python testsite/manage.py update_country_listing
    ```

4. **Start the development server**
    ```bash
    python testsite/manage.py runserver
    ```

5. **Access the API**
    Navigate to [http://127.0.0.1:8000/countries/stats/](http://127.0.0.1:8000/countries/stats/)


## Testing the project


### Format the code

To format the code with black and isort use:

```bash
isort . && black .
```

### Running Tests

To run the test suite for the app use:

```bash
python testsite/manage.py test countries
```
