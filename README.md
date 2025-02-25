# Skin Cancer Detection

This repository contains a web application for detecting skin cancer using a deep learning model. The application allows users to upload an image of a skin lesion and receive a prediction on whether the lesion is benign or malignant.

## Live URL

The application is currently live at [anilenambiar.com](http://anilenambiar.com).

## Project Structure

- [`app.py`](app.py ): The main Flask application file.
- [`model.py`](model.py ): Contains the function to load the pre-trained model.
- [`Procfile`](Procfile ): Configuration file for deploying the app with Gunicorn.
- [`requirements.txt`](requirements.txt ): Lists the dependencies required for the project.
- [`skin_cancer_model_VGG16_v1.h5`](skin_cancer_model_VGG16_v1.h5 ): The pre-trained model file.
- [`static`](static ): Directory for static files like CSS.
- [`templates`](templates ): Directory for HTML templates.
- [`testing.ipynb`](testing.ipynb ): Jupyter notebook for testing the model.
- [`training.ipynb`](training.ipynb ): Jupyter notebook for training the model.
- [`uploads`](uploads ): Directory for storing uploaded images.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/skin-cancer-detection.git
    cd skin-cancer-detection
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    flask run
    ```

## Usage

1. Open the application in your web browser.
2. Upload an image of a skin lesion.
3. View the prediction result.

## Model Training

The model is trained using a VGG16 architecture. The training process is documented in the [`training.ipynb`](training.ipynb ) notebook.

## Model Testing

The model is tested using the [`testing.ipynb`](testing.ipynb ) notebook. The notebook includes evaluation metrics such as loss, accuracy, classification report, and confusion matrix.

## Dataset

International Skin Imaging Collaboration. SIIM-ISIC 2020 Challenge Dataset. International Skin Imaging Collaboration https://doi.org/10.34970/2020-ds01 (2020).

Creative Commons Attribution-Non Commercial 4.0 International License.

The dataset was generated by the International Skin Imaging Collaboration (ISIC) and images are from the following sources: Hospital Clínic de Barcelona, Medical University of Vienna, Memorial Sloan Kettering Cancer Center, Melanoma Institute Australia, The University of Queensland, and the University of Athens Medical School.

You should have received a copy of the license along with this work.

If not, see [https://creativecommons.org/licenses/by-nc/4.0/legalcode.txt](https://creativecommons.org/licenses/by-nc/4.0/legalcode.txt).

## Deployment

The application is deployed using Gunicorn. The [`Procfile`](Procfile ) contains the necessary configuration:
