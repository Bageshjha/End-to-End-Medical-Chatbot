# End-to-End-Medical-Chatbot 



This project sets up an end-to-end pipeline using Pinecone, LangChain, and Hugging Face embeddings. 
It is a Flask-based application structured for easy setup and modular code maintenance.



### Setup Instructions

1. **Install Dependencies**  
   Run the following command to install the required packages:
   ```bash
   pip install -r requirements.txt
### Step 2: Create environment variables
 "Creating .env file for environment variables."
 "Please replace <your-pinecone-api-key> with your actual API key in .env."
cat <<EOT >> .env
PINECONE_API_KEY=<your-pinecone-api-key>
EOT

### Step 3: Set up file structure
"Setting up project directories and files..."

declare a list_of_files=(

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
        "Created directory: $dirpath"
    fi

    # Create empty file if it doesn't exist or is empty
    if [ ! -f "$filepath" ] || [ ! -s "$filepath" ]; then
        touch "$filepath"
        "Created empty file: $filepath"
    else
        "$filename already exists and is not empty."
    fi
done

### Step 4: Run the application
echo -e "\nTo run the application, use the command:\npython app.py"

### Additional Usage Instructions
 #### Usage Instructions

"To start the Flask API server, run: python app.py"

"To test the application, run: python test.py"

"For research and trials, open the Jupyter notebook in the research folder: jupyter notebook research/trials.ipynb"

#### Setup complete! Happy coding!
