# End-to-End-Medical-Chatbot

#!/bin/bash

# Project Title: Flask-based Data Extraction and Retrieval API
# Description: This project sets up an end-to-end pipeline using Pinecone, LangChain, and Hugging Face embeddings. 
# It is a Flask-based application structured for easy setup and modular code maintenance.

# Prerequisites: Python and pip must be installed.

echo "Setting up your project..."

# Step 1: Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Step 2: Create environment variables
echo "Creating .env file for environment variables. Replace <your-pinecone-api-key> with your actual API key."
cat <<EOT >> .env
PINECONE_API_KEY=<your-pinecone-api-key>
EOT

# Step 3: Set up file structure
echo "Setting up project directories and files..."
declare -a list_of_files=(
    "src/__init__.py"
    "src/helper.py"
    "src/prompt.py"
    ".env"
    "setup.py"
    "app.py"
    "research/trials.ipynb"
    "test.py"
)

for filepath in "${list_of_files[@]}"; do
    dirpath=$(dirname "$filepath")
    filename=$(basename "$filepath")

    # Create directories if they do not exist
    if [ ! -d "$dirpath" ]; then
        mkdir -p "$dirpath"
        echo "Created directory: $dirpath"
    fi

    # Create empty file if it doesn't exist or is empty
    if [ ! -f "$filepath" ] || [ ! -s "$filepath" ]; then
        touch "$filepath"
        echo "Created empty file: $filepath"
    else
        echo "$filename already exists and is not empty."
    fi
done

# Step 4: Run the application
echo "To run the application, use the following command:"
echo "python app.py"

# Additional Usage Instructions

echo ""
echo "## Usage Instructions"

# Run API
echo "To start the Flask API server, run:"
echo "python app.py"

# Test the application
echo "To test the application, run:"
echo "python test.py"

# Explore research notebook
echo "For research and trials, open the Jupyter notebook in the research folder:"
echo "jupyter notebook research/trials.ipynb"

echo ""
echo "Setup complete! Happy coding!"
