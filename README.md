# AI-Powered Cosplay Photography Booth

This project is an AI-powered photography booth designed for cosplay events and gaming conventions. It streamlines the process of capturing, processing, and delivering high-quality cosplay photos to attendees.

## Features

- **Check-in**: Attendees can check in at the booth and provide details about their cosplay, including the character, fandom, desired background, mood, and style.
- **Photography**: Our skilled photographer captures reference and action shots of the cosplayers.
- **AI Processing**: The photos are processed through a ComfyUI workflow, which applies AI-based enhancements and transformations based on the cosplayer's preferences.
- **Finalization**: The processed images undergo a final review and touch-up by our staff before being prepared for delivery.
- **Gallery**: Cosplayers can view their photos in a dedicated online gallery, which is automatically updated as the images move through the processing pipeline.
- **Queue Management**: Our staff can monitor and manage the queue of jobs, viewing details such as job status, cosplayer information, and creation/update times.

## Tech Stack

- **Backend**: Python, Flask, SQLAlchemy
- **Frontend**: HTML, CSS, JavaScript
- **AI Processing**: ComfyUI
- **Database**: SQLite

## Setup

1. Clone the repository.

2. Install the required Python packages:
`pip install -r requirements.txt`

3. Set up the ComfyUI workflow:
   - Install ComfyUI following the official documentation
   - Create a workflow that takes the raw photos as input and applies the desired AI enhancements
   - Configure the workflow to save the processed images in the designated job directory

4. Start the Flask server:
`python run.py`

5. Access the application in your web browser at `http://localhost:5000`

## Contributing

We welcome contributions to improve and expand the functionality of the Cosplay Photography Booth. If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

We would like to thank the following open-source projects and libraries that made this application possible:

- [Flask](https://flask.palletsprojects.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## Contact

For any inquiries or questions, please contact our team at hallo@andersundbesser.de.
