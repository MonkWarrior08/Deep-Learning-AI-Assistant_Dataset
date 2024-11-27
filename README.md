# Deep Learning AI Assistant

An AI assistant powered by OpenAI's API, specifically fine-tuned for Deep Learning education and assistance.

## Setup Instructions

### 1. Fine-tuning Setup
1. Create an OpenAI account and obtain an API key from [OpenAI Platform](https://platform.openai.com/)
2. Create a fine-tuning job on the OpenAI website using the provided JSONL file with the following parameters:
   - Epochs: 10
   - Learning rate multiplier: 2
   - Batch size: 1

### 2. Knowledge Base Preparation
Before creating the vector store, gather relevant deep learning materials from:
1. Academic Resources:
   - Research papers from arXiv
   - Deep learning textbooks (e.g., Deep Learning by Goodfellow et al.)
   - Academic course materials from top universities

2. Technical Documentation:
   - Framework documentation (PyTorch, TensorFlow, etc.)
   - Implementation guides
   - Best practices documents

3. Tutorial Content:
   - Online course materials
   - Code examples
   - Case studies

### 3. Vector Store Creation
1. Format your collected materials appropriately
2. Upload the knowledge base on the OpenAI platform to create a vector store storage
3. This will serve as the assistant's knowledge repository

### 4. Assistant Creation
1. Go to the [OpenAI Platform](https://platform.openai.com/)
2. Create a new assistant
3. Select the fine-tuned model created for deep learning
4. Connect the vector storage to the assistant
5. Save the assistant ID for later use

### 5. Environment Setup
1. Clone this repository:
```bash
git clone [repository-url]
```

2. Install required dependencies:
```bash
pip install openai python-dotenv
```

3. Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your-api-key-here
```

### 6. Running the Application
1. Open `main.py`
2. Replace the empty `assistant_id` variable with your assistant ID
3. Run the application:
```bash
python main.py
```

## Usage
- Type your message and press Enter to interact with the assistant
- The assistant can help with:
  - Deep learning concepts explanation
  - Architecture design recommendations
  - Debugging assistance
  - Best practices advice
  - Implementation guidance
- Type 'quit', 'exit', or 'bye' to end the conversation

## License
This project is licensed under the MIT License - see the LICENSE file for details.
