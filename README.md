# Deep Learning AI Assistant

A sophisticated deep learning system trained on extensive educational datasets to create an adaptive AI tutor, leveraging GPT-4o's capabilities through fine-tuning with specialized pedagogical conversation patterns and expert teaching methodologies.

## Setup Instructions

### 1. Installation

1. Clone this repository:
```bash
git clone https://github.com/MonkWarrior08/DeepTutor-AI.git
cd DeepTutor-AI
```

2. Install dependencies using the requirements file:
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration

1. Create a `.env` file in the project root:
```bash
touch .env  # macOS/Linux
# or manually create .env file in Windows
```

2. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```


### 3. OpenAI Setup

1. Create an OpenAI account and obtain an API key from [OpenAI Platform](https://platform.openai.com/)
2. Create a fine-tuning job with the following parameters:
   - Epochs: 10
   - Learning rate multiplier: 2
   - Batch size: 1

### 4. Knowledge Base Preparation
1. Academic Resources:
   - Research papers from arXiv
   - Deep learning textbooks
   - Academic course materials

2. Technical Documentation:
   - Framework documentation
   - Implementation guides
   - Best practices documents

3. Tutorial Content:
   - Online course materials
   - Code examples
   - Case studies

### 5. Vector Store Creation
1. Create vector store storage on the OpenAI plaftform
2. Upload the knowledge base to the created vector store

### 6. Assistant Configuration
1. Create a new assistant
2. Select the fine-tuned model
3. Connect the vector storage
4. Save the assistant ID

### 7. Application Setup
1. Open `main.py`
2. Replace the empty `assistant_id` variable with your assistant ID
3. Run the application:
```bash
python main.py
```

## Usage
- Get assistance with:
  - Deep learning concepts
  - Architecture design
  - Debugging
  - Best practices
  - Implementation guidance
- Exit by typing 'quit', 'exit', or 'bye'

## License
This project is licensed under the MIT License - see the LICENSE file for details.
