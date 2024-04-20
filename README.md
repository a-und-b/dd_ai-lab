# Cosplay Photography Workflow

This project implements a workflow for cosplay photography, allowing cosplayers to have their photos taken, processed using AI-generated images, and receive the final results.

## Features

- Cosplayers can check in and provide their preferences for the photo shoot (background, style, character, mood).
- Photographers can take reference photos and select the best shots for further processing.
- AI-generated images are created based on the selected photos and cosplayer preferences.
- The final image can be manually edited and enhanced by the photographer.
- Cosplayers can access their photos and generated images through a unique QR code.

## Technologies Used

- Python
- SQLite
- SQLAlchemy
- Flask (optional, if using a web framework)
- ComfyUI

## Getting Started

### Prerequisites

- Conda (Miniconda or Anaconda)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/cosplay-photography.git
   ```

2. Change into the project directory:

   ```bash
   cd cosplay-photography
   ```

3. Create a Conda environment using the `environment.yaml` file:

   ```bash
   conda env create -f environment.yaml
   ```

4. Activate the Conda environment:

   ```bash
   conda activate cosplay-photography
   ```

### Configuration

1. Open the `config.py` file and configure the necessary settings, such as database connection details, file paths, etc.

### Running the Application

1. Make sure the Conda environment is activated:

   ```bash
   conda activate cosplay-photography
   ```

2. Run the application:

   ```bash
   python run.py
   ```

3. Access the application in your web browser at `http://localhost:5000` (if using Flask).

## Project Structure

```
cosplay-photography/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── cosplayer_service.py
│   │   └── job_service.py
│   └── utils/
│       ├── __init__.py
│       └── database.py
├── data/
│   └── cosplay_photography.db
├── jobs/
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_routes.py
│   └── test_services.py
├── .gitignore
├── config.py
├── environment.yaml
└── run.py
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).